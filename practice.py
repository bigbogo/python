print(5)
print(-15)
print(1000)
print(2*3)
print("zz"*8)
print(5>1)
print(5>8)
'''
print(not False)
print(not True)
print(not (5<1))'''

from math import *
print(floor(4.9)) #내림
print(ceil(4.9)) #올림
print(sqrt(4.9)) #제곱

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 값

print(randrange(1, 46))

print(randint(1, 5))
sentence3 = """
난 소년
파이썬 쉬움
"""
print(sentence3)

jumin = "990931-1347592"
print("성별:"+jumin[7])
print("연:"+jumin[0:2]) # 0부터 2직전까지

print(""+jumin[:2]) # 처음부터 2직전까지
print("연:"+jumin[:2])

print("나는 %d살" % 20)
print("나는 %s살" % "목")
print("나는 %c살" % "A")
print("나는 %s살 %s색 좋아" % ("A", "금"))
print("나는 {}살 " .format(20))

print("나는 {}살 {}색 좋아" .format(20,1))
print("나는 {0}살 {1}색 좋아" .format(20,1))
print("나는 {1}살 {0}색 좋아" .format(20,1))

gun = 10 

def checkpoint(soldiers): #경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
