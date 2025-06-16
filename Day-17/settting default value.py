print("Setting default value.")
# Setting default value when key in dictionary.
amp = {"name" : "Tushar", "age" : 12}
age = amp.setdefault("name")
print(amp)
print()

# When key is not in dictionary
print("When key is not in dictionary")
emp = {"name" : "Tushar"}
city = emp.setdefault('city')
age = emp.setdefault('age', 22)
print(emp)
print("City: ", city)
print("Age: ", age)
print()