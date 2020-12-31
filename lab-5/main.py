# Контрольная точка 5
# Построить модель множественной линейной регрессии цены дома от его параметров.

from numpy.ma import array
from matplotlib import pyplot
from pandas import read_csv, DataFrame
from sklearn.linear_model import LinearRegression as lm
from sklearn.metrics import mean_squared_error

# pandas.options.display.max_rows = 20      # Выводим максимум 20 строк
# pandas.options.display.max_columns = 20   # Выводим максимум 20 столбцов

df = read_csv("houses.csv", sep=",")

# Перемешивание строк для обеспечения независимости наблюдений
df = df.sample(len(df))
df.index = range(len(df))

print(df.corr())

#                  price   sqft_living      grade
# sqft_living   0.702035      1.000000   0.762704
# grade         0.667434      0.762704   1.000000
# price         1.000000      0.702035   0.667434
#
# Наибольшую корреляцию можно увидеть между "price" и "sqft_living" (0,70),
# а также "price" и "grade" (0,67).Прослеживается явная линейная связь между
# "price" и "sqft_living", а также "price" и "grade".

dataFrame = DataFrame()
dataFrame["price"] = df.price
dataFrame["grade"] = df.grade
dataFrame["sqft_living"] = df.sqft_living

# Разделяем выборку на 2 части: обучающую и тестовую, соотношение 7 к 3.
train_ind = dataFrame.index < int(0.7 * len(dataFrame))
test_int = list(not i for i in train_ind)

train = dataFrame[train_ind]  # Обучающая выборка
test = dataFrame[test_int]  # Тестовая выборка

x1_train = train[["sqft_living"]]
x2_train = train[["grade"]]
y_train = train.price

x1_test = test[["sqft_living"]]
x2_test = test[["grade"]]
y_test = test.price

# Обучаем модель на обучающей выборке
model1 = lm().fit(X=x1_train, y=y_train)
model2 = lm().fit(X=x2_train, y=y_train)

# pyplot.scatter(df.grade, df.price)
# pyplot.plot(dataFrame.grade, model2.predict(dataFrame[["grade"]]))
# pyplot.show()  # Выводим график

pyplot.scatter(df.sqft_living, df.price)
pyplot.plot(dataFrame.sqft_living, model1.predict(dataFrame[["sqft_living"]]))
pyplot.show()  # Выводим график

print("y = " + str(model1.intercept_) + " + " + str(model1.coef_[0]) + "x")

# Предскажем цены на тестовой выборке
y_pred = model1.predict(x1_test)

# Оценка качество модели на тестовой выборке
R2 = model1.score(x1_test, y_test)
RMSE = mean_squared_error(y_true=y_test, y_pred=y_pred) ** 0.5
print("R2 =", R2, "RMSE =", RMSE)
# При каждом запуске программы sample по-разному перемешивает наблюдения, и обучающая и тестовая выборки отличаются.
# Следовательно, отличаются и построенные модели: иногда качественные (R2 близок к 1, RMSE поменьше), иногда не очень
# качественные. Вот тут поможет кросс-валидация: переберем разные варианты моделей и усредним значения метрик. Поймем,
# насколько хороши наши модели в среднем.

# Реализация кросс-валидации
k: int
while True:
    try:
        k = int(input("Введите количество блоков: "))
    except ValueError:
        k = 0
    if k > 0 and k * 3 < len(dataFrame):
        break
inds = array(dataFrame.sample(frac=1).index[0:(k * 3)]).reshape(k, 3)
for i in range(inds.shape[0]):  # перебираем индексы построчно
    test_inds = inds[i]  # очередная строка - тестовая выборка (индексы)
    train_inds = list(set(dataFrame.index) - set(test_inds))  # все остальные индексы - обучающая выборка
    print(dataFrame.loc[train_inds])  # обучающая выборка
    print(dataFrame.loc[test_inds])  # тестовая выборка
