
class Student:
    def __init__(self, name):
        self.last_name = name[0]
        self.first_name = name[1:]


a = [ Student("어피치"), Student("라이언") ]
print(a)
