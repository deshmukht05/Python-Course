# Override in multi-level inheritance.
class base():
    def sample_method(self):
        print("I am in base.")

class middle(base):
    def sample_method(self):
        print("I am in middle.")
        super(middle, self).sample_method()

class derived(middle):
    def sample_method(self):
        print("I am in derived.")
        super(derived,self).sample_method()

obj = derived()
obj.sample_method()