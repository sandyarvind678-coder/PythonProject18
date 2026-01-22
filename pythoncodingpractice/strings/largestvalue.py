user=list(map(int, input().split(",")))

largestvalue=user[0]
smallestvalue=user[0]


for ch in user:
    if ch>largestvalue:
        largestvalue=ch
print(largestvalue)

for ch in user:
    if ch<smallestvalue:
        smallestvalue=ch

print(smallestvalue)