# # 2884 / 알람 맞추기
# time = input()
# hour = int(time.split()[0])
# min  = int(time.split()[1])
# result = [0,0]

# # print(time, hour, min, sep='\n')
# if min >= 45 :
#     result[1] = min - 45

# if min < 45 :
#     hour -= 1
#     if hour < 0 : hour = 23

#     result[1] = 60 + ( min - 45 )

# result[0] = hour

# print(result[0], result[1])

# # 2525 / 알람 맞추기
# time = input()
# time2 = input()

# hour = int( time.split()[0] )
# min  = int( time.split()[1] )

# min += int(time2)

# if min > 59 :
#     hour += ( min // 60 )
#     min -= 60*(min // 60)

# if hour > 23 :
#     hour -= 24

# print(hour, min)

# 2408 / 주사위 세개
# dice = input()
# dice = dice.split()
# num = []
# result = 0

# for i in range(0,3):
#     dice[i] = int( dice[i] )

# for i in range(0,6):
#     num.append( dice.count(i + 1) )

# max_n = max(num)
# n = num.index(max_n) + 1

# # print(num, max_n, n, max(dice))

# if max_n == 3 :
#     result = 10000 + ( 1000 * n )
# if max_n == 2 :
#     result = 1000 + ( 100 * n )
# if max_n == 1 :
#     result = 100 * max( dice )

# print( result )

# # 10950 / A+B - 3
# n = int( input() )
# num = []

# for i in range(0,n):
#     # num.append( input() )
#     cal = input()
#     cal = int(cal.split()[0]) + int(cal.split()[1])
#     num.append( cal )

# for i in range(0,n):
#     print(num[i])

# # 15552 / 빠른 A+B
# import sys
# t = sys.stdin.readline().rstrip('\n')
# for i in range(int(t)):
#     n = sys.stdin.readline().rstrip('\n')
#     n = int( n.split()[0] ) + int( n.split()[1] )
#     print(n)

# # 10871 / X보다 작은 수
# num = input().split()
# n = int( num[0] )
# x = int( num[1] )
# mid_result = []
# a = input().split()

# for i in range(n):
#     a[i] = int( a[i] )
#     if x > a[i] : mid_result.append( a[i] ) 

# result = ''

# for i in range( len(mid_result) ):
#     result = result + ' ' + str( mid_result[i] )

# print( result.lstrip(' ') )

# # 10952 / A+B - 5
# import sys
# ns = sys.stdin.readlines()
# for n in ns:
#     a,b = map(int, n.split())
#     print(a+b)

# 1110 / 더하기 사이클
import sys

n = int( sys.stdin.readline() )
cnt = 0
new = 0
old = n

a = n // 10
b = n % 10

while True:
    if new == old and cnt != 0:
        break
    
    new = b * 10 + (( a + b ) % 10 )
    cnt += 1
    
    a = new // 10
    b = new % 10

print(cnt)