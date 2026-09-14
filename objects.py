''' OBJECTS

1. what is object
2. Iterable objects & RANGE
3. DICTIONARY
4. Error handling system 


'''
import array  # package / module
import math
from math import ceil, asin

print("=====waht is object=======")
# An  object has state amd method properties
# Everything is obejct in PYTHON!

print(type('hello world'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigma > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritence | Polimorphism
result = math.ceil(97.1)  # CALL
print("result", result)

result1 = ceil(97.1)  # CALL
print("result1", result1)
