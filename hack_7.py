"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(input):
    result = []
    if input == [0]:
        return [0]

    for i in range(len(input)):
        if i % 2 == 0:
            result.append(str(i + 1))
        else:
            result.append(i + 1)
    
    return result