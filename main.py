import random
import time
from input_validator_EN import valid_float_input, valid_int_input, valid_int_string_input, valid_alternative_input
import sys
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
        , allowed)                                          # Ber användaren av sitt val bland de tillgängliga alternativen

    if inventory_choice == "e":                             # Om användaren väljer att avsluta
        return None                                             # Returnera inget (avsluta)

    chosen_item = available[inventory_choice - 1]           # Sätter valet till en item i listan
    return chosen_item                                      # Returnar användarens val

def roll_shop(store_items):
    available = []
    for name, values in store_items.items():
        if values["chance"] > random.random():
            available.append(name)
    return available

def shop(store_items, available, items, coins):
    while True:
        print("#"*30, "\n")
        if not available:
            print("Nothing is available for sale right now.")
            press_any_key()
            return None, coins

        for number, name in enumerate(available, start=1):
            print(f"({number}) {name}: {store_items[name]['price']}")

        allowed = list(range(1, len(available) + 1)) + ["e"]
        shop_choice = valid_alternative_input(f"\nChoose an alternative [1-{len(available)}] or [e] to exit: ", allowed)
        if shop_choice == "e":
            return None, coins
        if ((coins - (store_items[available[shop_choice-1]]["price"])) >= 0):
            coins -= store_items[available[shop_choice-1]]["price"]
            print(f"You now have 1 more {available[shop_choice-1]}.")
            press_any_key()
            return available[shop_choice-1], coins
        else:
            print("\nYou don't have enough money for that!")

def upgrade_menu(upgrade_points, player_xp, player_stats):
    available = []
    while True:
        if upgrade_points <= 0:
            print("#"*30)
            print(f"\nYou don't have any upgrade points right now.")
            print(f"You have {player_xp}/1000 xp.\n")
            print("#"*30)
            press_any_key()
            return upgrade_points
        else:
            print("#"*30)
            print("\nCurrent stats:")
            print(f"Damage level: {player_stats["Damage_level"]["level"]}")
            print(f"Luck level: {player_stats["luck_level"]["level"]}")
            print(f"Defence level: {player_stats["defence_level"]["level"]}\n")
            for upgrade in player_stats:
                available.append(upgrade)
            for number, upgrade in enumerate(available, start=1):
                print(f"({number}) {upgrade}: {player_stats[upgrade]['level']}\n")
            allowed = list(range(1, len(available) + 1)) + ['e']
            upgrade_choice = valid_alternative_input(f"Choose an alternative [1-{len(available)}] or [e] to exit: ", allowed)
            if upgrade_choice == "e":
                return upgrade_points, player_stats



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

def enemy_damage(enemy_level_bonus, enemy_max_damage, player_defence_level):
    damage = random.randint(1, enemy_max_damage)
    damage *= (enemy_level_bonus+1)
    damage /= player_defence_level
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
    items = {
        "item1": 0,
        "item2": 0,
        "item3": 0
        }
    item_list = [
        "item1",
        "item2",
        "item3"
        ]
    store_items = {
        "item1": {"chance": 1.0, "price": 10},
        "item2": {"chance": 0.5, "price": 20},
        "item3": {"chance": 0.3, "price": 35}
    }
    player_stats = {
        "Luck_level": {"level": 1, "max_level": 4},
        "Defence_level": {"level": 1, "max_level": None},
        "Damage_level": {"level": 1, "max_level": None},
        "Player_level": 1
    }

    enemy_max_damage = 5
    enemy_level_bonus = 0
    dice_count = 1
    item_bonus = 0
    coins = 0
    player_xp = 0
    player_level = 1
    upgrade_points = 0
    rounds = 0

    while player_hp > 0:
        if first_time:
            print("\nWelcome!")
            tutorial_grammar = input("Would you like a tutorial for the controls? [Y/n]: ").lower().strip()
            if tutorial_grammar != "n":
                grammar_tutorial()
            tutorial_game = input("Would you like a tutorial for how the game will work? [Y/n]: ").lower().strip()
            if tutorial_game != "n":
                game_tutorial()
            while player_hp > 0 and enemy_hp > 0:
                choice = fight_menu(name, player_hp, enemy, enemy_hp)
                enemy_alive = True
                if choice == 1:
                    player_hp -= enemy_damage(enemy_level_bonus, enemy_max_damage, player_defence_level)
                    enemy_hp -= player_damage(player_damage_level, player_luck_level, dice_count, item_bonus, enemy_level_bonus)
                elif choice == 2:
                    item_choice = inventory(items, coins)
                elif choice == 3:
                    sys.exit()
            first_time = False
        if enemy_hp < 0 and enemy_alive:
            enemy_alive = False
            rnd_num = random.randint(1, (1+player_luck_level))
            if rnd_num >= 2:
                item_dropped = random.choice(item_list)
            rnd_xp = random.randint(15, (100*player_luck_level))
            rnd_coin_drop = random.randint(10, (20*player_luck_level)) 
            print(f"\nYou defeated {enemy}!")
            print("It dropped: ")
            print(f"{rnd_xp} xp")
            print(f"{rnd_coin_drop} coins")
            if rnd_num == 2:
                print(f"1 {item_dropped}\n")
            player_xp += rnd_xp
            coins += rnd_coin_drop
            if player_xp >= 1000:
                upgrade_points += 1
                player_xp -= 1000
            player_hp += 50
            rounds += 1
            available = roll_shop(store_items)
        elif player_hp < 0:
            print("You died and lost!")
            break
        choice = main_menu(name, player_hp, player_defence_level, player_level, player_xp, upgrade_points, coins)
        if choice == 1:
            enemy_alive = True
            while player_hp > 0 and enemy_hp > 0:
                choice = fight_menu(name, player_hp, enemy, enemy_hp)
                enemy_alive = True
                if choice == 1:
                    player_hp -= enemy_damage(enemy_level_bonus, enemy_max_damage, player_defence_level)
                    enemy_hp -= player_damage(player_damage_level, player_luck_level, dice_count, item_bonus, enemy_level_bonus)
                elif choice == 2:
                    item_choice = inventory(items, coins)
                elif choice == 3:
                    sys.exit()
            if enemy_hp < 0 and enemy_alive:
                enemy_alive = False
                rnd_num = random.randint(1, (1+player_luck_level))
                if rnd_num >= 2:
                    item_dropped = random.choice(item_list)
                rnd_xp = random.randint(15, (100*player_luck_level))
                rnd_coin_drop = random.randint(10, (20*player_luck_level)) 
                print(f"\nYou defeated {enemy}!")
                print("It dropped: ")
                print(f"{rnd_xp} xp")
                print(f"{rnd_coin_drop} coins")
                if rnd_num == 2:
                    print(f"1 {item_dropped}\n")
                player_xp += rnd_xp
                coins += rnd_coin_drop
                if player_xp >= 1000:
                    upgrade_points += 1
                    player_xp -= 1000
                player_hp += 50
                rounds += 1
                available = roll_shop(store_items)
            elif player_hp < 0:
                print("You died and lost!")
                break
        elif choice == 2:
            purchase, coins = shop(store_items, available, items, coins)
            if not name == None:
                items[purchase] += 1
#        elif choice == 3:
#            upgrade_menu()
        elif choice == 4:
            item_choice = inventory(items, coins)
            if item_choice == "item1":
                pass
            elif item_choice == "item2":
                pass
            elif item_choice == "item3":
                pass
#        elif choice == 5:
#            boss_fight_menu()
        elif choice == 6:
            sys.exit()
    break