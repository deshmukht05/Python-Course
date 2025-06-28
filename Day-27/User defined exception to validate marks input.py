# User defined exception to validate marks input
# New exception can be defined by deriving new class from the predefined Exception class.

class MarksValidation(Exception):
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return repr(self.data)

marks = int(input("Enter marks obtained: "))

try:
    if(marks>=500):
        raise MarksValidation("Invalid: Must be less than 500.")

except MarksValidation as mv:
    print("Received error: ", mv.data)

else:
    print("Valid marks.")