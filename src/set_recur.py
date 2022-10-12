def set4(n: int, arr: set = {4}):
    if n == 0:
        return [4]
    x = list(arr)
    for i in range(len(x)):
        x.append(x[i] - 12)
        x.append(x[i] ** 2)

    return x + set4(n - 1, set(x))


def makeSet(n: int):
    x = set(set4(n))
    y = list(x)
    for i in y:
        if i%4 != 0:
            return 'False'
    return 'True'



if __name__ == '__main__':
    print(makeSet(3))



def set4(n: int, X: set):
    if n == 0: return {4}
    Y = set4(n - 1, X).copy()
    for x in Y:
        X.add(x)
        X.add(x - 12)
        X.add(x ** 2)
    return X
set4(2, set())