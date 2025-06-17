# To describe class instance relationship
class base:
    pass
class derived(base):
    pass
print(issubclass(derived, base))
print(issubclass(base, derived))

b = base()
d = derived()

print(isinstance(b, base))
print(isinstance(b, derived))
print(isinstance(d, base))
print(isinstance(d, derived))