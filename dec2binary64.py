from dec2dpbcd import dec2dpbcd


def dec2binary64(s):
    dec_str, exp = s.split()

    sign_bit = 0
    if dec_str[0] == "-":
        sign_bit = 1
        dec_str = dec_str[1:]

    MSD = int(dec_str[0])
    MSD_bin = bin(MSD)[2:].zfill(4)

    E = int(exp) + 398
    E_bin = bin(E)[2:].zfill(10)

    combi_field = ""
    if MSD_bin[0] == "0":
        combi_field += E_bin[:2]
        combi_field += MSD_bin[1:]
    else:
        combi_field += "11"
        combi_field += E_bin[:2]
        combi_field += MSD_bin[-1]

    exp_conti = E_bin[2:]

    coeff_contis = dec2dpbcd(dec_str[1:])

    print(f"Sign bit: {sign_bit}")
    print(f"Combination field: {combi_field}")
    print(f"Exponent continuation: {exp_conti}")
    for idx, cc in enumerate(coeff_contis):
        print(f"Coefficient continuation {idx}: {cc}")


print("Input is 16-digit decimal and exponent")
print("Format: XXXXXXXXXXXXXXXX X..X")
print()
while True:
    dec2binary64(input("Enter 16-digit decimal and exponent: "))
    print()
