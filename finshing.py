import random
import time

def show_fish_art(fish_name):
    fish_art = r"""
         ><(((°>
    ____/'>:{}\!#@$%^Y&*()____
         \   %s   /
    """ % fish_name.upper()
    print(fish_art)

def fishing_game():
    fish_types = ["Salmon", "Trout", "Bass", "Goldfish", "Old Boot", "Nothing"]
    catch_probabilities = [0.2, 0.15, 0.1, 0.05, 0.1, 0.4]  # Total = 1.0

    print("🎣 Welcome to the Fishing Game!")
    print("Press Enter to cast your line. Type 'quit' to exit.")

    score = 0
    while True:
        cmd = input("\nCast your line... ")
        if cmd.lower() == "quit":
            print("Thanks for playing! Your total score:", score)
            break

        print("Waiting for a bite...", end="", flush=True)
        time.sleep(random.uniform(1.5, 3.0))

        fish = random.choices(fish_types, weights=catch_probabilities, k=1)[0]
        print("\n🎣 You caught:", fish)

        if fish == "Nothing":
            print("Better luck next time.")
        else:
            show_fish_art(fish)
            if fish == "Old Boot":
                
                print("Ew... just an old boot. No points.")
            else:
                points = random.randint(5, 20)
                print(f"Nice! You earned {points} points.")
                score += points

# Run the game
fishing_game()

