import string


def print_errors(s):
    alphabet = list(string.ascii_lowercase)
    denominator = len(s)
    numerator = 0
    for letter in s:
        if letter in alphabet[13:]:
            numerator += 1
    return str(numerator) + "/" + str(denominator)


print(print_errors("aaaxbbbbyyhwawiwjjjwwm"))