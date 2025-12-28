# let's play cricket
#selection criteria for batsman is required to score 20 runs in one over

batsman_name=input()

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
total_runs=a+b+c+d+e+f
if total_runs>=20:
    print(f"batsman {batsman_name} is eligible for t20,ODI and test match")

elif total_runs>=14:
    print(f"batsman {batsman_name} is eligible for ODI and test match")

elif total_runs >= 10:
    print(f"batsman {batsman_name} is eligible for test match")

else:
    print(f"batsman {batsman_name} is not eligible for any match")







