a = 7

total = 0
for i in range(1, a):
    if a % i == 0:
        total = total + i

if total == a:
    print("it's a perfect number")
else:
    print("it's not a perfect number")

