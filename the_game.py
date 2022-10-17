import random

list_of_numbers = range
real_number = random.randint(0,100)

user_name = input('Hello User would u tell me Your name ?\n')
print(f'Hi {user_name}, good to see you in this game. Try to guess a number between 0 and 100')

while True:
    user_number = input('Number: \n')
    user_number = int(user_number)

    if user_number > real_number:
        print("No, no, no. It's too high. Try again")
    elif user_number < real_number:
        print("No, no, no. It's too low. Try again")
    elif user_number == real_number:
        print('CONGRATULATIONS! U guessed it ! ')
        break
