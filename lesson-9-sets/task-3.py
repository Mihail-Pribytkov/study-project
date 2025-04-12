# Задание №3

# Во входную строку водится последовательность чисел через пробел.
# Для каждого числа выведите слово ”YES” (в отдельной строке), если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

numbers = list(map(int, input().split()))
seen = set()
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)