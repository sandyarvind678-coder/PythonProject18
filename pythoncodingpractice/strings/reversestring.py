user=input("enter your name")

reverse=""
#reversed=user[::-1]
#print(reversed)

for out in user:
    reverse= out + reverse

print(reverse)