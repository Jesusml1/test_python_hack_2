"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(input):

    splited_word = list(input)
    if len(splited_word) > 3:
        splited_word.pop()
        splited_word.pop(0)

    result = ''.join(splited_word)
    return result