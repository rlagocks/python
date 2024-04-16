# 원화 변환기
money = input("원화를 입력하세요 : ")
temp = float(money)/1393
print(f"{money} -> {temp}$")

# 수학 연산 프로그램

num1 = input("두 개의 숫자를 입력하세요 : ")
num2 = input()

plus = int(num1) + int(num2)
minus = int(num1) - int(num2)
mutiple = int(num1) * int(num2)
result = int(num1) / int(num2)
rest = int(num1) % int(num2)
square = int(num1) ** int(num2)

print(f"합 : {plus}")
print(f"차 : {minus}")
print(f"곱 : {mutiple}")
print(f"몫 : {result}")
print(f"나머지 : {rest}")
print(f"제곱 : {square}")

# 원의 둘레와 넓이 계산 프로그램

radius = input("원의 반지름을 입력하세요 : ")
cir = 2 * int(radius) * 3.14
width = 3.14 * (int(radius) ** 2)

print(f"둘레 {cir}")
print(f"넓이 {width}")