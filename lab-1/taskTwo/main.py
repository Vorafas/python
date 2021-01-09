def getNumber(text):
    res: int
    while True:
        try:
            res = int(input(text))
            break
        except ValueError:
            print("Введено не число.")
    return res

length = getNumber("Введите число чисел в последовательности: ")

result = ""
minElement: int

for i in range(length):
    num = getNumber("Введите " + str(i) + "-й элемент: ")
    if i == 0:
        minElement = num

    if minElement > num:
        minElement = num
    result += str(num) + " "

print("Минимальный элемент: " + str(minElement))
print(result)