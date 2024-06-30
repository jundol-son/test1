
"""
상속의 개념
- 클래스들의 공통된 속성과 메서드를 뽑아내서 부모클래스를 만든다.
- 자식 클래스에서 상속받아서 사용한다

상속의 장점
- 코드의 중복을 제거
- 유지보수가 편리해 진다

실습
Item이라는 부모 -> weapon, armor, healing items라는 자식 클래스 설계

item
속성 : 이름, 메서드 : 줍기, 버리기

item(추상클래스) : 상속받는 클래스에서 반드시 구현해야함
속성 :  추상메서드(abstract) : 사용하기

weapon
속성 : 이름, 데미지 , 메서드 : 줍기, 버리기, 공격하기

armor
속성 : 이름, 메서드 : 줍기, 버리기

healing items
속성 : 이름, 회복량 메서드 : 줍기, 버리기, 사용하기

"""
from abc import * #추상클래스 사용을 위해서 abc를 가져와야함


class Item(metaclass=ABCMeta): #추상클래스 사용을 위해 metaclass=ABCMeta 작성
    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")

    def discard(self):
        print(f"[{self.name}]을(를) 버렸습니다.")

    @abstractmethod #추상클래스 사용을 위한 데코레이터
    def use(self):
        pass

class Weapon(Item): #상속할 클래스 이름을 괄호에 넣어줌


    def __init__(self,name,demage):
        super().__init__(name) #super : 부모클래스의 생성자를 호출
        self.demage = demage
#use method를 작성하지 않으면 오류가 발생함
    def use(self):
        print(f'[{self.name}]을(를) 이용해 {self.demage}로 공격합니다.')



class HealingItem(Item): #상속할 클래스 이름을 괄호에 넣어줌

    def __init__(self,name,recovery_amount):
        super().__init__(name) #super : 부모클래스의 생성자를 호출
        self.recovery_amount = recovery_amount

    def use(self):
        print(f'[{self.name}]을(를) 사용합니다. {self.recovery_amount} 회복')

m16 = Weapon("m16",110)   
bungdae = HealingItem("붕대",20)

m16.use()
bungdae.use()
m16.pick()
