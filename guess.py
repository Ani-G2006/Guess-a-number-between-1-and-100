import random

def guess_a_number():
    a=int(input("enter any integer between 1 & 100: "))
    number =random.randint(1, 100)
    if a==number:
        print('YES, guess is correct')
    else:
        print('NO, guess is not correct \nEntered number: ' ,end="")
        print(a)
        print("Actual number: ",number)
guess_a_number()

a=1
while a>0:
    choice=int(input("enter 1 for continue, Enter 2 for stop: "))
    match choice:
        case 1:
            guess_a_number()
        case 2:
            print("BYE")
            break
    if choice !=1 or 2:
        print('Invalid Choice')
    a+=1  