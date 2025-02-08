# Задание №2

# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы "a", "e", "i", "o", "u".
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите Fals

consonants = "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"
vowels = "A", "E", "I", "O", "U", "Y"

vowels_count = 0
consonants_count = 0

input_text = str(input())

for char in input_text.upper(): 
    if char in vowels:
        vowels_count += 1
    elif char in consonants:
        consonants_count += 1

if vowels_count and consonants_count != 0:
    print(f"В тексте '{input_text}' {vowels_count} гласных и {consonants_count} согласных.")
else:
    print("false")