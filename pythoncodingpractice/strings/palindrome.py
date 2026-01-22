user =input("Enter your name")

reverse=""

for i in user:
    reverse=i + reverse

if(reverse==user):
    print("it's a palindrome")

else:
    print("it's not a palindrome")
print(reverse)
