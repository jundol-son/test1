
class Student:
    def __init__(self, name):
        self.last_name = name[0]
        self.first_name = name[1:]

    def __repr__(self):
        return f"{self.first_name}"

a = [ Student("어피치"), Student("라이언") ]
print(a)
