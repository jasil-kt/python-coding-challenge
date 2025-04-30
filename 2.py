list1=[22,33,4,22,33,9,8,7,4]
def remove_duplicates(list):
    result =[]
    for item in list:
        if item not in result:
            result.append(item)
    return result
print(remove_duplicates(list1))