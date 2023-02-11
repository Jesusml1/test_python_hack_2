"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(input):

    splited_word = list(input)
    new_word = []

    for i in range(len(splited_word)):
        if splited_word[i] == 'a':
            new_word.append('@')
        elif splited_word[i] == 'e':
            new_word.append('3')
        elif splited_word[i] == 'i':
            new_word.append('¡')
        elif splited_word[i] == 'o':
            new_word.append('0')
        elif splited_word[i] == 'u':
            new_word.append('v')
        elif i == 0 or i == len(splited_word) - 1:
            new_word.append(splited_word[i].upper())
        else:
            new_word.append(splited_word[i])
        
    result = ''.join(new_word)

    return result