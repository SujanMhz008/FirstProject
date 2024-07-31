import random
import sys
import time

ike = {
    "Name": "Ike",
    "HP": 100,
    "STR": 10,
    "DEF": 8,
    "EVA": 20,
    "ACC": 70
}

lizardman1 = {
    "Name": "Lizardman 1",
    "HP": 50,
    "STR": 6,
    "DEF": 5,
    "EVA": 10,
    "ACC": 50
}

lizardman2 = {
    "Name": "Lizardman 2",
    "HP": 50,
    "STR": 5,
    "DEF": 6,
    "EVA": 10,
    "ACC": 50
}

head1 = {
    "Name": "Cerberus's Head 1",
    "HP": 100,
    "STR": 6,
    "DEF": 4,
    "EVA": 10,
    "ACC": 60
}

head2 = {
    "Name": "Cerberus's Head 2",
    "HP": 75,
    "STR": 6,
    "DEF": 6,
    "EVA": 10,
    "ACC": 60
}

head3 = {
    "Name": "Cerberus's Head 3",
    "HP": 50,
    "STR": 5,
    "DEF": 3,
    "EVA": 30,
    "ACC": 60
}


def start():
    print("Once upon a time, there lived a boy named Ike with his grandmother in the secluded woods.")
    time.sleep(3)
    print("The boy learned how to live in the woods along with his grandmother who was dying because of old age.")
    time.sleep(3)
    print("The grandmother with her dying breath told Ike to head to the demon castle where her mother lived.")
    time.sleep(3)
    print("Soon after the grandmother's passing, Ike journeyed towards the demon castle to meet his mother.")


def status(character):
    print(f"\nHP: {character['HP']}")
    print(f"STR: {character['STR']}")
    print(f"DEF: {character['DEF']}")
    print(f"EVA: {character['EVA']}")
    print(f"ACC: {character['ACC']}")


def rng():
    checker = random.randint(1, 100)
    return checker


def gameover():
    print("Game Over!")
    print("Do you want to play again? yes or no")
    choice = input()
    if choice.lower().strip() in "y yes".split():
        __main__()
    else:
        sys.exit(0)


def selectlizardmen():
    print("\nSelect Enemy")
    if lizardman1['HP'] > 0 and lizardman2['HP'] > 0:
        print("1. Lizardman 1")
        print("2. Lizardman 2")
    elif lizardman1['HP'] <= 0 < lizardman2['HP']:
        print("2. Lizardman 2")
    elif lizardman1['HP'] > 0 >= lizardman2['HP']:
        print("1. Lizardman 1")


def selecthead():
    print("\nSelect Enemy")
    if head1['HP'] > 0 and head2['HP'] > 0 and head3['HP'] > 0:
        print("1. Head 1")
        print("2. Head 2")
        print("3. Head 3")
    elif head1['HP'] <= 0 < head2['HP'] and head3['HP'] > 0:
        print("2. Head 2")
        print("3. Head 3")
    elif head2['HP'] > 0 >= head2['HP'] and head3['HP'] > 0:
        print("1. Head 1")
        print("3. Head 3")
    elif head3['HP'] <= 0 < head1['HP'] and head2['HP'] > 0:
        print("1. Head 1")
        print("2. Head 2")
    elif head1['HP'] > 0 >= head2['HP'] and head3['HP'] <= 0:
        print("1. Head 1")
    elif head1['HP'] <= 0 < head2['HP'] and head3['HP'] <= 0:
        print("2. Head 2")
    elif head1['HP'] <= 0 < head3['HP'] and head2['HP'] <= 0:
        print("3. Head 3")


def enemyattack(enemy):
    if enemy['HP'] > 0:
        hitrate = enemy['ACC'] - ike['EVA']
        checker = rng()
        if checker <= hitrate:
            damage = enemy['STR'] * 2 - ike['DEF']
            ike['HP'] = ike['HP'] - damage
            print(f"Ike took {damage} from {enemy['Name']}'s attack")
            time.sleep(1)
        else:
            print(f"Ike dodged {enemy['Name']}'s attack.")
            time.sleep(1)


def ikeattacks(enemy):
    hitrate = ike['ACC'] - enemy['EVA']
    checker = rng()
    if checker <= hitrate:
        damage = ike['STR'] * 2 - enemy['DEF']
        enemy['HP'] = enemy['HP'] - damage
        print(f"\nIke dealt {damage} to {enemy['Name']}")
        time.sleep(1)
    else:
        print(f"\n{enemy['Name']} dodged Ike's attack.")
        time.sleep(1)


def pet(head):
    if head == head1:
        print(f"{head['Name']} loves it.")
        print(f"Petting {head['Name']} made the others angry")
        head1['STR'] = 6
        head2['STR'] = head2['STR'] * 3
        head3['STR'] = head3['STR'] * 3
    elif head == head2:
        print(f"{head['Name']} loves it.")
        print(f"Petting {head['Name']} made the others angry")
        head1['STR'] = head1['STR'] * 3
        head2['STR'] = 6
        head3['STR'] = head3['STR'] * 3
    elif head == head3:
        print(f"{head['Name']} loves it.")
        print(f"Petting {head['Name']} made the others angry")
        head1['STR'] = head1['STR'] * 3
        head2['STR'] = head2['STR'] * 3
        head3['STR'] = 5


