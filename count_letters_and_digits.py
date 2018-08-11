#Program takes a console input and counts the number of digits and letters from the sentence

user_input = input('Enter a sentence: ')

d = {'Digits':0, 'Letters':0}

for i in user_input:
    if i.isdigit():
        d['Digits'] += 1
    elif i.isalnum():
        d['Letters'] += 1
    else:
        pass
print ('Letters: ', d['Letters'])
print ('Digits: ', d['Digits'])
