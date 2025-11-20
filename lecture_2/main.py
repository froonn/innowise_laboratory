CURRENT_YEAR = 2025

def generate_profile(age):
    if 0 <= age <= 12:
        return 'Child'
    elif 13 <= age <= 19:
        return 'Teenager'
    elif 20 <= age:
        return 'Adult'
    else:
        raise ValueError('age must be greater than or equal to 0')

user_name = input('Enter your full name: ')
birth_year_str = input('Enter your birth year: ')
birth_year = int(birth_year_str)
current_age = CURRENT_YEAR - birth_year
life_stage = generate_profile(current_age)

hobbies = []

while True:
    hobby = input('Enter a favourite hobby or type \'stop\' to finish: ')
    if hobby == 'stop':
        break
    if hobby not in hobbies:
        hobbies.append(hobby)

user_profile = {
    'name': user_name,
    'age': current_age,
    'stage': life_stage,
    'hobbies': hobbies
}

print('Profile summary:')
print(f'Name: {user_name}')
print(f'Age: {current_age}')
print(f'Life Stage: {life_stage}')

if not hobbies:
    print('You didn\'t mention any hobbies.')
else:
    print(f'Favourite Hobbies ({len(hobbies)}):')
    for hobby in hobbies:
        print(f'- {hobby}')