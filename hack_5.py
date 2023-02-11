"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(input):
    result = []
    if not input.startswith('f'):
        count = 0

        for i in range(len(input)):
            if count < 2:
                result.append(input[i])
            else:
                result.append('-')
                count = 0
                continue

            count += 1
    else:
        part_1 = input[:int(len(input) / 2)] # fooz
        part_2 = input[int(len(input) / 2) : len(input)] # iman

        word_1 = []
        word_2 = []

        for i in range(len(part_1)):
            if i == 2:
                word_1.append('-')
            else:
                word_1.append(part_1[i])
        
        for i in range(len(part_2)):
            if i == 0:
                word_2.append(part_2[i] + '-')
            elif i == len(part_2) - 1:
                word_2.append('-')
            else:
                word_2.append(part_2[i])

        return ''.join(word_1) + ''.join(word_2)


    result = ''.join(result)
    return result