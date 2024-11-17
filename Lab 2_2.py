money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    if money_capital > 0:
        spend += spend * increase
        n = money_capital + salary
        money_capital = n - spend
        count += 1
    elif money_capital < 0:
        break
print("Количество месяцев, которое можно протянуть без долгов:", int(count))
