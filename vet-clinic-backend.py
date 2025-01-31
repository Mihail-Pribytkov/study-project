startText = "Добрый день! Вы находитеся на сайте ветеринарной клиники."
breedText = "Введите, пожалуйста, породу питомца:"
ageText = "Введите возраст питомца:"
nicknameText = "Введите кличку питомца:"

print(startText)

print(breedText)
breedPet = input()

print(ageText)
agePet = input()

print(nicknameText)
nicknamePet = input()

print(f"Это", breedPet, "по кличке", nicknamePet, ". Возраст:" ,agePet, "года") # Не придумал как склонять слово год :(