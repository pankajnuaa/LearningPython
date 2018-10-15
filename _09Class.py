class Dog:

    #Constructor
    def __init__(self,name, age):
        self._name = name
        self._age = age

#Getter method
    def get_age(self):
        return self._age
    def get_name(self):
        return self._name

#Setter method
    def set_name(self,name):
        self._name= name

    def set_age(self,age):
        self._age = age

    # function that doesn't uses self its more like a static method
    def random():
        return 7

#Tostring method
    def __str__(self):
        return "Dog:\nName:"+self._name+"\nAge: "+ str(self._age)


d1= Dog("Punte",13)
print(d1.get_age())
print(d1)
print(Dog.random())



unwantedText