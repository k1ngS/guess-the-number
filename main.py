#Number Guessing Game Objectives:
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_random = random.randrange(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

chances = {"easy": 10,"hard": 5}

game_over = False
while not game_over:
  print(f"You have {chances[difficulty]} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))

  chances[difficulty] -= 1

  if guess > number_random:
    print("Too hight.")
  elif guess < number_random:
    print("Too low.") 
  else:
    print(f"You got it! The answer was {number_random}")
    game_over = True

  if 0 in chances.values():
    print("You've run out of guesses, you lose.")
    game_over = True
