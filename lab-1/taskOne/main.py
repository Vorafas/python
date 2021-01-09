radius = 1.5

xCenter = 3
yCenter = 3

x: int
while True:
    try:
        x = float(input("Веедите значение x: "))
        break
    except ValueError:
        print("Введено не число.")

y: int
while True:
    try:
        y = float(input("Веедите значение y: "))
        break
    except ValueError:
         print("Введено не число.")

result = (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius ** 2

if result:
    print("YES")
else:
    print("NO")
