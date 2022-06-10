#클래스

# 마린 : 공격 유닛, 군인. 총을 쓸수 있음.
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

#탱크 : 공격 유닛, 탱크. 포를 쏠수 있는데, 일반 모드 / 시즈모드.
tank_name = "시저탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되어씁니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

##############################################################################
# 클래스

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        #print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("{0} 유닛이 생성 되었습니다.".format(name))
        #print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def move(self, location):
        print("[지상 유닛 이동]") 
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))


#marine1 = Unit("마린", 40, 5)
#marine2 = Unit("마린2", 45, 15)
#tank = Unit("땡크", 140, 5)


#############################################################################

# 멤버변수
# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


############################################################################
# 메소드

# 공격 유닛
class AttackUnit(Unit):   # 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    # 스팀팩 : 일정시간 동안 이동 및 공격속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용 합니다. (HP 10감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동불가
    seize_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        #현재 시즈모드가 아닐때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드를 해제 합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

###########################################################################

# 다중상속
#드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# 날수있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):  # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__("레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 해제 상태)

# 발키리 : 공중 공격 유닛, 한번에 14 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 290, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

#     Unit
#      ↑
#   AttackUnit
#      ↑
#   FlyableAttackUnit  →  Flyable
# 

######################################################################       
# 메소드 오버라이딩

#벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력 높음, 공격력 강함
battlecruiser = FlyableAttackUnit("배틀크루저", 50, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

#     Unit (move())
#      ↑
#   AttackUnit
#      ↑
#   FlyableAttackUnit (move() 재정의)  →  Flyable

###########################################################################
# pass
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location
        #pass 

# 서플라이 디폰 : 건물, 1개 건물 = 8개유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

