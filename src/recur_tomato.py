def tomato(x):
    arg = list(x)
    if len(arg) == 0:
        return 'please input valuable data'
    if len(arg) == 1:
        return x[0]
    sum = ''
    sum += arg.pop() + tomato(arg)
    return sum


def reverse_kr(st: str):
    if len(st) == 0:
        return st
    else:
        return reverse_kr(st[1:]) + st[0]

print(tomato('1231'))