# Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명을 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
from os import write

for n in range(1,51):
    with open((str(n) + ' 주차.txt'), 'w', encoding='utf8') as report_file :
        # report_file.write(' - ' + str(n) + '주차 주간보고 - \n')
        report_file.write(' - {0} 주차 주간보고 - \n'.format(n))
        report_file.write(' 부서 : SI \n' )
        report_file.write(' 이름 : TG \n' )
        report_file.write(' 업무요약 : ' + str(n) + ' 주차 주간보고\n' )