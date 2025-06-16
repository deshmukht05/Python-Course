print("Function to print arbitrary number of keywords parameters.")
def func(**k):
    print("*k: ", *k)
    print("Values: ", *k.values())
    print(k)

func(e = "English", m = "Maths", s = "Science")