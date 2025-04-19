
pets = {}

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    'Вид питомца': pet_type,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

def get_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'
    
for pet_name, pet_info in pets.items():
    pet_type = pet_info['Вид питомца']
    pet_age = pet_info['Возраст питомца']
    owner_name = pet_info['Имя владельца']
    
    age_suffix = get_age_suffix(pet_age)

info_string = f'Это {pet_type.lower()} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}'
print(info_string)


# startText = "Добрый день! Вы находитеся на сайте ветеринарной клиники."
# breedText = "Введите, пожалуйста, породу питомца:"
# ageText = "Введите возраст питомца:"
# nicknameText = "Введите кличку питомца:"

# print(startText, breedText)

# breedPet = input()

# print(ageText)
# agePet = input()

# print(nicknameText)
# nicknamePet = input()

# print(f"Это", breedPet, "по кличке", nicknamePet, ". Возраст:" ,agePet, "года") # Не придумал как склонять слово год :(