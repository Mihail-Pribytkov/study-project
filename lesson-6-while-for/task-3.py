# Задание №3

# Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные числа на заданном отрезке через пробел.

a, b = map(int, input("Введите целые числа A и B: ").split())

even_numbers = []

for num in range(a, b + 1):
    if num % 2 == 0:
        even_numbers.append(num)
        
output_string = " ".join(map(str, even_numbers))
print(f"Четные числа в диапазоне от {a} до {b} = {output_string}")