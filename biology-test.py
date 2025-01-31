startText = "Сейчас будут проверочные вопросы на тему \"Этапы развития человека\". Для продолжения нажмите enter"

questions = {
    1: "Какой был первый род Homo?",
    2: "На каком этапе человека началось использование природных предметов в качестве орудий для защиты?",
    3: "Какой род считается самым первым представителем человеческого рода?",
    4: "Какой вид человека был первым прямоходящим?"
}

print(startText)
input()

print(questions[1])
answerQuestion_1 = input()

print(questions[2])
answerQuestion_2 = input()

print(questions[3])
answerQuestion_3 = input()

print(questions[4])
answerQuestion_4 = input()

print(answerQuestion_1,  answerQuestion_2, answerQuestion_3, sep='=>')