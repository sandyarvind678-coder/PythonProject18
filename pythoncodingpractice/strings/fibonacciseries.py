n1 = int(input())
n2 = int(input())
sum = 0


for i in range(2,10):
    sum = n1 + n2
    print(sum)
    n1 = n2
    n2 = sum


