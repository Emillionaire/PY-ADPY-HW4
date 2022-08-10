nested_list = [
    ['a', 'b', 'c'],
    ['d', [['e', 'x']], [[['f']]], 'h', False],
    [1, [[2]], None, 'h'],
    ['e', 'f', ['h', 1]],
    ['5', ['6'], '9', [4, 6, 8], [7, 8]]
]


def flat_generator(nested_list):
    # while True:
    for i in nested_list:
        if type(i) is list:
            yield from flat_generator(i)
        else:
            yield i


for item in flat_generator(nested_list):
    print(item)
