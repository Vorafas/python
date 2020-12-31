# Ниже описаны четыре класса: "Human", "Programmer", "Departament" и "EmptyDepartamentException".
# Класс "Programmer" наследуется от класса "Human".
# Для класса "Human" определены методы возвращающие имя, возраст и пол.
# Для класса "Programmer" определены операции сложения и сравнения,
# а также методы возвращающие опыт работы и язык программирования.
# Для класса "Departament" определены операции сложения и вычитания,
# методы возвращающие количество программистов и их средний опыт работы,
# а также метод проверяющий вхождение программиста в отдел.
# Программиста можно складывать с программистом, результом является отдел.
# Отдел можно складывать с программистом или с другим отделом. Из отдела
# можно вычитать программсита или другой отдел.
# Класс "EmptyDepartamentException" используется при попытке вычесть объект из пустого отдела.

from copy import deepcopy


class Human:
    def __init__(self, name="Иван", age=0, sex="М"):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSex(self):
        return self.__sex

    def __str__(self):
        return f"Имя: {self.__name}, возраст: {self.__age}, пол: {self.__sex}"


class Programmer(Human):
    def __init__(self, name="Иван", age=0, sex="М", lang="Python", experience=0):
        super().__init__(name, age, sex)
        self.__lang = lang
        self.__experience = experience

    def getLang(self):
        return self.__lang

    def getExperience(self):
        return self.__experience

    def __eq__(self, other):
        if self.getName() == other.getName() and self.getAge() == other.getAge() and \
                self.getSex() == other.getSex() and self.__lang == other.__lang and \
                self.__experience == other.__experience:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Programmer):
            if other == self:
                return Departament(programmers=[other])
            else:
                return Departament(programmers=[self, other])
        elif isinstance(other, Departament):
            if other.isInDepartament(self) > -1:
                return deepcopy(other)
            else:
                return Departament(programmers=[self] + other.getProgrammers())
        elif isinstance(other, Human):
            print("Нельзя собрать отдел из программиста и непрограммиста")
        else:
            print(f"Нельзя добавить к программсту объект класс {type(other)}")

    __radd__ = __add__

    def __str__(self):
        return f"Имя: {self.getName()}, возраст: {self.getAge()}, пол: {self.getSex()}, язык программирования: " \
               f"{self.__lang}, опыт работы: {self.__experience}"


class Departament:
    def __init__(self, name="B2B", programmers=[]):
        self.__name = name
        self.__programmers = programmers

    def getName(self):
        return self.__name

    def getProgrammers(self):
        return self.__programmers

    def getCount(self):
        return len(self.__programmers)

    def isInDepartament(self, programmer):
        for i in range(self.getCount()):
            if programmer == self.__programmers[i]:
                return i
        return -1

    def getAverageExperience(self):
        return sum(map(lambda programmer: programmer.getExperience(), self.__programmers)) / self.getCount()

    def __add__(self, other):
        if isinstance(other, Programmer):
            if self.isInDepartament(other) > -1:
                return deepcopy(self)
            else:
                return Departament(programmers=self.__programmers + [other])
        if isinstance(other, Departament):
            newDepartament = deepcopy(self)
            for programmer in other.__programmers:
                if newDepartament.isInDepartament(programmer) > -1:
                    continue
                else:
                    newDepartament += programmer
            return newDepartament
        else:
            print(f"Нельзя добавить в группу объект класса {type(other)}")

    __radd__ = __add__

    def __sub__(self, other):
        try:
            if self.getCount() < 1:
                raise EmptyDepartamentException(self.__name)
        except EmptyDepartamentException as error:
            print(error)
            return

        if isinstance(other, Programmer):
            if self.isInDepartament(other) > -1:
                newProgrammers = deepcopy(self.__programmers)
                newProgrammers.pop(self.isInDepartament(other))
                return Departament(programmers=newProgrammers)
            else:
                return deepcopy(self)
        elif isinstance(other, Departament):
            newDepartament = deepcopy(self)
            for programmer in other.__programmers:
                newDepartament -= programmer
            return newDepartament
        elif isinstance(other, Human):
            print("Нельзя вычесть из отдела непрограммиста")
        else:
            print(f"Нельзя вычесть из департамнта объект класса {type(other)}")

    def __str__(self):
        if self.getCount() > 0:
            return f"Название отдела: {self.__name}, количество разработчиков: {self.getCount()}, " \
                   f"средний опыт работы: {self.getAverageExperience()} \n" + \
                   "".join(map(lambda programmer, index: f"\t{index + 1}. {programmer}\n", self.__programmers,
                               range(self.getCount())))
        else:
            return "Пустой отдел"


class EmptyDepartamentException(BaseException):
    def __init__(self, name):
        self.message = f"Ошибка: отдел '{name}' пуст"

    def __str__(self):
        return self.message


prog5 = Programmer("Борис", age=36, lang="JavaScript", experience=14)
prog1 = Programmer("Анатолий", age=24, lang="Java", experience=4)
prog4 = Programmer("Александр", age=44, lang="C", experience=19)
prog3 = Programmer("Роман", age=20, lang="C++", experience=1)
prog2 = Programmer("Виктор", age=33, experience=12)

departament = Departament("R&N", [prog1, prog2, prog3])

print(Programmer(age=22, experience=2) + departament + Programmer("Владислава", age=27, experience=7) + (
        prog4 + prog5) - departament)
print(prog4 + prog4 + departament - departament - departament - prog4)

departament - Human()

print(prog4 == prog4)
print(prog4 == prog5)
print(prog3 == prog1)
