
def collatz(number):    #function creates the collatz sequence, which eventually makes any number 1 when it is repeatedly performed on that number
    if number % 2 == 0:
        a = number // 2
        return (a)
    elif number % 2 != 0:
        b = 3 * number + 1
        return (b)

try:
    c = int(input('Enter a number: '))    #No matter what number you enter, the program will eventually make it '1'
    while c != 1:  # Exit loop once the result = 1
        c = collatz(c)
        print(c)
except:
    print ('You did not enter a number')

