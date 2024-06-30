"""
player 클래스 구현
1) 속성 닉네임, 미네랄, 가스, 유닛리스트(Unit 클래스로 부터 만들어진 객체)
is-a 관계 : weapon is-a Item #상속시 발생
has-a 관계 : Player has-a Unit #클래스가 클래스인 객체를 가진 경우

생산하기 메서드
produce(이름, 미네랄, 가스, 체력, 방어막, 공격력)
player의 미네랄과 가스가 충분한 경우
-> 유닛 객체를 생성하고 유닛리스트에 추가한다.
Player의 미네랄이 부족한 경우
-> "미네랄이 부족합니다"를 출력
Player의 가스가 부족한 경우 
-> "가스가 부족합니다"를 출력

"""
unit_info = {
    "probe" : {
        "name" : "프로브",
        "mineral" : 50,
        "gas" : 0,
        "hp" : 20,
        "shield" : 20,
        "demage" : 5
    },
    "zealot" : {
        "name" : "질럿",
        "mineral" : 100,
        "gas" : 0,
        "hp" : 100,
        "shield" : 60,
        "demage" : 16
    },
    "dragoon" : {
        "name" : "드라군",
        "mineral" :125,
        "gas" : 50,
        "hp" : 100,
        "shield" : 80,
        "demage" : 20
    }
}

class Unit:
    """속성 : 이름, 체력, 방어막, 공격력"""
    def __init__(self,name,hp,shield,demage):
        self.name=name
        self.hp=hp
        self.demage=demage
        self.shield=shield


class Player:
    "속성 : 닉네임, 미네랄, 가스, 유닛리스트"
    "메서드 : 유닛 생산하기"
    def __init__(self, nickname, mineral, gas, unit_list=[]):
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list     

    def produce(self, name, mineral, gas, hp, shield, demage):
        if self.mineral - mineral < 0:
            print("미네랄이 부족합니다.")
        elif self.gas - gas < 0:
            print("가스가 부족합니다.")
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name, hp, shield, demage)
            self.unit_list.append(unit)
            print(f"[{name}]을(를) 생산합니다.")

#플레이어 생성
player1 = Player("Bisu",400,50)

#유닛 생성
player1.produce(unit_info['probe']['name'],unit_info['probe']['mineral'],unit_info['probe']['gas'],unit_info['probe']['hp'],unit_info['probe']['shield'],unit_info['probe']['demage'])
player1.produce(unit_info['zealot']['name'],unit_info['zealot']['mineral'],unit_info['zealot']['gas'],unit_info['zealot']['hp'],unit_info['zealot']['shield'],unit_info['zealot']['demage'])
player1.produce(unit_info['dragoon']['name'],unit_info['dragoon']['mineral'],unit_info['dragoon']['gas'],unit_info['dragoon']['hp'],unit_info['dragoon']['shield'],unit_info['dragoon']['demage'])

for unit in player1.unit_list:
    print(f"[{unit.name}] 체력 : {unit.hp} 방어막 : {unit.shield} 공격력 : {unit.demage}")