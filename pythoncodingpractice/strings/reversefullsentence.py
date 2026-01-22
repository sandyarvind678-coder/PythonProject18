# user=input()
# #reverse=" ".join(user.split()[::-1])
# #print(reverse)
#
# s=user.split()
#
# reverse=" "
#
#
# for i in range(len(s)):
#     reverse=s[i] +" "+ reverse
# print(reverse)

# sentence = "i am going to temple"
#
# words = sentence.split()
# words.reverse()
# result = " ".join(words)
#
# print(result)




inp=input()

sp= inp.split()


a=sp[3:] + sp[:3]
print(a)

output=" ".join(a)

print(output)


