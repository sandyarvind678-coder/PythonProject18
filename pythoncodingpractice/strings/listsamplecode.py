data=[95,97,33,34,87,85]

highistmark=max(data)
averagemark=sum(data)//len(data)
failedcount=[]


for i in data:
    if i<35:
        failedcount.append(i)
print(highistmark)
print(averagemark)
print(failedcount)