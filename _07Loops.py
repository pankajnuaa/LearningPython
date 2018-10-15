#while loop

x=0
while x<5:
    print(x,end=" ")
    x=x+1
print()

#for loop
for x in range(5): # takes 0 to 5 excluiding 5
    print(x,end=" ")
print()
for x in range(5,10):
    print(x,end=" ")

print()
#For loop from 5 to 10 increase by 3
for x in range(5,10,3):
    print(x,end=" ")
print()

#For each loop
list= [1,2,3,4]
for x in list:
    print(x,end=" ")
print()

#Continue
for x in list:
    if x == 3:
        continue
    print(x,end=" ")
print()

#else for for statement
for x in range(5):
    if x==5:
        break
else:
    print("Entered Else")