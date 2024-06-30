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

"""

class Unit:
    count=0 #클래스 속성 : 전체유닛 수
    # 인스턴스 속성 : 이름, 체력, 방어막, 공격력
    # -> 객체마다 다른 값을 가지는 속성
    def __init__(self,name,hp,shield,demage): # __init__ : 생성자, 생성자 첫칸은 self
        self.name=name
        self.__hp = hp #비공개 속성, 변경이 불가능
        self.shield=shield
        self.demage=demage
        print(f'[{self.name}](이)가 생성되었습니다.')
        Unit.count+=1 #클래스 속성 변화
    #메서드 추가하기
    def __str__(self):
        return f"[{self.name}] 체력: {self.__hp} 실드 : {self.shield} 공격력 : {self.demage} "
        


probe=Unit("프로브",20,20,5)
zealot=Unit("질럿",100,60,16)
dragoon=Unit("드라군",100,80,20)

#인스턴스 속성 수정
probe.demage += 1
print(probe)

#비공개 속성 접근
probe.__hp = 9999
print(probe)

# 네임 맹글링(name mangling)
probe._Unit__hp = 9999
print(probe)

# 전체 유닛 개수
print(Unit.count)