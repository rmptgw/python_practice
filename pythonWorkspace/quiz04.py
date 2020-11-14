# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건
# 1. 편의상 댓글은 20명이 작성아였고 아이디는 1 ~ 20 이라고 자정
# 2. 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 3. random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) # shuffle() 함수 : 리스트 내 값을 무작위로 변경
# print(lst)
# print(sample(lst, 1)) # sample( a, b ) : a에서 b개만큼 샘플 출력

from random import *
applicant = list( range( 1, 21 ) ) # 1부터 21 직전까지( 1이상 21미만 )
shuffle( applicant )
winner = sample( applicant, 4)

print(
    " -- 당첨자 발표 -- ", 
    "치킨 당첨자 : {0}".format(winner[0]), 
    "커피 당첨자 : {0}".format(winner[1:]), 
    " -- 축하합니다 --", 
    sep="\n"
)