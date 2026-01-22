mylist = [1, 2, 3, 4, 5, 8, 6, 7, 9]

largest = float('-inf')
second_largest = float('-inf')

for i in mylist:
    if i > largest:
        second_largest = largest
        largest = i


    elif i > second_largest and i != largest:
        second_largest = i

print(largest)
print(second_largest)