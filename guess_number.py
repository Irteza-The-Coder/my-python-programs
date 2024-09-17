import random
print("it is number guessing game")
print("you have three chances to guess the correct number")

first_guess =  random.randint(1,100)
second_guess = random.randint(1,100)
if first_guess > second_guess:
  first_guess,second_guess = second_guess,first_guess
target_guess = random.randint(first_guess,second_guess)

print("you have two guess the number between",first_guess,"and",second_guess)
chance = 3

while True:
  Get_number = int(input("guess a number"))

  if target_guess == Get_number:

    print("you win")
    break
  else:
    print("try again")
    chance = chance-1
    print("you have",chance,"chances left")
  if chance == 0:
    print("you lose")
    break

  
  
