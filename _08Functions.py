# define function

def sum(a,b,c):
    return a+b+c



print(sum(1,2,3))

#equating a function with another
mystery = sum
print(mystery(2,3,4))

#Overloading a method
def sum1(a,b,c=10):
    return a+b+c

print(sum1(5,5))