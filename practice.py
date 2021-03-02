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

# from random import *
# print( random() ) # random() : 0.0 ~ 1.0의 임의의 값 생성
# print( random() * 10 )
# print( int( random() * 10 ) ) # int() : 정수형으로 표현
# print( int( random() * 10 ) + 1 ) 

# print( randrange(1,46) ) # 1이상 46 미만의 임의값 생성
# print( randint(1,45) ) # 1이상 45이하의 임의값 생성

# python = "Python is Amazing"
# print( python.lower() ) # 소문자로 출력
# print( python.upper() ) # 대문자로 출력
# print( python[0].isupper() )
# print( len(python) )
# print(python.replace("Python", "Java"))

# index = python.index("n") # index() : 원하는 인덱스의 위치를 찾아줌
# print(index)

# index = python.index("n", index + 3)
# print(index)

# print(python.find("Java"))

# print("hi")
# print(python.count("n")) # count() 함수

# # 문자열 포맷
# print("a", "b", sep="")
# print("나는 %d살 입니다." % 20)
# print("나는 %s을 좋아해요." % "python")
# print("Apple은 %c로 시작해요." % "A")
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # 문자열 포맷 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# # 문자열 포맷 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="파란"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="파란", age=20))

# # 문자열 포맷 4 (python v3.6~)
# age = 20
# color = "파란"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# # 탈출문자 '\'
# print("백문이 불여일견 \n 백견이 불여일타") # \n : 줄바꿈
# print("저는 \"나도코딩\" 입니다.") # \를 통해 "를 인식시킴
# print('저는 "나도코딩"입니다.')
# print("c:\\Users\\Nadocoding\\Desktop\\PythonWorkspace") # \\ : \를 문자로 인식시ㅣㅁ
# print("Red Apple\rPine") # \r 커서를 맨 앞으로 이동
# print("Redd\bApple") # \b : back space (한 글자 삭제)
# print("Red\tApple") # \t : tab

# # 리스트 []
# # 순서를 가진 객체의 집합
# # 지하철 칸별로 10명, 20명, 30명

# subway = [10,20,30]
# print(subway)
# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1,"정형돈")
# print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇명 있는지 확인하기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list = [5,2,4,3,1]
# num_list.extend(mix_list)
# print(num_list)

# # 사전 : {}로 표현
# '3:"유재석" = key:value' 의 형태로 생성
# key = id값, value = 내부 값
# 사전을 불러오는 방법 1
# 사전이름 : cabinet
# cabinet[3] : 의 형태로 대괄호 를 통해 가져옴
# 사전을 불러오는 방법 2
# cabinet.get(3) : 의 형태로 get() 함수를 통해 가져옴
# 방법 2의 경우 값이 없어도 오류를 내지 않고 None을 출력하고 
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))

# # 사전 내 값을 확인하는 방법 
# # 1. get() 함수를 활용하는 방법
# # None을 출력하는 경우 "사용가능"으로 대체하여 출력함으로써 사용가능여부를 확인할 수 있음
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능")) 

# # 2. in을 활용하는 방법
# # in을 활용하는 경우 값이 있으면 논리값 True를 출력하며, 값이 없는 경우(사용가능한 경우) False를 출력한다.
# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"조세호"}
# # key update(값이 없는 경우 새로 생성)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 사전 내 자료 삭제
# # del 을 활용하여 삭제 가능
# del cabinet["A-3"]
# print(cabinet)

# # key 전체 출력
# # keys() 함수 활용
# print( cabinet.keys() )

# # value 전체 출력
# # values() 함수 활용
# print( cabinet.values() )

# # key와 value 쌍으로(묶어서 출력)
# # items() 함수 활용
# print( cabinet.items() )

# # 사전 내 전체 자료 지우기
# cabinet.clear()
# print(cabinet)

# # 튜플 () : 소괄호로 표현
# # 리스트와 다르게 변경할 수 없음, 리스트보다 속도가 빠름
# # 변경되지 않는 목록에 사용(고정목록)
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # 튜플의 장점으로 다중 값을 한번에 생성가능
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age, hobby)
# # 를 아래와 같은 형태로 선언가능
# ( name, age, hobby ) = ( "김종국", 20, "코딩" )
# print(name,age, hobby)

