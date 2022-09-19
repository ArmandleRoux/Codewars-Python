def two_to_one(s1, s2):
    longest = ""
    for letter in s1 + s2:
        if letter not in longest:
            longest += letter
    return "".join(sorted(longest))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(two_to_one(a, b))
