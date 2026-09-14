''' CLASS
1. What is class
2. Ordinary vs static properties
3. Special methods

'''

print("==== What is class ====")
# class - blueprint for object creation!
# structure > state constructure method


class Person ():
    # state
    messaga = "class state property"

    # constructure
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"the {self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Justin", 36)
person2 = Person("John", 22)

# ordinary state property
print("person1 name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print(" ========Ordinary vs static properties ========== ")
# static state
new_message = Person.messaga
print(new_message)

# static method
Person.explain()
