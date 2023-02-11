"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

import re

def fn_hack_9(input):
    input.popitem()

    items = list(input.items())

    new_key = items[0][0].capitalize()
    new_value = items[0][1].capitalize()
    new_value = re.sub('[k]+','', new_value)

    return {new_key: new_value}
