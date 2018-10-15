# From what I understand its a list that cannot be changed

x= 2, 3, 4, 5

# x[0]=5  cannot do that as its fixed

# Still can print it
print(x)  #(2, 3, 4, 5) -> its parenthesis rather than square bracket for tuple

#a tuple can contain tuple
x="1","5","9"
y="00",x
print(y)

print(y[1])
print(y[1][0])

#create tuple with one element
r= 9,
print(r)

#length
print(len(y))

print("00" in y) #-->True

#34:00