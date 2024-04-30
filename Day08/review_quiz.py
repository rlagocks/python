# # 정수 n에 따른 수열 합산 퀴즈
#
# num = int(input("정수 입력 : "))
# result = 0
#
# if num % 2 == 1:
#     for x in range(num+1):
#         if x % 2 == 1:
#             result += x
# else:
#     for x in range(num+1):
#         if x % 2 == 0:
#             result += x ** 2
#
# print(result)


# 배열 변환 기반 조건적 연산 퀴즈
# "정수 배열 arr와 자연수 k가 주어집니다. 이때, k의 홀짝성에 따라 배열에 다른 연산을 적용합니다. 만약k가 홀수라면 배열 arr의 모든 원소에
# k를 곱하고, k가 짝수라면 모든 원소에 k를 더합니다"

arr = {1, 2, 3}
k = int(input("입력 : "))
newList = []

if k % 2 == 1:
    for x in arr:
        newList.append(x * k)

else:
    for x in arr:
        newList.append(x + k)

print(newList)