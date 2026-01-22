mylist=[1,2,1,2,3,4,5,6,6,6,7,8,9,7,8,7]

count=0
outvalue=int(input())


for i in mylist:
    if i==outvalue:
        count=count +1
print("{} has occurred {} times".format(outvalue,count))