from dec2dpbcd import dec2dpbcd

DEC_LEN_32 = 7
DEC_LEN_64 = 16
BIAS_32 = 101
BIAS_64 = 398
E_LEN_32 = 8
E_LEN_64 = 10


def get_declen_bias_Elen(prec):
    if prec == "S":
        dec_len = DEC_LEN_32
        bias = BIAS_32
        E_len = E_LEN_32
    elif prec == "D":
        dec_len = DEC_LEN_64
        bias = BIAS_64
        E_len = E_LEN_64
    else:
        raise ValueError("Invalid precision value")

    return dec_len, bias, E_len


def get_sign_decstr(dec_str, dec_len):
    sign_bit = 0
    if dec_str[0] == "-":
        sign_bit = 1
        dec_str = dec_str[1:]
    dec_str = dec_str.zfill(dec_len)

    if len(dec_str) > dec_len:
        raise ValueError(f"Decimal length exceeds {dec_len} characters")

    return sign_bit, dec_str


def get_MSD_bin(dec_str):
    MSD = int(dec_str[0])
    return bin(MSD)[2:].zfill(4)


def get_E_bin(exp, bias, E_len):
    E = int(exp) + bias
    return bin(E)[2:].zfill(E_len)


def get_combi_field(E_bin, MSD_bin):
    if MSD_bin[0] == "0":
        combi_field = E_bin[:2] + MSD_bin[1:]
    else:
        combi_field = "11" + E_bin[:2] + MSD_bin[-1]
    return combi_field


def dec2bin2008(s):
    split_args = s.split()
    if len(split_args) != 3:
        raise ValueError("Incomplete arguments")

    precision, decimal_str, exponent = split_args

    decimal_len, bias, E_len = get_declen_bias_Elen(precision)

    sign_bit, decimal_str = get_sign_decstr(decimal_str, decimal_len)

    MSD_bin = get_MSD_bin(decimal_str)

    E_bin = get_E_bin(exponent, bias, E_len)

    combi_field = get_combi_field(E_bin, MSD_bin)

    exp_conti = E_bin[2:]

    coeff_contis = dec2dpbcd(decimal_str[1:])

    print(f"Sign bit: {sign_bit}")
    print(f"Combination field: {combi_field}")
    print(f"Exponent continuation: {exp_conti}")
    for idx, cc in enumerate(coeff_contis):
        print(f"Coefficient continuation {idx}: {cc}")


print("Input format:")
print("decimal32: S XXXXXXX X..X")
print("decimal64: D XXXXXXXXXXXXXXXX X..X")
print()
while True:
    dec2bin2008(input("Enter precision (S/D), decimal, and exponent: "))
    print()
