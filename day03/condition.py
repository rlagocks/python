# 제어문
# 실행 순서를 조작하는 문법
# 조건문
# if,else,elif

print("프로그램 시작!")

if 5 > 0:
    print("숫자 5는 0보다 크다")

print("프로그램 끝!")

# 숫자 입력을 받고, 해당 숫자가 100이면, 100을 입력 하셨습니다.

print("프로그램 시작!")
num = input("숫자를 입력하세요 : ")
if int(num) == 100:
    print("100을 입력하셨습니다.")
print("프로그램 끝!")

# 숫자 입력을 받고, 해당 숫자가 20~30이면, 20에서 30사이의 숫자를 입력 하셨습니다.

print("프로그램 시작!")
num = input("숫자를 입력하세요 : ")
print(f"{num}을 입력 하셨습니다.")
print("프로그램 끝!")

# 숫자 입력을 받고, 해당 숫자가 짝수이면, 짝수입니다~!

print("프로그램 시작!")
num = input("숫자를 입력하세요 : ")
if int(num)%2 == 0:
    print("짝수입니다~!")
print("프로그램 끝!")

# else

print("프로그램 시작!")
num = input("숫자를 입력하세요 : ")
if int(num) >= 0:
    print("양수입니다")
else:
    print("음수입니다")
print("프로그램 끝!")

# 비밀번호 입력 프로그램
# ! and "IT" 포함되면, 올바르게 비밀번호를 입력하셨습니다!
# ! and "IT" 포함되지 않으면, 올바르게 비밀번호를 입력하지 않았습니다!

password = input("비밀번호를 입력해주세요 : ")
temp = "!" in password and "IT" in password
if temp == True:
    print("올바르게 비밀번호를 입력하셨습니다")
else:
    print("올바르게 비밀번호를 입력하지 않았습니다")

# 홀수짝수 판별 프로그램
# 정수 입력 :
# 홀수입니다! or 짝수입니다!

num = int(input("숫자를 입력해주세요 : "))
if num % 2 == 0:
    print("짝수입니다!")
else:
    print("홀수입니다!")

# 비밀번호 설정
# '!' 포함되지 않고 첫번째 글자가 'a' or 'A'이어야만
# 비밀번호를 올바르게 설정하였습니다.
# 아니면 비밀번호를 올바르게 설정하지 않았습니다.

password = input("비밀번호를 입력해주세요 : ")
temp = not('!' in password)
if  (temp == True) and (password[0] == 'A' or password[0] == 'a'):
    print("비밀번호를 올바르게 설정하였습니다.")
else:
     print("비밀번호를 올바르게 설정하지 않았습니다.")