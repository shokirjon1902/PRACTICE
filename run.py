# Dunder __ builtins__, __init__

print("python: everything is object ")

print("message")

result = type("message")
print("result:", result)

''' In Python, there are builtin tools :
1. TYPES > int float str list dict
2. FUNCTIONS > print(), len(), input(), type(), str()
3. CONSTANTS > True False None

 '''

print(dir(__builtins__))
