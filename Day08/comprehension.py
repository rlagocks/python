# comprehension

# [0 ~ 100] 리스트 출력
a = [x for x in range(101)]

# "apple ==> [a,p,p,l,e]
b = [x for x in "apple"]

# 0 ~ 100 짝수만 리스트
c = [x for x in range(11) if x % 2 == 0]

# 0 ~ 100 홀수만 리스트
d = [x for x in range(101) if x % 2 == 1]

# 0 ~ 100 짝수를 제곱인 형태인 리스트
e = [x**2 for x in range(101) if x % 2 == 0]

# 0 ~ 10 홀수에서 10을 더한 리스트
f = [x + 10 for x in range(11) if x % 2 == 1]

fruits = ["apple", "pear", "orange", "banana", "strawberry", "kiwi"]
g = [len(x) for x in fruits if 'i' in x]


# 매핑 comprehension
# 홀수는 10 짝수 20
h = [x + 10 if x % 2 == 1 else x + 20 for x in range(101)]

# 5글자 이하이면 글자의 길이로 나타내고, 아니면 대문자화 하기
fruits = ["apple", "pear", "orange", "banana", "strawberry", "kiwi"]
i = [len(x) if len(x) <= 5 else x.upper() for x in fruits]
print(i)
