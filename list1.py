# # how to take input for list in python
# d = []    # empty list
# for i in input('Enter items').split():
#     d.append(int(i))
# print(d)

# # list comprehension
# a = [x+y for x in range(5) for y in range(10,16)]
# print(a)

# input using list comprehension
# a = [int(x) for x in input('Enter items').split()]
# print(a)

# slicing in list

# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[::-1])

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [10,9,8,7,6,5,4,3,2,1]
list3 = [x+y for x,y in zip(list1,list2)]
print(list3)