# # 세트(set) : 집합
# # 미중복, 순서 없음
# # {}로 표현 / 사전과의 차이는 key와 value를 같이 적는 것이 아니라 value만 작성
# # set() 함수를 통해 작성 가능 / 리스트를 set으로 변경
# my_set = {1,2,3,3,3}
# print(my_set) # 출력값이 중복되지 않음

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 출력( java와 python의 교집합 )
# # 표현방식 : & 기호 사용, intersection() 함수 사용
# print( java & python )
# print( java.intersection(python) )

# # 합집합 출력( java와 python의 합집합 )
# # 표현방식 : | 기호 사용, union() 함수 사용
# print( java | python )
# print( java.union(python) )

# # 차집합 ( java에만 있는 사람, 파이썬에는 없음 )
# # 표현방식 : - 기호 사용, difference() 함수 사용
# print( java - python )
# print( java.difference( python ) )

# # 집합에 값 추가( python에 "김태호" 추가 )
# # add() 함수 사용
# python.add("김태호")
# print(python)

# # 집합 내 값 삭제( java에서 "김태호" 삭제 )
# # remove() 함수 사용
# java.remove("김태호")
# print(java)

# # 자료구조 변경
# # 커피숍
# menu = {"커피", "우유", "주스"} # 집합으로 생성
# print( menu, type(menu) )

# menu = list( menu )
# print( menu, type(menu) )
# menu = tuple( menu )
# print( menu, type(menu) )
# menu = set( menu )
# print( menu, type(menu) )

# # 분기( 조건문 )
# # if() 함수
# # if 조건 :
# #   실행명령문
# wether = "비"
# wether = input("오늘 날씨는 어때요?")
# if wether == "비" or wether == "눈":
#     print("우산을 챙기세요.")
# elif wether == "미세먼지" :
#     print("마스크를 챙기세요.")
# else :
#     print("준비물 필요 없어요.")

# if wether == "비" : print("우산을 채기세요")

# tmp = int( input("기온은 어때요?") )
# if 30 <= tmp : print("너무 더워요. 나가지 마세요.")
# elif 10 <= tmp and tmp < 30 : print("괜찮은 날씨에요.")
# elif 0 <= tmp < 10 : print("외투를 챙기세요.")
# else : print("너무 추워요. 나가지 마세요.")

# # 반복문
# 1.for
# for waiting_no in [0,1,2,3,4] : 
#     print("대기번호 : {0}".format(waiting_no));
# for waiting_no in range(5) : 
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks : 
#     print("{0}손님 주문하신 커피 준비되었습니다.".format(customer))

# 2.while : 조건이 만족할 때까지 반복
# customer = "토르"
# index = 5
# while index >= 1 :
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0 : print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 0
# while True :
#     print("{0}, 커피가 준비되었습니다. 호출 {1}번".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unkown"
# while person != customer : 
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# continue 와 break
# absent = [2,5] # 결석
# no_book = [7] # 책을 안가져옴
# for student in range(1,10) : 
#     if student in absent : continue # 해당 반복 차례를 넘김
#     if student in no_book : 
#         print("오늘 수업은 여기까지. {0}은(는) 교무실로 따라와 ~!!!".format(student))
#         break
#     print("{0}야, 책을읽어봐!!".format(student))

# # 한 줄 for
# # 출석번호 1 2 3 4, 앞에 100을 붙이기로함 -> 101, 102, 103, 104...
# student = [1,2,3,4,5]
# print(student)
# student = [i + 100 for i in student]
# print(student)

# # 학생 이름을 길이로 변환
# student = ["Iron man", "Thor", "I an groot"]
# print(student)
# student = [len(i) for i in student]
# print(student)
# student = ["Iron man", "Thor", "I an groot"]
# student = [i.upper() for i in student]
# print(student)

# # 함수
# def open_account():
#     print('새로운 계좌가 생성되었습니다.')

# def deposit(balance, money): # 입금
#     print('입금이 완료되었습니다. 잔액은 {0} 원 입니다.'.format( balance + money ) )
#     return balance + money

