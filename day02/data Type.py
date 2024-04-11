# 변수 : 저장하는 공간
# 2 + 3 = 5 인간 : 연산 + 기억[뇌]
# 2 + 3 = 5 컴퓨터 : 연산[CPU] + 기억[RAM]
# a = 2 + 3[숫자]
# a = "안녕하세요"[문자]

# 데이터 타입 종류

a1 = 1      # 정수형 타입
a2 = 3.14   # 실수형 타입
a3 = "3.14" # 문자형 타입
a4 = True   # 불리언형 타입
a5 = False  # 불리언형 타입
a6 = None   # None형 타입 [없음]

# 정수형, 실수형 타입
# 사칙연산이 적용됨
b = 2 + 3.14

# 문자형 타입
# 연결 연산
c = "300" + "100"
# 반복 연산
c1 = "300" * 5

# print : 출력 가능
# input : 입력 가능
# type : 타입을 알려주는 기능
print(type(1))
print(type("1"))
print(type(True))
print(type(None))

# type-casting[타입 변환]
# 정수화 : int()
d = int("100")
d1 = int(3.14)

# 실수화 : float()
e = float(3.14)

# 문자화 : str()
f = str(True)

# 불리언화 해주는 기능
bool("") # True or False [0,"",None]