# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http;//naver.com

# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                 (nav)         (5)           (1)         (!)
# 예) 생성된 비밀번호 : nav51!

# url = "http://naver.com"
url = "http://daum.net"
url = "http://google.com"
url = "http://youtube.com"

# rule 1
sentence1 = url.replace("http://", "")
# rule 2
# index = sentence1.index(".")
sentence2 = sentence1[:int(sentence1.index("."))]
# rule 3
# count = sentence2.count("e")
password = sentence2[:3] + str( len( sentence2 ) ) + str( sentence2.count("e") ) + "!"
# print(
#     sentence2[:3], 
#     str( len(sentence2) ),
#     str(count),
#     "!",
#     sep=""
# )
print("{0}의 비밀번호는 \"{1}\"입니다.".format(url, password))