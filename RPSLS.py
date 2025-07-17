import random

print('===================')
print('Rock Paper Scissors')
print('===================')
print('Lets play a game!')
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")
player = int(input("pick a number: "))
computer = random.randint(1, 5)

winning_rules = {
    1: [3, 4],
    2: [1, 5],
    3: [2, 4],
    4: [5, 2],
    5: [3, 1]
}


def winner(player, computer):
    if player == computer:
        return "Its a tie!"
    elif computer in winning_rules[player]:
        return "The player won!"
    else:
        return "The computer wins!"


choices = {1: "✊", 2: "✋", 3: "✌️", 4: "🦎", 5: "🖖"}
result = winner(player, computer)

print(f"\nYou chose: {choices[player]}")
print(f"CPU chose: {choices[computer]}")
print(f"{result}")
