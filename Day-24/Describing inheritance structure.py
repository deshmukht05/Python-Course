# Describing inheritance structure
class circle:
    pass
class sphere(circle):
    pass

print(issubclass(sphere, circle))