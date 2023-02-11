"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(input):

    result = []
    counter = 1
    for i in range(len(input)):
        if i % 2 == 0:
            result.append({str(counter): str(counter + 1)})
        else:
            result.append({str(counter), str(counter + 1)})
        counter += 2

    return result