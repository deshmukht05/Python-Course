# Updating dictionary
print("Updating dcitionary")
emp = {"name" : "Tushar"}
city = emp.setdefault('city')
age = emp.setdefault('age', 22)
print("Emp: ", emp)
c = {"city" : "Nagpur"}
emp.update(c)
print("After updation: ", emp)
print()

emp.update(designation = "Python")
emp.update(salary = 50000)
print(emp)

for k, v in emp.items():
    print(k.capitalize(), " : ", v)