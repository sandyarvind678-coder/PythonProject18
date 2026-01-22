#ar=int(input())

arr=[1,2,3,4,5,6,7]


divisible=0
notdivisible=0
for i in arr:
    if i %2==0:
        divisible=i
        print("input value is divisible by 2:",divisible)
    if i %4==0:
        divisible=i
        print("input value is divisible by 4:",divisible)
    else:
        notdivisible=i
        print("input value is not divisible by 2:",notdivisible)

first_value=arr[0]
second_value=arr[1]
last_value=arr[-1]
last_secondvalue=arr[-2]

print(first_value)
print(second_value)
print(last_value)
print(last_secondvalue)