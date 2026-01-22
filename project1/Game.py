import random

computer = random.choice([-1, 0 , 1])
yorstr = input("Enter your choice : ")

youdict = {"s":-1, "w":1, "g":0}
reversdict = {-1:"snake", 0:"gun", 1:"water"}

you = youdict[yorstr]
print("you ",you)

print(f"You select {reversdict[you]} and Computer select {reversdict[computer]}")

if(computer == you):
    print("It is draw")
else:
    if(computer == -1 and you == 1):
        print("You lose")
    elif(computer == 1 and you == -1):
        print("You win!!")
    elif(computer == 1 and you == 0):
        print("You lose!!")
    elif(computer == 0 and you == 1):
        print("You win!!")
    elif(computer == 0 and you == -1):
        print("You lose!!")
    elif(computer == -1 and you == 0):
        print("You win!!")
    else:
        print("Something went worng")