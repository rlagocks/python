# 100의 자리 추출기 프로그램!

num = input("10,000부터 99,999 사이의 숫자를 입력하세요 : ")

temp = int(num)
idx = temp // 100
result = idx % 10

print(f"결과 : {result}")