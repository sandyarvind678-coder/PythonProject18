# Size of first array
n = int(input("Enter size of first array: "))

# Auto-generate first array
arr1 = []
for i in range(1, n + 1):
    arr1.append(i * 10)

# Fetch middle value
middle_value = arr1[len(arr1) // 2]

# Second array contains only the middle value
arr2 = [middle_value]

print("First Array (Auto Generated):", arr1)
print("Second Array Output:", arr2[0])
