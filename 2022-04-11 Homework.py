# 권동한_LAB3-2

weekend = ['토', '일']

w = input('무슨 요일? ')

if w in weekend:
    print("주말")
else:
    print("평일")

# 권동한_HW1

x = float(input("x값을 입력하세요 : "))

if x <= 0:
    sol = x ** 3 - 9 * x + 2
else:
    sol = 7 * x + 2

print("f(x) = ", sol)

# 권동한_HW2

n1 = int(input("첫 번째 숫자를 입력하세요 : "))
n2 = int(input("두 번째 숫자를 입력하세요 : "))
n3 = int(input("세 번째 숫자를 입력하세요 : "))

min = 0

min = n1

if n2 < min:
    min = n2
if n3 < min:
    min = n3

print("가장 작은 숫자는", min, "입니다.")

# 권동한_HW3

season = int(input("값을 입력하세요 : "))

if season == 1:
    print("봄 입니다.")
elif season == 2:
    print("여름 입니다.")
elif season == 3:
    print("가을 입니다.")
elif season == 4:
    print("겨을 입니다.")
else:
    print("계절")