# def withraw( balance, money ): # 출금
#     if balance >= money:
#         print('출금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(balance - money))
#         return balance - money
#     else:
#         print('출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.'.format(balance))
#         return balance
# def withraw_night(balance, money): #저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit( balance, 1000 )
# print( balance )

# balance = withraw(balance, 700)
# print(balance)
# balance = withraw(balance, 700)
# print(balance)
# commission, balance = withraw_night(balance, 100 )
# print('수수료는 {0}원이며, 잔액은 {1}입니다.'.format(commission, balance))

# def profile( name, age, main_lang ):
#     print('이름 : {0} \t나이: {1}\t주 사용 언어: {2}'\
#         .format(name, age, main_lang))

# profile('유재석', 20, '파이썬')

# def profile( name, age=17, main_lang='파이썬' ):
#     print('이름 : {0} \t나이: {1}\t주 사용 언어: {2}'\
#         .format(name, age, main_lang))
# profile('유재석')
# profile('김태호')

# # 키워드 값을 이용한 함수 호출
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name='유재석', main_lang='자바', age=11)

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print('이름: {0}\t나이 : {1}\t'.format(name, age), end= " ")
#     print(lang1, lang2, lang3, lang4, lang5 )


# def profile(name, age, *language):
#     print('이름: {0}\t나이 : {1}\t'.format(name, age), end= " ")
#     for lang in language:
#         print( lang, end= " " )
#     print()

# profile('유재석', 20, "Python", "Java", "C", "C++", "C#" )
# profile('김태호', 23, "Python", "Java", )

# gun = 10
# def checkpoint(soldiers): # 경계근무
#     global gun # 전역변수
#     gun -= soldiers
#     print('[함수 내] 남은 총: {0}'.format(gun))
# def checkpoint_ret(gun, soldiers): # 경계근무
#     gun -= soldiers
#     print('[함수 내] 남은 총: {0}'.format(gun))
#     return gun

# print('전체 총: {0}'.format(gun))
# gun = checkpoint_ret(gun, 2)
# print('남은 총: {0}'.format(gun))

# import sys
# print('Python', 'Java', file=sys.stdout)
# print('Python', 'Java', file=sys.stderr)

# 시험 성적
# score = {'수학':0, '영어':50, '코딩':100}
# for subject, score in score.items():
#     # print( subject, score )
#     print( subject.ljust(8), str(score).rjust(4), sep=" : " )

# answer = input('아무 값이나 입력하세요 : ')
# print('입력하신 값은 ' + answer + '입니다.' )
# answer = 10
# print(type(answer))

# score_file = open('score.txt', 'w', encoding='utf8')
# print('수학 :  0', file=score_file)
# print('영어 : 50', file=score_file)
# score_file.close()

# score_file = open('score.txt', 'a', encoding='utf8')
# score_file.write('과학 : 80\n')
# score_file.write('코딩 :100')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print( score_file.read() )
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end='')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# lines = score_file.readlines()
# for line in lines:
#     print(line, end='')
# score_file.close()

# pickle // dataset을 file 형태로 저장한 것
 
# import pickle
# profile_file = open('profile.pickle', 'wb')
# profile = {'이름':'박명수', '나이':30, '취미':['축구', '골프', '코딩']}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# import pickle
# profile_file = open('profile.pickle', 'rb')
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# # with 명령어 사용시 close를 별도로 해줄 필요가 없음
# import pickle
# with open('profile.pickle', 'rb') as profile_file:
# 	print(pickle.load(profile_file))
# with open('study.txt', 'w', encoding='utf8') as study_file:
# 	study_file.write('파이썬을 열심히 공부하고 있어요.')
# with open('study.txt', 'r', encoding='utf8') as study_file:
# 	print(study_file.read())

# # class : 서로 연관이 있는 변수와 함수의 집합
# # 마린: 공격 유닛, 군인. 총을 쏠 수 있음
# name = '마린' # 유닛 이름
# hp = 40 # 유닛 체력
# damage = 5 # 유닛 공격력

# print('{0} 유닛이 생성되었습니다.'.format(name))
# print('체력 {0}, 공격력 {1} \n'.format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = '탱크'
# tank_hp = 150
# tank_damage = 35
# print('{0} 유닛이 생성되었습니다.'.format(tank_name))
# print('체력 {0}, 공격력 {1} \n'.format(tank_hp, tank_damage))

