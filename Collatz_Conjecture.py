#start with number greater than 1 

def input_number():
    num = 0
    
    while num < 2:
        num = int(input('Please enter a number greater than 1: '))

        if num >1:
            return num
        else:
            print ('The number must be greater than 1')
            continue


#number of steps to reach 1, if number is even divide by 2, if number is odd multiply by 3 and add 1

def collatz(number):
    results = []

    while 1 not in results:
        if number%2 == 0:
            number = number/2
            results.append(number)
        
        elif number%2 == 1:
            number = (number*3)+1
            results.append(number)
        
    print (f'the number of steps to reach 1 is: {len(results)}')
    print (results)


number = input_number()
collatz(number)

        



    

