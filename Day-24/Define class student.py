# Define class student with attributes name and roll number. Derive class exam with attributes marks and percentage. Then derive class result from exam to calculate and display result.
class student:
    def __init__(self, n, r):
        self.name = n
        self.roll = r

class exam(student):
    def __init__(self, n, r, m1, m2, m3):
        student.__init__(self, n, r)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def cal_result(self):
        self.total = self.m1 + self.m2 + self.m3
        self.per = self.total/300 * 100

class result(exam):
    res = ''
    def __init__(self, n, a, b, c, d):
        exam.__init__(self, n, a, b, c, d)

    def disp_result(self):
        if self.per>=50:
            res = 'PASS'
        else:
            res = 'FAIL'
        print('Student Name: ', self.name)
        print('Roll Number: ', self.roll)
        print('Total Marks: ', self.total)
        print('Percentage: ', self.per)
        print('Result: ', res)
        print()

student1 = result("Vipul", 1, 90, 61, 83)
student1.cal_result()
student1.disp_result()

student2 = result("Raj", 2, 32, 23, 73)
student2.cal_result()
student2.disp_result()