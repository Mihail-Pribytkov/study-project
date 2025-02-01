print("Введите пятизначное число:")

number = input()

digit1 = int(number[0]);
digit2 = int(number[1]);
digit3 = int(number[2]);
digit4 = int(number[3]);
digit5 = int(number[4]);

mathAlgoritm = ((digit4 ** digit5) * digit3) // (digit1 - digit2)
print("Результат:")
print(mathAlgoritm)