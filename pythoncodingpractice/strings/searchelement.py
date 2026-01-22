mylist = [1, 2, 3, 4, 5, 6]

outvalue = int(input())

for i in mylist:
    if i == outvalue:
        print("value found")
        break
else:
    print("value not found")
