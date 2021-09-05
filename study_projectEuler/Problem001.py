# 입력되는 숫자들의 배수 
def multiple_sum(limit, n):

    sum = 0
    n_len = len(n)
    numbers = [] # 배수 구하기
    div = [] # n의 값으로 limit를 나눈 값을 저장
    sort_number = [] # 구해진 모든 숫자
    distinct_number = [] # 중복제거된 모든 수

    for i in range(n_len):
        div[i] = int( limit / n[i] ) # 최대 수 구하기

        # 배수 구하기
        for j in range( div[i] ):
            numbers[i][j] = n[i] * j
        
        # 중복제거
        distinct_number += set( numbers[i] )

    # 구해진 모든 수 더하기
    for i in range(distinct_number):
        sum += distinct_number[i]
    
    return print(sum)
