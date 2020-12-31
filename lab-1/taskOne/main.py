radius = 1.5

xCenter = 3
yCenter = 3

x = float(input("Веедите значение x: "))
y = float(input("Веедите значение y: "))

result = (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius ** 2

if result:
    print("YES")
else:
    print("NO")
