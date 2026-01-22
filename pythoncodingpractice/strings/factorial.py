n=int(input())

fact=1

# if n<=0:
#     print("why broooooo?")
# else:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)

while(n>0):
    fact=n*fact

    n=n-1
print(fact)