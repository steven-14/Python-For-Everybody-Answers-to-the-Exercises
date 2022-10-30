# 8 List arguments. 

# Exercise 1: Write a function called chop 
# that takes a list and modifies it,
# removing the first and last elements, 
# and returns None. 

# part 1

my_list = [1, 2, 3, 4]
def chop(lst):
 
    del lst[0]                          # Removes the first element
    del lst[-1]                         # Removes the last element
chop_list = chop(my_list)
print(my_list)                          # Should be [2,3]
print(chop_list) 

# part 2

my_list2 = [1, 2, 3, 4]
def middle(lst):
    new = lst[1:]                       # Stores all but the first element
    del new[-1]                         # Deletes the last element
    return new
middle_list = middle(my_list2)
print(my_list2)                         # Should be unchanged
print(middle_list)                      # Should be [2,3]

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if words[0] != 'From' : continue
    print(words[2])


