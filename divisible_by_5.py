
#3 different ways to take input and determine if it is divisible by 5. Last example takes binary input

'''
#Method 1:
def divisible_by_5 (num):

    if num % 5 == 0:
        return(num)
    else:
        return (0)

y = int(input('How many numbers do you want to enter? '))
i = 0
list = []

while y > i:
    x = int(input('Enter numbers to determine if they are divisible by 5: '))
    if (divisible_by_5(x)) > 0:
        list.append(divisible_by_5(x))
    i += 1
print (list)
'''

'''
#Method 2:
list = []
a = int(input('How many numbers do you want to enter? '))
i = 0

while a > i:

    x = [int(input('Enter numbers to determine if they are divisible by 5: '))]
    [list.append(num) for num in x if num % 5 == 0]
    i += 1
print (list)
'''

#Method 3:
list = []

a = int(input('How many numbers do you want to enter? '))
i = 0

while a > i:

    x = input('Enter binary numbers to determine if they are divisible by 5: ')
    x = int(x,2)
    if x % 5 == 0:
        list.append(x)
    i += 1
print (list)