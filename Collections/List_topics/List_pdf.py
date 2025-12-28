# https://www.pavanonlinetrainings.com https://www.youtube.com/@sdetpavan
# Python Collections
# List
# List
# • A list is a collection which is:
# o Ordered (items have a defined order and can be accessed using indexes).
# o Changeable (Mutable) (we can add, update, or remove items).
# o Duplicate values are allowed in the list.
# • Lists are written inside square brackets [ ].
# Creating a List
# mylist1 = [10, 20, 30, 40, 50]
# mylist2 = ["apple", "banana", "cherry"]
# mylist3 = ["apple", 10, "banana", 20] # mixed data types
# mylist4 = list() # empty list
# print(mylist1) # [10, 20, 30, 40, 50]
# print(mylist2) # ['apple', 'banana', 'cherry']
# Accessing List Items
# • Indexing starts from 0.
# • Negative indexing starts from -1 (last element).
# mylist = ["apple", "banana", "cherry"]
# print(mylist[0]) # apple
# print(mylist[-1]) # cherry
# Range of Indexes
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist[2:5]) # ['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1]) # ['orange', 'kiwi', 'melon']
# https://www.pavanonlinetrainings.com https://www.youtube.com/@sdetpavan
# Changing Item Value
# mylist = ["apple", "banana", "cherry"]
# mylist[1] = "orange"
# print(mylist) # ['apple', 'orange', 'cherry']
# Loop Through a List
# mylist = ["apple", "banana", "cherry"]
# for item in mylist:
#  print(item)
# Check if Item Exists
# mylist = ["apple", "banana", "cherry"]
# if "apple" in mylist:
#  print("Yes, apple is present")
# List Functions
# mylist = ["apple", "banana", "cherry"]
# print(len(mylist)) # 3 (length of list)
# print(mylist.count("apple")) # count occurrences
# Sorting & Reversing
# mylist = ["cherry", "mango", "banana", "apple"]
# mylist.sort()
# print(mylist) # ['apple', 'banana', 'cherry', 'mango']
# mylist.sort(reverse=True)
# print(mylist) # ['mango', 'cherry', 'banana', 'apple']
# mylist.reverse()
# print(mylist) # ['apple', 'banana', 'cherry', 'mango']
# Note: You cannot sort heterogenous data.
# https://www.pavanonlinetrainings.com https://www.youtube.com/@sdetpavan
# mylist=["a", 1, "x"]
# mylist.sort() #TypeError
# print(mylist)
# Adding Items
# mylist = ["apple", "banana"]
# mylist.append("cherry") # add at end
# mylist.insert(1, "orange") # insert at specific position
# print(mylist) # ['apple', 'orange', 'banana', 'cherry']
# Removing Items
# mylist = ["apple", "banana", "cherry"]
# mylist.remove("banana") # remove by value
# mylist.pop(0) # remove by index
# del mylist[1] # delete specific item
# mylist.clear() # clears all items
# Copying a List
# mylist1 = ["apple", "banana"]
# mylist2 = mylist1.copy()
# print(mylist2) # ['apple', 'banana']
# Joining Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# # Approach 1: +
# print(list1 + list2) # ['a', 'b', 'c', 1, 2, 3]
# # Approach 2: extend()
# list1.extend(list2)
# print(list1) # ['a', 'b', 'c', 1, 2, 3]
# Key Point: Lists are mutable → you can modify them anytime.