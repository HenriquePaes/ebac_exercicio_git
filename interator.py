my_list = [1, 2, 3, 4, 5]
iter_example = iter(my_list)

try:
    while True:
        print(next(iter_example))
except StopIteration as st:
    pass