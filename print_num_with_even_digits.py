
#Program take a range of numbers and prints every number that has all even digits (0 included)

class digit_identifier ():

    def __init__(self, range_of_num):
        self.range_of_num = range_of_num

    def get_even_digits (self, range_of_num):
        all_even_digits = []
        for i in range_of_num:
            s = str(i)
            for a in s:
                if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
                    all_even_digits.append(s)
        print (all_even_digits)

range_of_num = list(range(1000,3000))

call_class = digit_identifier(range_of_num)
call_class.get_even_digits(range_of_num)