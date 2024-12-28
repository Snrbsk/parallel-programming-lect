import string

chars = string.digits + string.ascii_letters

print(chars)

print(len(chars))

a = 0
for i in chars:
    for j in chars:
        a += 1 
        if a % 62 == 1:
            print(i + j)