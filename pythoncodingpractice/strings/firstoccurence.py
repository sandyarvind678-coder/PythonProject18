# s = "iamgoing"
# seen = ""
#
# for ch in s:
#     if ch in seen:
#         print("First repeating character:", ch)
#         break
#     seen += ch


#second occurrence or any occurrence
# s = "i ami going"
# seen = ""
# repeats = []
#
# for ch in s:
#     if ch in seen and ch not in repeats:
#         repeats.append(ch)
#     seen += ch
#
# print("Second repeating character:", repeats[0])


#nth occurrence
inp=["data","varaiable","data","file"]
delvalue=input()
noccur=int(input())
count=0

for i in range(0,len(inp)):
    if inp[i]==delvalue:
        count=count +1


        if count==noccur:
            inp.pop(i)
            break
print(inp)
