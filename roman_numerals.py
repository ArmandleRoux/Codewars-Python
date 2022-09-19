def print_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    new_word = ""

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            new_word += sym[i]
            div -= 1
        i -= 1
    return new_word

print(print_roman(1824))
