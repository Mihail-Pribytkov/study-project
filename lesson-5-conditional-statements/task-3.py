# Задание №3

# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов,
# больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2,
# если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

print("Введите минимальную сумму инветсиций:")
min_sum_investing = int(input())

print("Введите сколько долларов у Ивана")
cash_ivan = int(input())

print("Введите сколько долларов у Майкла")
cash_mikle = int(input())

if (cash_mikle >= min_sum_investing) and (cash_ivan < min_sum_investing):
    print("Mike")
elif (cash_ivan >= min_sum_investing) and (cash_mikle < min_sum_investing):
    print("Ivan")
elif (cash_mikle >= min_sum_investing) and (cash_ivan >= min_sum_investing):
    print("2")
elif (cash_mikle + cash_ivan) >= min_sum_investing:
    print("1")
elif (cash_mikle + cash_ivan) < min_sum_investing:
    print("0")