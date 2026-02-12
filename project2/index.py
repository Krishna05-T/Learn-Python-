import random

ans = random.randint(1, 100)

a =0
guess = 0
while(a != ans):
    a = int(input("Enter the number : "))

    if(a < ans):
        print("Number is too low")
        guess = guess+1
    elif(a > ans):
        print("Number is too high ")
        guess = guess+1
    else:
        print("You win!!")
        print(f"you number in {guess+1} times")