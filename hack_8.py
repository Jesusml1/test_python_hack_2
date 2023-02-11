"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(input):

    result = []
    if len(input) % 2 == 0:
        for i in range(len(input), 0, -1):
            result.append(str(i))
    else:
        for i in range(len(input), 0, -1):
            result.append(input[i - 1] + '-' + str(i))

    return result