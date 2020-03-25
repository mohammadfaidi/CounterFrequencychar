'''


from collections import Counter


def count(input):
    WC = Counter(input)
    j = -1
    for i in WC.values():
        j = j + 1
        if i > 1:
            print(WC.keys()[j],)





if _name_ == "_main_":
    input = 'geeksforgeeks'
    count(input)
'''




## initializing string
string = input("enter word:")
## initializing a dictionary
duplicates = {}
for char in string:
   ## checking whether the char is already present in dictionary or not
   if char in duplicates:
      ## increasing count if present
      duplicates[char] += 1
   else:
      ## initializing count to 1 if not present
      duplicates[char] = 1
for key, value in duplicates.items():
   if value > 1:
      print(key, end=" ")