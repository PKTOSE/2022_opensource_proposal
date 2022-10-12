import numpy as np

x = (9, 3, 7, 9, 2, 5, 8)


def iter_variance(arr: tuple):
    length = len(arr)
    m = sum(arr) / length
    _sum = 0
    for i in range(length):
        _sum += (arr[i] - m) ** 2
    return _sum / length


average = 0


def recur_variance(arr: tuple, avg=1):
    if avg == 1:
        global average
        average = sum(arr) / len(arr)
    if len(arr) == 1:
        return (arr[-1] - avg) ** 2
    length = len(arr)
    mid = length // 2
    Y = arr[:mid]
    Z = arr[mid:]
    return (recur_variance(Y, average) * mid + recur_variance(Z, average) * (length - mid)) / length


if __name__ == '__main__':
    y = np.array(x)
    print(f'''
    --------------------iterative-----------------
    x = {x} -> {iter_variance(x)}
    ----------------------Numpy-------------------
    x = {y} -> {np.var(y)}
    --------------------recursive-----------------
    x = {x} -> {recur_variance(x)}
    ''')
    if iter_variance(x) and np.var(y) and recur_variance(x):
        print('success!')
