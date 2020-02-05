
first_name = input('Your first name is...    ')
last_name = input('Your surname is...    ')
house_type = input('What sort of house do you live in?    ')
age = input('Age...    ').strip()
mother_age = input("How old's your mum?    ").strip()
skill_1 = input("Now three skills, firstly...    ")
skill_2 = input('Secondly...    ')
skill_3 = input('And finally...    ')
full_name = first_name.capitalize() + " " + last_name.capitalize()
skill_set = [skill_1, skill_2, skill_3]

print('So let me tell you about yourself...')
print(f"Property information: {full_name}'s {house_type} with well kept lawn")
print('Skills: ', skill_set[0].lower(), skill_set[1].upper(), skill_set[2].capitalize())
print(f"The age difference between you and your mother is {int(mother_age) - int(age)} years.")