def part1():
    print("After months of travelling, Ikie arrived at the gates of the demon castle to meet his mother.")
    print("The demon castle gate is being guarded by two lizardmen.")
    print("What will you do?")
    print("1. Confront lizardmen")
    print("2. Run away")
    action = int(input())
    if action == 1:
        if ike['HP'] > 0:
            while lizardman1['HP'] > 0 or lizardman2['HP'] > 0:
                print("\nYou are engaging the lizardmen guarding the gate.")
                print("What would you like to do?")
                print("1. Attack")
                print("2. Check status")
                print("3. Run away")
                action = int(input())
                if action == 1:
                    selectlizardmen()
                    counter = True
                    while counter:
                        action = int(input())
                        if action == 1:
                            ikeattacks(lizardman1)
                            enemyattack(lizardman1)
                            enemyattack(lizardman2)
                            counter = False
                            if lizardman1['HP'] <= 0:
                                print(f"\nYou have defeated {lizardman1['Name']}")
                        elif action == 2 and lizardman2['HP'] > 0:
                            ikeattacks(lizardman2)
                            enemyattack(lizardman1)
                            enemyattack(lizardman2)
                            counter = False
                            if lizardman2['HP'] <= 0:
                                print(f"\nYou have defeated {lizardman2['Name']}")
                        else:
                            print("Invalid enemy selected.")
                            selectlizardmen()
                elif action == 2:
                    counter = True
                    while counter:
                        selectlizardmen()
                        print("3. Ike's status")
                        action = int(input())
                        if action == 1:
                            status(lizardman1)
                            counter = False
                        elif action == 2:
                            status(lizardman2)
                            counter = False
                        elif action == 3:
                            status(ike)
                            counter = False
                        else:
                            print("No such enemy found.")
                            selectlizardmen()
                elif action == 3:
                    gameover()
                else:
                    print("Thank you for selecting a choice that does not exist.")
                    time.sleep(1)
                    print("Congrats, you broke the game so Bye Bye")
                    sys.exit(0)
        else:
            gameover()
    elif action == 2:
        gameover()
    else:
        print("No such option found. Try again!!\n")
        part1()


def part2():
    print("With the gaurds defeated, Ike enters the demon castle hallway.")
    time.sleep(1)
    print("The hallway is being guarded by the hellhound 'Cerberus'.")
    time.sleep(1)
    print("What would you like to do?")
    print("1. Confront Cerberus")
    print("2. Run away")
    if ike['HP'] > 0:
        action = int(input())
        if action == 1:
            while head1['HP'] > 0 or head2['HP'] > 0 or head3['HP'] > 0:
                if ike['HP'] <= 0:
                    print("You have been defeated by Cerberus.")
                    gameover()
                time.sleep(1)
                print("\nYou are engaging Cerberus in the hallway.")
                print("What would you like to do?")
                print("1. Attack")
                print("2. Check status")
                print("3. Pet")
                print("4. Run away")
                action = int(input())
                if action == 1:
                    selecthead()
                    counter = True
                    while counter:
                        action = int(input())
                        if action == 1 and head1['HP'] > 0:
                            ikeattacks(head1)
                            enemyattack(head1)
                            enemyattack(head2)
                            enemyattack(head3)
                            counter = False
                            if head1['HP'] <= 0:
                                print(f"\nYou have defeated {head1['Name']}")
                        elif action == 2 and head2['HP'] > 0:
                            ikeattacks(head2)
                            enemyattack(head1)
                            enemyattack(head2)
                            enemyattack(head3)
                            counter = False
                            if head2['HP'] <= 0:
                                print(f"\nYou have defeated {head2['Name']}")
                        elif action == 3 and head3['HP'] > 0:
                            ikeattacks(head3)
                            enemyattack(head1)
                            enemyattack(head2)
                            enemyattack(head3)
                            counter = False
                            if head3['HP'] <= 0:
                                print(f"\nYou have defeated {head3['Name']}")
                        else:
                            print("Invalid enemy selected.")
                            selecthead()
                elif action == 2:
                    counter = True
                    while counter:
                        selecthead()
                        print("4. Ike's status")
                        action = int(input())
                        if action == 1:
                            status(head1)
                            counter = False
                        elif action == 2:
                            status(head2)
                            counter = False
                        elif action == 3:
                            status(head3)
                            counter = False
                        elif action == 4:
                            status(ike)
                            counter = False
                        else:
                            print("No such enemy found.")
                            selecthead()
                elif action == 3:
                    counter = True
                    while counter:
                        selecthead()
                        action = int(input())
                        if action == 1:
                            pet(head1)
                            counter = False
                        elif action == 2:
                            pet(head2)
                            counter = False
                        elif action == 3:
                            pet(head3)
                            counter = False
                        else:
                            print("No such enemy found.")
                            selecthead()
                elif action == 4:
                    gameover()
                else:
                    print("Thank you for selecting a choice that does not exist.")
                    time.sleep(1)
                    print("Congrats, you broke the game so Bye Bye")
                    sys.exit(0)
        else:
            gameover()
    else:
        gameover()


def part3():
    print("After defeating the Cerberus, Ike enters the Throne Room where the demon queen is waiting who is "
          "also Ike's mother.")
    time.sleep(2)
    print("Upon entering the room, Ike sees a woman sitting on a large throne.")
    time.sleep(2)
    print("\"Hello Son.\", says the Demon Queen.")
    time.sleep(2)
    print("\"Now Get Ready to fight, Son.\", says the Demon Queen")
    time.sleep(2)
    print("'Ike gasps for breath and readies the stance to begin fighting.'")
    time.sleep(2)
    print("\"Let's see how well you're grown, Son\", says the Demon Queen")
    gameover()


def __main__():
    start()
    part1()
    time.sleep(3)
    part2()
    time.sleep(3)
    part3()


if __name__ == '__main__':
    __main__()
