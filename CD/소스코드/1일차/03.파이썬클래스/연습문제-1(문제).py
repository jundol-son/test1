"""삼성차라는 이름의 클래스를 정의하고 두 개의 객체를 생성합니다.
첫 번째 객체에 차종이라는 속성에 "SM5"을 두 번째 객체의 차종이라는
속성에 "QM6"를 저장하세요. 생성한 각 객체에 “차종”이라는 속성의 값을
화면에 출력하세요."""

class 삼성차:
    pass

a = 삼성차()
a.차종 = "SM5"
b = 삼성차()
b.차종 = "QM6"

print('a와 b의 차종은', a.차종 , b.차종)

class 사람:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        # print("이름 : ", self.name , ', 나이 : ', self.age ,', 성별 : ',self.sex)
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
    def setinfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 적에게 알리지마라")
        

areum = 사람("모름","25","모름")
areum.who()
areum.setinfo("아름","25","여자")
areum.who()
del(areum)