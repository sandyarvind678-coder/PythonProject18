user = input("Enter a character: ").lower()

vowels = ['a','e','i','o','u']
vowelcount=0
nonvowelcount=0
for ch in user:
    if ch in vowels:
        print("It is a vowel",ch)
        vowelcount=vowelcount+1
        break


    else:
        print("It is not a vowel",ch)
        nonvowelcount=nonvowelcount+1

print(vowelcount)
print(nonvowelcount)