
class Student:
    def __init__(self, name):
        self.last_name = name[0]
        self.first_name = name[1:]

    def __repr__(self):
        return f"{self.first_name}"

def create_student(src):
    pass

a = create_student( ["어피치", "라이언"] )
print(a)
