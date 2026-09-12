''' FUNCTIONS
1. DEFINE vs CALL
2. Parametr va Argument
3. Keyword vs default arguments
4. Scope

'''

# build in function > print(), type()
print("==========DEFINE vs CALL===========")
# Function - reusable of code !
# Instead of block {} in JAVA , Python uses indentation!


# DEFINE - built  parametr

def greet(a):
    print(f"how do you do, {a}")


def greeting(b):
    print("greeting executid")
    return f"Hey {b}"


# CALL - execute  argument
result1 = greet('John')
print(result1)

result2 = greeting("Justin")
print(result2)


print("====== Keyword & default arguments ========")

# Define


def give_greet(name, age=28):
    print("give_greet is executed")
    return f"Hi my name is {name} I am {age} years old!"


result3 = give_greet(name="JOHN", age=22)
print(result3)

result4 = give_greet("Justin")
print(result4)
