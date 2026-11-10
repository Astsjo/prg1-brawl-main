import random
import time
from input_validator_EN import valid_float_input, valid_int_input, valid_int_string_input, valid_alternative_input
import os
from any_key_continue import press_any_key

def fight_menu(name, player_hp, enemy_name, enemy_hp):
    print("#"*30)
    print(f"\n{name}'s HP: {player_hp}")
    print(f"\n{enemy_name}'s HP: {enemy_hp}\n")
    print("#"*30)
    print("\n(1) Fight")
    print("(2) Inventory")
    print("(3) Exit game\n")
    print("#"*30, "\n")
    fight_choice = valid_alternative_input("Choose an alternative [1-3]: ", allowed_inputs=range(1, 4))
    return fight_choice

def main_menu(name, player_hp, player_defence, player_level, xp, upgrade_points, coins):
    print("#"*30)
    print(f"\n{name}'s stats:")
    print(f"HP: {player_hp}")
    print(f"Defence: {player_defence}")
    print(f"Level: {player_level}")
    print(f"\nExperience: {xp}")
    print(f"Available upgrade points: {upgrade_points}")
    print(f"Coins: {coins}\n")
    print("#"*30)
    print("\n(1) Next fight")
    print("(2) Shop")
    print("(3) Upgrade")
    print("(4) Inventory")
    print("(5) Challenge boss")
    print("(6) Exit game\n")
    print("#"*30)
    main_menu_choice = valid_alternative_input("Choose an alternative [1-6]: ", allowed_inputs=range(1, 7))
    return main_menu_choice

def inventory(items, coins):                            # Definerar funktionen och tar in items med dens värden samt mängden mynt
    print(f"Coins: {coins}")                                # Skriver mängden mynt
    available = []                                          # Ny, tom lista
    for item, count in item.items():                        # Sätter item till namnet och count till värdet av den och upprepar för varje item i items
        if count > 0:                                           # Om värdet på en item är större än noll
            available.append(item)                                  # Lägg till item till listan

    if not available:                                       # Om listan är tom
        print("You don't have any items!")                      # Skriv ut att användaren har inga items
        press_any_key()                                         # Vänta tills användaren trycker någonting
        return None                                             # Returnera inget (avslutar funktionen)
    
    for count, name in enumerate(available, start=1):       # Count sätts till numret enumerate tillger och name blir itemname (från listan)
#                                                             startar från 1 och upprepar för varje item i listan
        print(f"({count}) {name}: {items[name]}")               # Skriver ut alternativen (t.ex.: (1) Health Potion: 2)

    allowed = list(range(1, len(available) + 1)) + ["e"]    # Skapar en lista med de tillåtna alternativen att välja mellan
    inventory_choice = valid_alternative_input(
        f"Choose an alternative [1-{len(available)}] or [e] to exit"
        ), allowed                                          # Ber användaren av sitt val bland de tillgängliga alternativen

    if inventory_choice == "e":                             # Om användaren väljer att avsluta
        return None                                             # Returnera inget (avsluta)

    chosen_item = available[inventory_choice - 1]           # Sätter valet till en item i listan
    return chosen_item                                      # Returnar användarens val

def player_damage(player_damage_level, player_luck_level, dice_count, item_bonus, enemy_level_bonus):
    if dice_count == 1:
        damage = random.randint(player_luck_level, 6)
    elif dice_count == 2:
        damage = random.randint(player_luck_level, 12)
    elif dice_count == 3:
        damage = random.randint(player_luck_level, 18)
    damage *= player_damage_level
    damage *= (item_bonus+1)
    damage /= (enemy_level_bonus+1)
    return damage

def enemy_damage(enemy_level_bonus, enemy_max_damage, player_defense):
    damage = random.randint(1, enemy_max_damage)
    damage *= (enemy_level_bonus+1)
    damage /= player_defense
    return damage

def grammar_tutorial():
    print()
    print("#" * 50, "\n")

    print("In yes/no options (shown as [y/n]) one of the options")
    print("is enough. Usually one letter will be capitalized;")
    print("that is the default option if you don't choose one of")
    print("the options.\n")

    print("For choices between preset things, like a list,")
    print("you only need to type the number that goes with that option.\n")

    print("Choices will always be inside square brackets. It can be ")
    print("a range (such as [1-3]), a letter (like [e]), etc\n")

    print("If you give an answer that doesn't work you will be asked to")
    print("choose one of the options. \n")

    print("#" * 50)
    press_any_key()
    print()

def game_tutorial():
    print("\n", "#"*50, "\n")

    print("You'll meet different enemies that you can fight.")
    print("Your goal is to not die and earn as many upgrades/items")
    print("to later go and fight the boss to win the game.\n")

    print("Defeating an enemy will drop coins, experience (xp), and")
    print("potentially an item.\n") 

    print("Earning enough experience will give you an upgrade point")
    print("that you can spend to upgrade a stat.\n")

    print("Between fights you can visit the shop where you can spend")
    print("the coins you earn on items.\n")

    print("Both during and between fights you can open the inventory")
    print("to use items you may have.\n")

    print("#"*50, "\n")
    press_any_key()
    print()

name = input("What's your name: ")
restart = True
first_time = True
enemies = ["Zombie", "Goblin", "Troll", "Ork", "Vampire", "Slime"]
enemy = random.choice(enemies)
# Main game
while restart:
    player_hp = 100
    enemy_hp = 100
    items = {"item1": 0, "item2": 0, "item3": 0}
    player_luck_level = 1
    enemy_max_damage = 6
    enemy_level_bonus = 0
    player_defense = 1
    player_damage_level = 1
    dice_count = 1
    item_bonus = 0

    if first_time:
        print("\nWelcome!")
        tutorial_grammar = input("Would you like a tutorial for the controls? [Y/n]: ").lower().strip()
        if tutorial_grammar != "n":
            grammar_tutorial()
        tutorial_game = input("Would you like a tutorial for how the game will work? [Y/n]: ").lower().strip()
        if tutorial_game != "n":
            game_tutorial()
    first_time = False
    choice = fight_menu(name, player_hp, enemy, enemy_hp)
    if choice == 1:
        player_hp -= enemy_damage()