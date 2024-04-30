# 함수 : input[int,str,[],None] -> output
# 마술상자 : [100 -> 500, 200 -> 1000, 300 -> 1500]
# f(x) => len(x), str(x), int(x), print(x), input(x)
# count("p")

def koreaIt(x):
    return x + "코리아아이티"
a = koreaIt("인천점")
print(a)

def add(x,y):
    return x + y
b = add(1,2)
print(b)

# 어떠한 단어를 넣었을 때, 그 단어가 5글자 이상이면
# 글자가 길어요!, 아니면 글자가 짧아요!

def word(x):
    if len(x) >= 5:
        return "글자가 길어요!"
    else:
        return "글자가 짧아요!"
c = word("kiwi")
print(c)

# 함수 : input -> [로직] -> output

# abc(5,'😊')
# ['😊','😊','😊','😊','😊']

def abc(a,b):
    return [b for x in range(a)]
d = abc(5,"😊")
print(d)

# 🥚🎅🍜🍣🍱
# 🥚 -> 🎅
# 🎅 -> 🍜
# 🍜 -> 🍣
# 🍣 -> 🍱

def change(x):
    if x == '🥚':
        return '🎅'
    elif x == '🎅':
        return '🍜'
    elif x == '🍜':
        return '🍣'
    elif x == '🍣':
        return '🍱'
    else:
        return "에러"

print(change('🍣'))

change = {
    '🥚' : '🎅',
    '🎅' : '🍜',
    '🍜' : '🍣',
    '🍣' : '🍱',
}