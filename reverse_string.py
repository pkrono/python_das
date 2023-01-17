def reverse_string(st):
    s1 = ''
    for c in st:
        s1 = c + s1
    return s1 
print(reverse_string('Peter'))