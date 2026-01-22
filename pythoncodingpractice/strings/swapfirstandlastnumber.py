mylist=[1,3,4,5,6,7,8]

# size=len(mylist)
#
# temp=mylist[0]
# mylist[0]=mylist[size-1]
# mylist[size-1]=temp
#
# print(mylist)

#approach2

# mylist[-1],mylist[0]=mylist[0],mylist[-1]
# print(mylist)

#approach3

# get=(mylist[-1],mylist[0])
# mylist[0],mylist[-1]=get
# print(mylist)

# change position for any number

inp=[1,2,3,4,5,6,7,8]

pos1,pos2=2,4

inp[pos1],inp[pos2]=inp[pos2],inp[pos1]
print(inp)