# tank2_name = '탱크'
# tank2_hp = 150
# tank2_damage = 35
# print('{0} 유닛이 생성되었습니다.'.format(tank2_name))
# print('체력 {0}, 공격력 {1} \n'.format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
# 	print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(\
# 		name, location, damage))

# attack(name, '1시', damage)
# attack(tank_name, '1시', tank_damage)
# attack(tank2_name, '1시', tank2_damage)
# # __init__ : 생성자
# # 맴버 변수 : class 내에서 선언된 변수 
# # ex)
# # self.name에서 .name, 
# # self.hp 에서 .hp
# class Unit:
# 	def __init__(self, name, hp, damage):
# 		self.name = name
# 		self.hp = hp
# 		self.damage = damage
# 		print('{0} 유닛이 생성되었습니다.'.format(self.name))
# 		print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

# marine1 = Unit('마린', 40, 5)
# marine2 = Unit('마린', 40, 5)
# tank = Unit('탱크', 150, 35)

# wraith1 = Unit('레이스', 80, 5)
# print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))

# wraith2 = Unit('레이스', 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
# 	print('{0}는 현재 클록킹 상태입니다.'.format(wraith2.name))

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#         .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if( self.hp <= 0 ):
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃 : 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# class Unit: # 일반유닛
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
#             .format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#         .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if( self.hp <= 0 ):
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린/ 파이어뱃/ 탱크 등을 수송
# # 날 수 있는 기능을 가진 클래스
# class Flyable: 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit( AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중유닛, 체력도 굉장히 좋음, 공격력 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # self 없이 사용
#         self.location = location

# # 서플라이 디폿 : 건물, 1개 건물 = 8유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
# def game_over():
#     pass

# game_start()
# game_over()

# from random import *

# class Unit: # 일반유닛
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
    
#     def move(self, location):
#         # print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
#             .format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if( self.hp <= 0 ):
#             print("{0} : 파괴되었습니다.".format(self.name))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#         .format(self.name, location, self.damage))
# # 마린 클래스
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
    
#     # 스팀팩 : 일정 시간동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     seize_developed = False # 시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False
    
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         # 현재 시즈모드가 아닐때 --> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드를 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드 일때 --> 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# # 날 수 있는 기능을 가진 클래스
# class Flyable: 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit( AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         # print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False # 클로킹 모드(해제 상태)
    
#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print('Player : gg') # good game
#     print('[player] 님이 게임에서 퇴장하셨습니다.')

# # 게임 진행
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리( 생성된 모든 유닛 append )
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# # 공격 모든 준비( 마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹 )
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음( 5 ~ 21 )


# # 게임 종료
# game_over()

# try : 
#     print('나누기 전용 계산기입니다.')
#     nums = []
#     nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
#     nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
#     # nums.append(int(nums[0] / nums[1]))int(num1/num2)
#     print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))
# except ValueError :
#     print('에러! 잘못된 값을 입력하였습니다.')
# except ZeroDivisionError as err :
#     print(err)
# except Exception as err :
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self) :
#         return self.msg

# try :
#     print('한 자리 숫자 나누기 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요 : '))
#     num2 = int(input('두 번째 숫자를 입력하세요 : '))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))
#     print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
# except BigNumberError as err:
#     print('에러가 발생하였습니다.. 한 자리 숫자만 입력하세요.')
#     print(err)
# finally:
#     print('계산기를 이용해 주셔서 감사합니다.')

# import theater_module as mv # as 를 통해 별칭을 사용할 수 있다.

# theater_module.price(3) # 3명이서 영화보러 갔을 때
# theater_module.price_morning(4) # 4명이서 조조할인 영화보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화보러 갔을 때

# mv.price(3) # 3명이서 영화보러 갔을 때
# mv.price_morning(4) # 4명이서 조조할인 영화보러 갔을 때
# mv.price_soldier(5) # 5명의 군인이 영화보러 갔을 때

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# # 부분 로드
# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# # 함수 별칭 사용
# from theater_module import price_soldier as price
# price(3)