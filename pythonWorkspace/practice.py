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
