print("=====Iterable objects & RANGE=======")
# Iterable object > string dict tuple list range map filter

range_obj = range(3)
print(range_obj)


text = "MIT"
for letter in text:
    print(f"the letter : {letter}")


for ele in range_obj:
    print(f"the element {ele}")


print("===== DICTIONARY======")
# Dictionary is JSON object!

person = {"name": "Justin", "age": 28, "single": True}
person_obj = dict(name="justin", age=25, single=True)

print(f"the person:{person}")
print(f"the person_obj: {person_obj}")

# method get()
name = person_obj.get("hobby")
hobby = person_obj.get("name")
balance = person_obj.get("balance ", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")


del person_obj["single"]
for key in person_obj:
    print(f"the key : {key} => value {person_obj.get(key)}")


print("======Error handling system =======")

car_dict = dict(name="Toyoto", year=2026, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:
    print("No speed found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
