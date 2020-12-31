length = int(input("Введите число чисел в последовательности: "))

result = ""
minElement: int

for i in range(length):
    num = int(input("Введите " + str(i) + "-й элемент: "))
    if i == 0:
        minElement = num

    if minElement > num:
        minElement = num
    result += str(num) + " "

print("Минимальный элемент: " + str(minElement))
print(result)
