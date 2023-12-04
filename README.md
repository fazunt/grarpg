# grarpg
import random

player = {
    "name": "",
    "level": 1,
    "health": 100,
    "max_health": 100,
    "damage": 10,
    "experience": 0,
    "gold": 50,
    "weapon": "Miecz Drewniany",
    "armor": "Zwykła Zbroja",
    "dexterity": 5,
    "magic_resistance": 10,
    "strength": 15,
    "potions": 5,
    "diamond_armor": False,
    "completed_quests": [],
    "inventory": []
}

enemies = {
    "Las": [
        {"name": "Goblin", "health": 30, "damage": 5, "reward": {"gold": 20, "experience": 10}},
        {"name": "Szkielet", "health": 50, "damage": 8, "reward": {"gold": 30, "experience": 15}},
    ],
    "Jaskinia": [
        {"name": "Ogr", "health": 80, "damage": 12, "reward": {"gold": 50, "experience": 20}},
        {"name": "Demon", "health": 100, "damage": 15, "reward": {"gold": 70, "experience": 25}},
    ],
    "Wieża Czarownika": [
        {"name": "Czarownik", "health": 120, "damage": 18, "reward": {"gold": 80, "experience": 30}},
        {"name": "Smok", "health": 150, "damage": 20, "reward": {"gold": 100, "experience": 40}},
    ],
    "Boss": [
        {"name": "Boss", "health": 500, "damage": 45, "reward": {"gold": 200, "experience": 100}},
    ]
}

shop = {
    "Miecz Drewniany": {"damage": 10, "price": 20},
    "Miecz Żelazny": {"damage": 20, "price": 50},
    "Topór": {"damage": 30, "price": 80},
    "Łuk": {"damage": 15, "price": 30},
    "Miecz Magiczny": {"damage": 25, "price": 100, "level_requirement": 3},
    "Kusza": {"damage": 18, "price": 60, "level_requirement": 2},
    "Włócznia": {"damage": 30, "price": 120, "level_requirement": 4},
    "Zwykła Zbroja": {"armor": 5, "price": 30},
    "Pancerz Krasnoluda": {"armor": 10, "price": 80, "level_requirement": 3},
    "Diamentowa Zbroja": {"armor": 15, "price": 200, "level_requirement": 5}
}

quests = [
    {"name": "Poszukiwanie Złotego Kamienia", "experience": 20, "gold": 50, "item": "Miecz Magiczny", "level_requirement": 2},
    {"name": "Ochrona Wioski przed Goblinami", "experience": 30, "gold": 70, "item": "Diamentowa Zbroja", "level_requirement": 4},
    {"name": "Zabij Smoka w Wieży Czarownika", "experience": 50, "gold": 100, "item": "Smoczy Miecz", "level_requirement": 6}
]

def battle(location):
    if location == "Boss" and player["level"] < 7:
        print("Nie jesteś wystarczająco silny, aby zmierzyć się z Bossem. Wróć, gdy osiągniesz 7. poziom.")
        return

    enemy_index = random.randint(0, len(enemies[location]) - 1)
    enemy = enemies[location][enemy_index]

    print(f'Walka z {enemy["name"]} (HP: {enemy["health"]}) na {location}')
    while player["health"] > 0 and enemy["health"] > 0:
        print(f'{player["name"]} (HP: {player["health"]}) vs {enemy["name"]} (HP: {enemy["health"]})')
        print("1 - Atakuj")
        print("2 - Użyj mikstury")
        print("3 - Ucieknij")
        action = input("Wybierz akcję: ")
        if action == "1":
            perform_attack(enemy)
        elif action == "2":
            use_potion()
        elif action == "3":
            run_away()
        else:
            print("Nieprawidłowa akcja. Tracisz turę.")
        if enemy["health"] > 0:
            enemy_attack(enemy)
    if player["health"] > 0:
        print(f'Pokonałeś {enemy["name"]}! Zdobywasz {enemy["reward"]["gold"]} złota '
              f'i {enemy["reward"]["experience"]} punktów doświadczenia.')
        player["gold"] += enemy["reward"]["gold"]
        player["experience"] += enemy["reward"]["experience"]
        level_up()
        check_quest_completion()
    else:
        print("Przegrałeś walkę. Koniec gry.")

def perform_attack(enemy):
    critical_strike = random.randint(1, 10) <= player["dexterity"]
    damage = player["damage"] * 2 if critical_strike else player["damage"]
    damage -= enemy.get("armor", 0)
    enemy["health"] -= max(0, damage)
    print(f'Zadałeś {damage} obrażeń! (Krytyk: {critical_strike})')

def enemy_attack(enemy):
    player["health"] -= max(0, enemy["damage"] - player["magic_resistance"])
    print(f'{enemy["name"]} zadał Ci {enemy["damage"]} obrażeń!')

def use_potion():
    if player["potions"] > 0:
        print("Używasz mikstury zdrowia.")
        player["health"] = min(player["health"] + 20, player["max_health"])
        player["potions"] -= 1
        print(f'Twoje zdrowie teraz wynosi {player["health"]}. Pozostało mikstur: {player["potions"]}.')
    else:
        print("Nie masz żadnych mikstur.")

def run_away():
    print("Próbujesz uciec...")
    escape_chance = random.randint(1, 5) <= player["dexterity"]
    if escape_chance:
        print("Udało się uciec z walki!")
    else:
        print("Nie udało się uciec. Przeciwnik kontratakuje!")

