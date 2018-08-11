
#Asks user how many words they want to enter, the user enters the words they want included,
# and then the words are sorted alphabetically and printed out

words = []

num = int(input('How many words do you want to enter? '))

i = 0

while i < num:
    user_input = str(input('Enter the word you want included: '))
    words.append(user_input)
    i += 1

words.sort()
print (words)