def break_camel_case(s):
    new_word = ""
    for i, letter in enumerate(s):
        if letter.isupper():
            new_word += " " + letter
        else:
            new_word += letter
    return new_word
            
print(break_camel_case("helloWorldPapa"))