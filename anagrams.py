def anagrams(prime_word, compare_list):
    anagrams_list = []
    prime_word = sorted(prime_word)
    for word in compare_list:
        if len(word) != len(prime_word):
            continue
        if word == prime_word:
            anagrams_list.append(word)
        elif prime_word == sorted(word):
            anagrams_list.append(word)
    return anagrams_list


def anagram(word, words):
    word = sorted(word)
    return [item for item in words if sorted(item) == word]

print(anagram('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagram('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagram('laser', ['lazing', 'lazy',  'lacer']))

