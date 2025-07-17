import random
import time
import json
import os

# 🎣 Rods and Upgrades
rods = {
    "Basic Rod": {"multiplier": 1.0, "cost": 0},
    "Carbon Rod": {"multiplier": 1.2, "cost": 50},
    "Golden Rod": {"multiplier": 1.5, "cost": 100}
}

# 🎣 Fish Types
fish_types = ["Salmon", "Trout", "Bass", "Goldfish", "Old Boot", "Nothing"]
catch_probabilities = [0.2, 0.15, 0.1, 0.05, 0.1, 0.4]

# 🎒 Starting Inventory
def default_inventory():
    return {fish: 0 for fish in fish_types if fish != "Nothing"}

# 💾 Save/Load Functions
def save_game(score, inventory, rod):
    data = {
        "score": score,
        "inventory": inventory,
        "rod": rod
    }
    with open("savegame.json", "w") as f:
        json.dump(data, f)
    print("💾 Game saved!")

def load_game():
    if os.path.exists("savegame.json"):
        with open("savegame.json", "r") as f:
            data = json.load(f)
            print("📂 Save loaded!")
            return data["score"], data["inventory"], data["rod"]
    else:
        print("🆕 Starting new game!")
        return 0, default_inventory(), "Basic Rod"

# 🛍️ Shop
def rod_shop(current_score, current_rod):
    print("\n🪝 Rod Shop:")
    for name, data in rods.items():
        status = " (owned)" if name == current_rod else ""
        print(f"  {name} - {data['cost']} points{status}")
    choice = input("Buy a new rod (type name or press Enter to skip): ").strip()
    if choice in rods and choice != current_rod:
        cost = rods[choice]["cost"]
        if current_score >= cost:
            print(f"✅ You bought the {choice}!")
            return choice, current_score - cost
        else:
            print("❌ Not enough points.")
    return current_rod, current_score

# 📦 Show Inventory
def show_inventory(inventory):
    print("\n🎒 Inventory:")
    for fish, count in inventory.items():
        print(f"  {fish}: {count}")

# 🐟 Main Game Loop
def fishing_game():
    score, inventory, current_rod = load_game()

    print("\n🎣 Welcome to the Ultimate Fishing Game!")
    print("Press Enter to fish, type 'shop' to upgrade rod, 'inv' to view inventory, 'save' to save, 'quit' to exit.\n")

    while True:
        cmd = input("🎯 Action: ").strip().lower()
        if cmd == "quit":
            print(f"🏁 Final Score: {score}")
            break
        elif cmd == "inv":
            show_inventory(inventory)
            continue
        elif cmd == "save":
            save_game(score, inventory, current_rod)
            continue
        elif cmd == "shop":
            current_rod, score = rod_shop(score, current_rod)
            continue

        print("🌊 Casting line... waiting for a bite...", end="", flush=True)
        time.sleep(random.uniform(1.5, 2.5))

        fish = random.choices(fish_types, weights=catch_probabilities, k=1)[0]
        print(f"\n🎣 You caught: {fish}!")

        if fish == "Nothing":
            print("😢 Nothing this time.")
        else:
            inventory[fish] += 1
            if fish == "Old Boot":
                print("🪣 No points for that...")
            else:
                base_points = random.randint(5, 20)
                points = int(base_points * rods[current_rod]["multiplier"])
                score += points
                print(f"✨ {base_points} base points × {rods[current_rod]['multiplier']} ({current_rod}) = {points} points!")
                print(f"💰 Total Score: {score}")

# ▶️ Start Game
if __name__ == "__main__":
    fishing_game()

