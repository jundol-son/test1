# 클래스 : 속성 + 메서드
"""
클래스 만들기
class "클래스이름" :
pass #나중에 구현 하겠다는 뜻

객체 만들기
인스턴스 = 클래스이름()

인스턴스 속성(객체 마다 다른 속성)
클래스 안 : self.속성명
클래스 밖 : 객체명(인스턴스).속성명

클래스 속성(모든 객체가 공유하는 속성)

비공개 속성(클래스 안에서만 접근 가능한 속성)
-> 접근이 어려움, 네임 맹글링을 이용하면 접근가능

인스턴스 메서드 : 인스턴스 속성에 접근할 수 있는 메서드
항상 첫번째 파라미터로 self를 가진다.

클래스 메서드 : 클래스 속성에 접근하기 위해서 사용
-> 클래스를 의미하는 cls를 파라미터로 받는다.

정적 메서드 : 인스턴스를 만들 필요가 없는 메서드
- self를 받지 않는다
- 메서드가 인스턴스 유무와 관계없이 독립적으로 사용될때

매직 메서드 : 클래스안에 정의할 수 있는 스페셜 메서드
- 특별한 상황에 호출된다. #__init__
- __이름__의 형태로 되어있다.

"""

class Unit:
    count=0 #클래스 속성 : 전체유닛 수
    # 인스턴스 속성 : 이름, 체력, 방어막, 공격력
    # -> 객체마다 다른 값을 가지는 속성
    def __init__(self,name,hp,shield,demage): # __init__ : 생성자, 생성자 첫칸은 self
        self.name=name
        self.hp = hp #비공개 속성, 변경이 불가능
        self.shield=shield
        self.demage=demage
        print(f'[{self.name}](이)가 생성되었습니다.')
        Unit.count+=1 #클래스 속성 변화
    #메서드 추가하기
    def __str__(self):
        return f"[{self.name}] 체력: {self.hp} 실드 : {self.shield} 공격력 : {self.demage} "
    #hit 메서드 구현하기(인스턴스 메서드)
    #1. 데미지가 방어막보다 작거나 같으면 방어막만 깎인다.
    #2. 데미지가 방어막보다 크고 체력보다 작으면 체력과 방어막이 깎인다.
    #3. 데미지가 체력보다 크면 체력을 0으로 만든다.
    def hit(self,demage):
        # 방어막 변경
        if self.shield >= demage:
            self.shield -= demage
            demage = 0
        else:
            demage -= self.shield
            self.shield = 0
        
        #체력 변경
        if demage > 0:
            if self.hp > demage:
                self.hp -= demage
            else:
                self.hp = 0
    
    @classmethod #데코레이터
    def print_count(cls):
        print(f"전체 유닛 개수:{cls.count}")


probe=Unit("프로브",20,20,5)
zealot=Unit("질럿",100,60,16)
dragoon=Unit("드라군",100,80,20)

print(probe)
probe.hit(16)
print(probe)
probe.hit(16)
print(probe)

#클래스 메서드 실행
Unit.print_count()