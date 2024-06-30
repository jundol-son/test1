class Student:
    def __init__(self, name):
        self.last_name = name[0]
        self.first_name = name[1:]

    def show(self):
        print(f"내 이름은 {self.last_name}{self.first_name}!!")

a = [ Student("어피치"), Student("라이언") ]
print( a[0].last_name, a[0].first_name )

a[1].show()
