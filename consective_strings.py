def longest_string(strarr, k):
    # Create array with concatenated words.
    longest_arr = []
    for i, word in enumerate(strarr):
        if i <= len(strarr)-k:
            new_word = ""
            for f in range(k):
                new_word += strarr[i+f]
            longest_arr.append(new_word)

    # Find the longest word and return
    longest = ""
    for word in longest_arr:
        if len(word) > len(longest):
            longest = word
    return longest

strarr = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]

print(longest_string(strarr, 2))
