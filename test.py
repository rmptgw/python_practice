# # 알람 맞추기
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

# 알람 맞추기
time = input()

hour = int( time.split()[0] )
time = int( time.split()[1] )
result = [0,0]

