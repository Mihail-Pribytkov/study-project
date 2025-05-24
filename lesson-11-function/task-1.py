# Задание №1

# Создайте функцию, которая принимает в качестве параметра - натуральное целое число.
# Данная функция находит факториал полученного числа
# Например, факториал числа 3 это число 6.

# Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_list(n):
    original_factorial = factorial(n)
    result = []
    for num in range(original_factorial, 0, -1):
        result.append(factorial(num))
    return result

n = int(input("Введите натуральное число: "))

if n <= 0:
    print("Ошибка: число должно быть натуральным (n > 0)")
else:
    result_list = factorial_list(n)
    print(f"Факториал числа {n} = {factorial(n)}")
    print(f"Список факториалов от {factorial(n)} до 1:\n{result_list}")