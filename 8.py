List1 = [2, 1, 3, 3, 1, 3,1,2,3]
def most_frequent(List1):
    counter = 0
    num = List1[0]
    for i in List1:
        frequent = List1.count(i)
        if (frequent > counter):
            counter = frequent
            num = i

    return num

print(most_frequent(List1))