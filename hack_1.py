"""
generic script

text: "fooziman" output => "fOozIman"
text: "qux" output => "qUx"
text: "eq" output => "eq"
"""


def fn_hack_1(input):

    word_list = []
    word = []
    char_count = 0

    for i in range(len(input)):

        word.append(input[i])
        char_count += 1

        if char_count == 3:
            char_count = 0
            word_list.append(word)
            word = []

        if i == len(input) - 1 and len(word) > 0 and len(word) < 3:
            word_list.append(word)

    if(len(word_list) < 2 and len(word_list[0]) < 3):
        return input
    
    for i in range(len(word_list)):
        if len(word_list[i]) > 2:
            word_list[i][1] = word_list[i][1].upper()

    word_list_flatted = [item for sublist in word_list for item in sublist]
    result = "".join(word_list_flatted)

    return result


# print(fn_hack_1('fooziman'))