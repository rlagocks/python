# 유저에게
# 첫 번째 정수 입력 : 
# 두 번째 정수 입력 :
# 받은 후 두 수의 합을 출력하는 프로그램
# ex) 첫 번째 정수 입력 : 5
#     두 번째 정수 입력 : 3
#     결과 : 8

num1 = input("첫 번째 정수 입력 : ")
num2 = input("두 번째 정수 입력 : ")

temp = int(num1) + int(num2);

print(f"결과 : {temp}")

# ------------------------------------------

# 나이를 통한 출생년도 알아내기

age = input("나이를 입력해주세요 : ")

temp = 2024 - int(age) + 1

print(f"나이가 {age}살이라면, 출생년도는 {temp}입니다.")

# ------------------------------------------

# 정사각형 넓이 계산 프로그램

length = input("한 변의 길이를 입력해주세요 : ")

temp = int(length) * int(length)

print(f"한 변의 길이가 {length}cm이라면, 넓이는 {temp}cm^2")

# ------------------------------------------

# 시간 변환

time = input("0부터 10000 사이 숫자를 입력해주세요 : ")

temp = int(int(time)/60)
idx = int(time)%60

print(f"{temp}분 {idx}초")