list = [4, 3, 4, 5, 8, 6, 7, 1, 2, 0]

secondlargestnumber = list[0]
thirdnumber = list[0]

for i in list:
    if i < secondlargestnumber:
        thirdnumber = secondlargestnumber
        secondlargestnumber = i

    elif i != secondlargestnumber and i < thirdnumber:
        thirdnumber = i
print(secondlargestnumber)
print(thirdnumber)

