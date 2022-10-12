def palindrome(st: str):
    if len(st) == 0:
        return 'please put in valuable str'
    if len(st) == 1:
        return st
    return st[-1] + palindrome(st[:-1])


print(palindrome(''))
