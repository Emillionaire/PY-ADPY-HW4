nested_list = [
    ['a', 'b', 'c'],
    ['d', [['e', 'x']], [[['f']]], 'h', False],
    [1, [[2]], None, 'h'],
    ['e', 'f', ['h', 1]],
    ['5', ['6'], '9', [4, 6, 8], [7, 8]]
]


class FlatIterator:
    def __init__(self, nested_list):
        result = self.unpacker(nested_list)
        self.start = result[0]
        self.end = len(result)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= self.end:
            raise StopIteration
        return nested_list[self.cursor]

    def unpacker(self, nested_list):
        if type(nested_list) is list:
            list_checker = [1]
        while list_checker.count(1) > 0:
            result = []
            for i in nested_list:
                if type(i) is list:
                    for j in i:
                        result.append(j)
                    nested_list.remove(i)
            for i in result:
                nested_list.append(i)
            list_checker = []
            for i in nested_list:
                if type(i) is list:
                    list_checker.append(1)
                else:
                    list_checker.append(0)
        return nested_list


print(f'Вывод запроса: for item in FlatIterator(nested_list):')
for item in FlatIterator(nested_list):
    print(item)

print(f'\nВывод запроса: flat_list = [item for item in FlatIterator(nested_list)]')
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
