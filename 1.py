list1 = [2,4,22,44,17,5]
def second_largest(numbers):
    if len(numbers)<2:
        return None
    largest = second_largest = float()
    for num in numbers:
        if num > largest:
            second_largest=largest
            largest = num
        elif largest > num >second_largest:
            second_largest = num
    return second_largest
print(second_largest(list1))