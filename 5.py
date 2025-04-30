a = [2,4,4,7,9,9,5,5,5]
b = {}
for c in a:
    if c in b:
        b[c] += 1
    else:
        b[c] = 1
print(b)