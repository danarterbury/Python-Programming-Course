from random import randrange
def get_user_weapon():
    print("\nSelect your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_selection = int(input("Enter the number of your weapon: "))
    return user_selection
def get_enemy_weapon():
    enemy_selection = randrange(1, 4)
    return enemy_selection
def determine_winner(user_weapon, enemy_weapon):
    weapons = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"\nYou chose: {weapons[user_weapon]}")
    print(f"Enemy chose: {weapons[enemy_weapon]}")
    if user_weapon == enemy_weapon:
        print("It's a tie!")
    elif (user_weapon == 1 and enemy_weapon == 3) or \
         (user_weapon == 2 and enemy_weapon == 1) or \
         (user_weapon == 3 and enemy_weapon == 2):
        print ("You won king!")
    else:
        print("You lost chump!")
def main():
    play_again = "y"
    while play_again.lower() == "y":
        user_weapon = get_user_weapon()
        enemy_weapon = get_enemy_weapon()
        determine_winner(user_weapon, enemy_weapon)
        play_again = input("\nBet you wanna play again, huh? (y/n): ")
    print("\nThanks for playing fam!")

if __name__ == "__main__":
    main()

print ("Completed by Daniel Arterbury AKA Mustache McGee")