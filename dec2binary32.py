from dec2dpbcd import dec2dpbcd


def dec2binary32(s):
    dec_str, exp = s.split()

    sign_bit = 0
    if dec_str[0] == "-":
        sign_bit = 1
        dec_str = dec_str[1:]

    MSD = int(dec_str[0])
    MSD_bin = bin(MSD)[2:].zfill(4)

    E = int(exp) + 101
    E_bin = bin(E)[2:].zfill(8)

    combi_field = ""
    if MSD_bin[0] == "0":
        combi_field += E_bin[:2]
        combi_field += MSD_bin[1:]
    else:
        combi_field += "11"
        combi_field += E_bin[:2]
        combi_field += MSD_bin[-1]

    exp_conti = E_bin[2:]

    coeff_conti1, coeff_conti2 = dec2dpbcd(dec_str[1:])

    print(f"Sign bit: {sign_bit}")
    print(f"Combination field: {combi_field}")
    print(f"Exponent continuation: {exp_conti}")
    print(f"Coefficient continuation 1: {coeff_conti1}")
    print(f"Coefficient continuation 2: {coeff_conti2}")


print("Input is 7-digit decimal and exponent")
print("Format: XXXXXXX X..X")
print()
while True:
    dec2binary32(input("Enter 7-digit decimal and exponent: "))
    print()
