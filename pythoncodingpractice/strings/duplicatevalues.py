# user=input("enter a string")
# result=""
# for ch in user:
#     if ch not in user:
#         ca=ch + result
#
# print("duplicate removed",ca)

inp = input()

result = ""
dupresult = ""
count = 0

for i in inp:
    if i not in result:
        result = result + i
    else:
        if i not in dupresult:
            dupresult = dupresult + i
            count = count + 1

print(result)
print(dupresult)
print(count)
