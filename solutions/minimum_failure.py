
def minimum(some_list):
    a = some_list[0]
    for x in range(0, len(some_list)):
        if some_list[x] < a:
            a = some_list[x]
    return a

assert minimum([1, 2, 3]) == 1
assert minimum([3, 2, 1]) == 1
assert minimum([-1, -2, 3]) == -2