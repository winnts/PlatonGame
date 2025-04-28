import random
import time

letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
counter = 0

def print_letters():
    global counter
    random_letter = random.choice(letterList)
    start_time = time.time()
    input_letter = input('Press letter: ' + random_letter + ' ')
    end_time = time.time()
    if input_letter == random_letter:
        if end_time - start_time > 1.5:
            print('correct! but too slow! elapsed time: ' + str(end_time - start_time) + ' seconds')
            print('Your record is: ' + str(counter) + '')
            return False
        else:
            print('correct! elapsed time: ' + str(end_time - start_time) + ' seconds')
            counter +=1
        return True
    else:
        print('wrong!')
        print('Your record is: ' + str(counter) + '')
        return False


while print_letters():
    print_letters()