a = [2,4,32,11,44,6,7]

def sum(list):
    total = 0
    for num in list:
        if num%2==0:
            total += num
    return total
print(sum(a))        