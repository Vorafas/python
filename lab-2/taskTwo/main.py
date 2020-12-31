# Организация сети мини-кофеен в Пермь
# Цель проекта: анализ целесообразности и эффективности реализации
# инвестиционного проекта по созданию в Перми сети мини-кофеен
#
# Первоначальные затраты: 40 млн.
# Период: 1 год
# Поступления: 12 млн.
# Затраты: 6 млн.
# Ставка дисконтирования: 2.5
# Срок реализации проекта: 12 месяцев

from itertools import accumulate

initialCost = 40_000_000
yearIncome = 10_000_000
yearCost = 3_000_000
r = 2.5
n = 12

NPVs = list(
    map(lambda item: (yearIncome - yearCost) / (1 + r) ** item, range(1, n + 1))
)
print(*NPVs)

NPVcumul = accumulate([-initialCost] + NPVs)

print(*NPVcumul)
