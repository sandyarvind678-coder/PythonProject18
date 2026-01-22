n=int(input("input value:"))


if n<=1:
    print("enter valid number")
else:
    for i in range(2,n):
        if n%i==0:
            print("It's not a prime number")
            break
    else:
        print("It's a prime number")