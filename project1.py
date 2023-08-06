import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

def play_turn(player_idx):
    current_score = 0
    while True:
        should_roll = input("Player {}, would you like to roll (y/n)? ".format(player_idx + 1))
        if should_roll.lower() == "y":
            value = roll()
            if value == 1:
                print("You rolled a 1, your turn is over.")
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your current score is:", current_score)
        else:
            break
    return current_score

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4.")
    else:
        print("Invalid input, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

for player_idx in range(players):
    print("\nPlayer", player_idx + 1, "turn has started.")
    current_score = play_turn(player_idx)
    player_scores[player_idx] += current_score

    print("\nPlayer", player_idx + 1, "turn has ended.")
    print("Player", player_idx + 1, "score:", player_scores[player_idx])

winning_score = max(player_scores)
winning_idx = player_scores.index(winning_score)
print("\nPlayer number", winning_idx + 1, "is the winner of the game with a score of:", winning_score)
