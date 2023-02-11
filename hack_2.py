"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(input):

    word = list(input)
    word_without_vowels = []

    for i in range(len(word)):
        if word[i] != 'a' and word[i] != 'e' and word[i] != 'i' and word[i] != 'o' and word[i] != 'u':
            word_without_vowels.append(word[i])

    result = ''.join(word_without_vowels)

    return result

# print(fn_hack_2("fooziman"))