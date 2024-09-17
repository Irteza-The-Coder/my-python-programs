
import random
print("it is a rock,paper,scissor game.")
print("you have two chances")
def random_string():
    ROCK= ["rock","paper","scissor"]
    generator = random.choice(ROCK)
    
    return generator

random_choice= random_string()
chances = 2
NUM1 = "try again"
while True:
    user_choice = str(input("choose between rock,paper and scissor: "))
  
        
    if user_choice  not in ["rock","paper","scissor"]:
        print("it is invalid input choose between rock,paper and scissor")
    elif (user_choice == "paper" and random_choice == "rock") or (user_choice=="rock" and random_choice == "scissor") or (user_choice =="scissor" and random_choice == "paper"):
        print("you win")
        print("computer chose:",random_choice)
        break
    elif (user_choice == "rock" and random_choice == "paper") or (user_choice == "scissor" and random_choice == "rock")  or (user_choice == "paper" and random_choice == "scissor"):
        print(NUM1)
        chances = int(chances) - 1
        random_choice = random_string()
        print("chances left",chances)
    elif user_choice == random_choice:
        print("its a tie")
        print("computer chose:",random_choice)
        random_choice = random_string()
    if chances == 0:
        print("you lose")
        NUM1 = ""
        break




    
       
    



