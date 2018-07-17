#Asks the user for a number and determines if the number is prime or not

number_list = []

def get_integer(number = 'Please enter a number: '):
    return int(input(number))

def is_number_prime():

    user_num = get_integer()

    number_list = list(range(2, user_num))

    print (number_list)

    i = 0

    a = 0

    while i < user_num - 2:
        if user_num % number_list[i] == 0:
            a  += 1
            i += 1

        else:
            i += 1

    if a > 0:
        print ('The number is not prime')

    else:
        print ('The number is prime')

    return ()

answer = is_number_prime()