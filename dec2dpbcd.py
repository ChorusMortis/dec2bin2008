def dec2pbcd(s):
    return bin(int(s))[2:].zfill(4)


dpbcd_dict = {
    "000": "bcd fgh 0 jkm",
    "001": "bcd fgh 1 00m",
    "010": "bcd jkh 1 01m",
    "011": "bcd 10h 1 11m",
    "100": "jkd fgh 1 10m",
    "101": "fgd 01h 1 11m",
    "110": "jkd 00h 1 11m",
    "111": "00d 11h 1 11m",
}


def append_zeros(s):
    s = s.replace(" ", "")
    s_len = len(s)

    if s_len == 0:
        raise ValueError("Input cannot be empty string")
    if not s.isdecimal():
        raise ValueError("Input is decimal digits only")

    remainder = s_len % 3

    if remainder == 0:
        return s
    else:
        zeros_to_add = 1 if remainder == 2 else 2
        return s.zfill(s_len + zeros_to_add)


def group_decimals(s):
    s = append_zeros(s)
    # from https://stackoverflow.com/a/5711464
    return [s[i : i + 3] for i in range(0, len(s), 3)]


def dec2dpbcd(s):
    results = []
    decimal_groups = group_decimals(s)

    for dec_group in decimal_groups:
        nibbles = []
        for digit in dec_group:
            nibbles.append(dec2pbcd(digit))

        a, b, c, d = nibbles[0]
        e, f, g, h = nibbles[1]
        i, j, k, m = nibbles[2]

        pattern = dpbcd_dict[a + e + i]
        pattern = pattern.replace("b", b)
        pattern = pattern.replace("c", c)
        pattern = pattern.replace("d", d)
        pattern = pattern.replace("f", f)
        pattern = pattern.replace("g", g)
        pattern = pattern.replace("h", h)
        pattern = pattern.replace("j", j)
        pattern = pattern.replace("k", k)
        pattern = pattern.replace("m", m)

        results.append(pattern)

    return results
