def getNumber(text):
    res: int
    while True:
        try:
            res = int(input(text))
            break
        except ValueError:
            print("Введено не число.")
    return res

radius = 1.5

xCenter = 3
yCenter = 3

x = getNumber("Веедите значение x: ")
y = getNumber("Веедите значение y: ")

result = (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius ** 2

if result:
    print("YES")
else:
    print("NO")
