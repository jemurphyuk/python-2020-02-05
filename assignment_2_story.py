
print('Welcome to your Marvel trilogy generator!')
marvel_hero = input('Who is your favourite marvel character?    ')
first_movie = input('What is your favourite Captain America movie?    ')
second_movie = input('What is your favourite Thor movie?    ')
third_movie = input('What is your favourite Avengers movie, starring them all?    ')
hero_gender = input('Are they male, female or prefer not to say?    ')
hero_age = input('How old is your hero?    ')
hero_story = {'beginning': first_movie,
                   'middle': second_movie,
                   'end': third_movie,
                   'hero':
                       {'name': marvel_hero,
                        'age': hero_age,
                        'gender': hero_gender,
                    }
                   }
dictionary_hero = hero_story['hero']['name'].capitalize()
print(dictionary_hero, hero_story['beginning'])
if int(hero_age) > 40:
    print(dictionary_hero, hero_story['middle'], ': The Elder Story')
else:
    print(dictionary_hero, hero_story['middle'], ': An Origin Story')
if hero_gender.lower() == 'male':
    print(dictionary_hero, hero_story['end'], ': Man on a Mission')
elif hero_gender.lower() == 'female':
    print(dictionary_hero, hero_story['end'], ': Woman vs. The World')
else:
    print(dictionary_hero, hero_story['end'], ': Gender Neutral Being vs. Society')
