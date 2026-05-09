#collect two inputs
#compare both inputs using the rules from the rock paper scissors game to find #out who wins or if it was a draw

import random

options = ["rock","paper","scissors"]

player_one = random.choice(options)
player_two = random.choice(options)

if (player_one == "rock" and player_two == "scissors") or (player_one == "scissors" and player_two == "paper") or (player_one == "paper" and player_two == "rock"):
    print(f"Player One wins!!!\n{player_one} beats {player_two} always!!")

elif (player_two ==  "rocks" and player_one == "scissors") or (player_two == "scissors" and player_one == "paper") or (player_two == "paper" and player_one == "rock"):
    print(f"Player Two wins!!!\n{player_two} beats {player_one} always!!")

elif (player_one ==  "rock" and player_two == "rock") or (player_one == "paper" and player_two == "paper") or (player_one == "scissors" and player_two == "scissors"):
    print(f" A Tie!\n{player_one} and {player_two} ties always!!")
