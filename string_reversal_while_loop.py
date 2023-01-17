def reverse_while_loop(st):
    s1 = ''
    length = len(st) - 1
    while length >= 0:
        s1 = s1 + st[length]
        length = length - 1
    return s1
print(reverse_while_loop('Peter'))