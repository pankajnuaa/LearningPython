list1 =[]  # creates list as List interface from java

# Lets add things in our list
list1.append("house")
list1.append("mouse")
list1.append("blouse")

#Lets print list
print(list1)

#lenght of list
print("Length:", len(list1))

#get value at index for list
print("Index 1", list1[1])


#add at index
list1.insert(1, "gourse")
print(list1)

#remove at index
del(list1[1])
print(list1)

del(list1[1:])  # from one and all
print(list1)

#adding other elements for next demo
list1.append("mouse")
list1.append("blouse")

list2 = []
list2.append("house")
list2.append("mouse")
list2.append("blouse")

# add list2 to the end of list
list1.extend(list2)
print(list1)

# also add list
list3 = list1 + list2
print(list3)

list3 = []
list3.append(list1)
list3.append(list2)
print(list3)  #[['house', 'mouse', 'blouse', 'house', 'mouse', 'blouse'], ['house', 'mouse', 'blouse']]


# to access the individual elements of list
print(list3[1][2])

# change the index
list3[0] =22 #[22, ['house', 'mouse', 'blouse']]
print(list3)

print(22 in list3)