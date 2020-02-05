
first_name = input('Your first name is...    ')
last_name = input('Your surname is...    ')
age = input('Age...    ')
house_type = ('What sort of house do you live in?    ')
mother_age = input("How old's your mum?    ")
skill_1 = input("Now three skills, firstly...    ")
skill_2 = input('Secondly...    ')
skill_3 = input('And finally...    ')
full_name = first_name.capitalize() + " " + last_name.capitalize()
skill_set = [skill_1, skill_2, skill_3]

print('So let me tell you about yourself...')
print(f"Property information: {full_name}'s {house_type} with well kept lawn")
print 
