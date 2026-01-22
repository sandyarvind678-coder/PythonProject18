mylist=[8,1,2,3,4,5,6,7,1,1]

mylist.remove(5)
mylist.pop(1)
mylist.append(10)

newlist=mylist.copy()
newlist.insert(1,7)
newlist.extend([12])
print(newlist)
print(mylist)