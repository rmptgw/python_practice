# animal = "강아지";
# name = "연탄이";
# age = 4;
# hobby = "산책";
# is_adult = age >= 3;

# print("우리집" + animal + "의 이름은 " + name + "예요.")
# print(name + "는" + str(age) + "살이며, " + hobby + "을 아주 좋아해요." )
# print(name + "는 어른일까요? "+ str(is_adult) )

# print("우리집", animal, "의 이름은 ", name, "예요.")
# print(name + "는", age, "살이며, ", hobby, "을 아주 좋아해요." )
# print(name + "는 어른일까요? ",is_adult )

# # 주석
# ''' 여러 문장 주석입니다. '''

# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2

# print(2**3) # ** = 제곱
# print(10%3) # % = 몫

# print(5//3) # 몫
# print(10//3) # 몫

# print( 10 > 3 ) # T
# print( 4 >= 7 ) # F
# print( 10 < 3 ) # F
# print( 5 <= 5 ) # T

# print( 3 == 3 ) # abs()


# a = 1
# a += 3
# print(a)

# print( abs( -5 ) ) # abs() : 절대값
# print( pow( 4, 2 ) ) # pow(a,b) : a의 b승(제곱) 
# print( max( 5, 12 ) ) # min() : 최소값
# print( min( 5, 12 ) ) # max() : 최대값
# print( round( 3.14 ) ) # 반올림
# print( round( 4.99 ) ) # 반올림

# from math import *
# print( floor( 4.99 ) ) # 내림
# print( ceil( 3.14 ) ) # 올림
# print( sqrt( 16 ) ) # 제곱근

from random import *
# print( random() ) # random() : 0.0 ~ 1.0의 임의의 값 생성
# print( random() * 10 )
# print( int( random() * 10 ) ) # int() : 정수형으로 표현
# print( int( random() * 10 ) + 1 ) 

# print( randrange(1,46) ) # 1이상 46 미만의 임의값 생성
# print( randint(1,45) ) # 1이상 45이하의 임의값 생성

python = "Python is Amazing"
print( python.lower() ) # 소문자로 출력
print( python.upper() ) # 대문자로 출력
print( python[0].isupper() )
print( len(python) )
print(python.replace("Python", "Java"))

index = python.index("n") # index() : 원하는 인덱스의 위치를 찾아줌
print(index)

index = python.index("n", index + 3)
print(index)

print(python.find("Java"))

print("hi")
print(python.count("n")) # count() 함수