def buy_weapon():
    print("Sklep z bronią i zbrojami:")
    for item, stats in shop.items():
        print(f'{item} - Cena: {stats.get("price", "Niedostępne")} złota, '
              f'Obrażenia: {stats.get("damage", "Niedostępne")}, '
              f'Pancerz: {stats.get("armor", "Niedostępne")}, '
              f'Leczenie: {stats.get("healing", "Niedostępne")}, '
              f'Wymagany poziom: {stats.get("level_requirement", 1)}')
    choice = input("Wybierz broń/zbroję do zakupu (lub Q aby wrócić): ")
    if choice == "Q":
        return
    if choice in shop:
        if player["gold"] >= shop[choice].get("price", 0):
            if "level_requirement" in shop[choice] and player["level"] < shop[choice]["level_requirement"]:
                print("Nie masz wystarczającego poziomu do zakupu tej broni/zbroi.")
            else:
                if "damage" in shop[choice]:
                    print(f'Kupiłeś {choice} za {shop[choice]["price"]} złota.')
                    player["damage"] = shop[choice]["damage"]
                    player["weapon"] = choice
                elif "healing" in shop[choice]:
                    print(f'Kupiłeś {choice} za {shop[choice]["price"]} złota.')
                    player["potions"] += 1
                elif "armor" in shop[choice]:
                    print(f'Kupiłeś {choice} za {shop[choice]["price"]} złota.')
                    equip_armor(choice)
                player["gold"] -= shop[choice]["price"]
        else:
            print("Nie masz wystarczająco złota.")
    else:
        print("Nieprawidłowy wybór.")

def equip_armor(armor_type):
    if armor_type == "Diamentowa Zbroja" and not player["diamond_armor"]:
        print(f'Czy na pewno chcesz kupić {armor_type} za {shop[armor_type]["price"]} złota? (Tak/Nie): ')
        confirmation = input()
        if confirmation.lower() == "tak":
            print(f'Kupiłeś {armor_type}.')
            player["armor"] = armor_type
            player["diamond_armor"] = True
            player["inventory"].append(armor_type)
        else:
            print("Anulowano zakup.")
    else:
        print(f'Kupiłeś {armor_type}.')
        player["armor"] = armor_type
        player["inventory"].append(armor_type)

def level_up():
    if player["experience"] >= player["level"] * 30:
        player["level"] += 1
        player["max_health"] += 20
        player["health"] = player["max_health"]
        player["damage"] += 5
        print(f'Awanasujesz na poziom {player["level"]}! Zdrowie zostało zwiększone, '
              f'otrzymujesz nowe obrażenia i pełne uzdrowienie.')

def check_quest_completion():
    for quest in quests:
        if quest["name"] not in player["completed_quests"]:
            if player["level"] >= quest["level_requirement"]:
                print(f'Zadanie dostępne: {quest["name"]}')
                action = input("Czy chcesz podjąć to zadanie? (Tak/Nie): ").lower()
                if action == "tak":
                    print(f'Rozpoczynasz zadanie: {quest["name"]}.')
                    quest_completion(quest)
                else:
                    print("Zadanie odrzucone.")
            else:
                print(f'Zadanie niedostępne: {quest["name"]} (wymagany poziom {quest["level_requirement"]}).')

def quest_completion(quest):
    print(f'Wykonujesz zadanie: {quest["name"]}...')
    print(f'Ukończyłeś zadanie: {quest["name"]}! Otrzymujesz {quest["experience"]} punktów doświadczenia '
          f'i {quest["gold"]} złota.')
    player["experience"] += quest["experience"]
    player["gold"] += quest["gold"]
    if "item" in quest:
        print(f'Otrzymujesz przedmiot: {quest["item"]}.')
        player["inventory"].append(quest["item"])
    player["completed_quests"].append(quest["name"])


while True:
    print("\n### GRA RPG ###")
    if not player["name"]:
        player["name"] = input("Podaj swoją postać: ")

    print(f'{player["name"]} (Poziom: {player["level"]}, Zdrowie: {player["health"]}, '
          f'Obrażenia: {player["damage"]}, Złoto: {player["gold"]}, Broń: {player["weapon"]}, '
          f'Zbroja: {player["armor"]}, Mikstury: {player["potions"]}, '
          f'Diamentowa Zbroja: {"Tak" if player["diamond_armor"] else "Nie"})')

    print("1 - Walcz z przeciwnikiem")
    print("2 - Kup broń/zbroję")
    print("3 - Użyj mikstury")
    print("4 - Sprawdź zlecenia")
    print("5 - Zakończ grę")

    choice = input("Wybierz akcję: ")

    if choice == "1":
        location = input("Wybierz lokalizację walki (Las/Jaskinia/Wieża Czarownika/Boss): ")
        if location not in enemies:
            print("Nieprawidłowa lokalizacja. Spróbuj ponownie.")
            continue
        battle(location)
    elif choice == "2":
        buy_weapon()
    elif choice == "3":
        use_potion()
    elif choice == "4":
        check_quest_completion()
    elif choice == "5":
        print("Dziękujemy za grę. Do widzenia!")
        break
    else:
        print("Nieprawidłowa akcja. Spróbuj ponownie.")
