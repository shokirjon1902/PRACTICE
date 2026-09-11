print("====================NUMBER==================")
# in JAVA, variable is a name of storage location
# in PYTHHON, variable is named reference!

count = 100
count_type = type(count)
print("count ", count, count_type)

print(f"the count : {count}, and type ; {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("=================string=====================")
# METHODS: upper(), lower(), title(), find(), replace()

course = "AI Python Fullstack"
result = course.title()
print(f"the result (1),:{result}")


result3 = type(course)
print(f"the type of course (2): {result3}")

result = course.upper()
print(f"the result (3):{result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result (4):{result}")

print("=================boolean=====================")
