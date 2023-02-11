"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(input):
    result = []
    if input == []:
        return ['0']

    for i in range(len(input)):
        if i % 2 == 0:
            result.append(str(i + 1))
        else:
            result.append('-')
    
    return result