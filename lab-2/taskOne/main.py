import pickle
import re
from collections.abc import Iterable

txtFile = 'text.txt'
binFile = 'result.bin'

try:
    file = open(txtFile, "r")
except FileNotFoundError:
    print("Файл ненаден")
else:
    text = file.read()
    if text.strip() == "":
        print("Файл пуст")
    else:
        # 1.1. Количественный анализ текста

        wordCount = len(text.split(" "))
        sentences = re.split(r"(?<=[.!?]) ", text)
        sentenceCount = len(sentences)
        wordsList = list(map(lambda sentence:
                             (sentence, len(sentence.split(" "))), sentences))
        letterDict = dict(map(lambda letter:
                              (letter, len(letter)), text.split(" ")))

        singsDict = {'.': 0, ',': 0, '!': 0, ':': 0, '-': 0, '?': 0, ';': 0}
        numericOfSings = {}
        for item in text:
            if item in singsDict:
                singsDict[item] = singsDict[item] + 1

        for i in singsDict:
            if singsDict[i] > 0:
                numericOfSings[i] = singsDict[i]

        result = {
            'Всего слов': wordCount,
            'Всего предложений': sentenceCount,
            'Предложения': wordsList,
            'Слова': letterDict,
            'Знаки препинания': numericOfSings
        }

        file.close()

        # 1.2. Сохранение полученного объекта в двоичный файл, и загрузка из файла

        with open(binFile, 'wb') as pickleFile:
            pickle.dump(result, pickleFile)

        with open(binFile, 'rb') as pickleFile:
            statisticsDict = pickle.load(pickleFile)


        def printIterableElement(elements: Iterable):
            for elem in elements:
                if isinstance(elem, Iterable):
                    print("AAA", elem)
                    printIterableElement(elem)
                else:
                    print(elem)


        # 1.3. Вывод рассчитанной статистики на экран

        textResult = ""
        for i in statisticsDict:
            textResult += f"{i}: {statisticsDict[i]} \n"
        print(textResult)

        # 1.4. Разбиенине текста на абзацы по n предложений

        quantityParagraphs = input("Введите количество абзацев в предложении: ")
        paragraphs = []
        try:
            if int(quantityParagraphs) <= 0:
                print("Необходимо ввести число больше нуля")
            else:
                txt = ""
                for i in range(len(sentences)):
                    txt += f"{sentences[i]} "
                    if ((i + 1) % int(quantityParagraphs)) == 0:
                        paragraphs.append(txt)
                        txt = ""
                    if i == len(sentences) - 1 and (txt != ""):
                        paragraphs.append(txt)
        except ValueError:
            print("Введенено не число")

        # 1.5. Сортировка абзацев по количеству слов

        sortedParagraphs = sorted(paragraphs, key=lambda par: len(par.split(" ")))

        # 1.6. Сохранение полученного текста в текстовый файл

        newText = ""
        for i in range(len(sortedParagraphs)):
            newText += f"{sortedParagraphs[i]}\n"

        resultTxt = open('result.txt', 'w')
        resultTxt.write(newText)
        resultTxt.close()
