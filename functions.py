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


# DEFINE - built

def greet(a):
    print(f"how do you do, {a}")


def greeting(b):
    print("greeting executid")
    return f"Hey {b}"


# CALL - execute
result1 = greet('John')
print(result1)

result2 = greeting("Justin")
print(result2)
