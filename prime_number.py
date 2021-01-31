
n = int(input('please enter a number: '))
if n != 0 and n > 1:
    for x in range(2, n):
        if (n%x) == 0:
            print(n,' is not a prime number.')    
            break
    else:
        print(n,' is a prime numnber.')
        
elif n == 1:
    print('plesase enter a number greater than 1.')

else:
    print("number can't be zero or negative.")

    


