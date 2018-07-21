#Randomly generates a number and asks the user to guess the number. Reports back if the user's answer is correct, lower, or higher than the number.
# Gives the user the ability to continue the game if desired, once the correct number is guessed
# Reports the number of guesses taken by the user to get the number


import random

end = 0

num_of_guesses = 0

num = random.randint(1, 9)

print(num)

while end != 'exit':

    guess = int(input('Guess a number between 1 and 9: '))

    num_of_guesses += 1

    if num == guess:
        print ('Correct!')
        num = random.randint(1, 9)
        print(num)

    elif num > guess:
        print ('Your guess is lower than the number')

    else:
        print ('Your guess is higher than the number')

    end = str(input('Enter "exit" when you are finished playing or hit "Enter" to continue: '))

print ('You guessed the number ' + str(num_of_guesses) + ' times')
