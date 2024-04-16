# operator_quiz
# 뉴스 기사 단어 검색 프로그램

news = """1400원 터치한 환율…당국 구두개입에 오름폭 일부 반납(종합)"""

word = input("단어를 입력하세요 : ")
temp ="word" in news
print(f"뉴스 기사 내에 {word} 단어는 {temp}")

# 비밀번호 검증 프로그램

word = input("비밀번호를 입력하세요 : ")
password = "IT" in word and "!" in word
print(f"비밀번호는 {password}")