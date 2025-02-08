# Задание №1

# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

n = int(input("Введите число:"))

count = 0
indexNumber = 1

for _ in range(n):
    num = int(input(f"Введите целое число {indexNumber}: "))
    if num == 0:
        count += 1
    indexNumber += 1

print(f"Количество чисел равных нулю: {count}")