################################################################################
#
# Computer Project 02
#
# This project is focused on the game Oddly.
#
# The goal is to reach an odd number of stones when the game is done.
# The opponent is the computer.
# The winner is whoever has the greatest amount of victories.
#
################################################################################

banner = """*** Welcome to the Oddly Game! ***
*Let's see if you can beat the odds!*"""

rules = """\nOddly is a strategic two-player game that challenges your ability
to think ahead.
The game begins with two piles of stones split from an odd total number of stones.
Players take turns removing stones from the piles.
The game ends when all stones are removed. The winner? The player who ends up
with an odd number of stones!
Good luck, and don't let the computer outsmart you!"""

print(banner)
print(rules)

computer = 0
human = 0

yn = input("\n:~Would you like to play? (0=no, 1=yes) ~:")

while yn == "1":

    print("\nStarting a new game...")
    odd = "Yes"
    human_stones = 0
    computer_stones = 0
    pile_1 = 0
    pile_2 = 0

    while odd == "Yes":
        inp_stones = int(input("\n:~How many stones would you like to play? ~:"))

        if inp_stones > 1 and inp_stones % 2 != 0:
            odd = "No"

        else:
            print("The total number of stones must be odd and greater than 1.")

    pile_1 = inp_stones // 2 + 1
    pile_2 = inp_stones // 2
    print("Start --> Pile 1:", pile_1, ", Pile 2:", pile_2)

    while pile_1 != 0 or pile_2 != 0:
        pile = int(input("\n:~Choose a pile (1 or 2) ~:"))

        if pile == 1 and pile_1 > 0:
            a = 0

            while a == 0:
                rmv = int(input("\n:~Choose stones to remove from pile ~:"))

                if rmv < 1 or rmv > 3:
                    print("Invalid number of stones. Please try again.")
                    continue
                check = pile_1 - rmv

                if check >= 0:
                    pile_1 = check
                    human_stones += rmv
                    a = 1
                    print("\nPlayer ->", "Remove", rmv, "stones from pile 1")
                    print("Pile 1:", pile_1, ", Pile 2:", pile_2)

                    if pile_2 > 0:
                        pile_2 -= 1
                        computer_stones += 1
                        print("\nComputer ->", "Remove 1 stones from pile 2")
                        print("Pile 1:", pile_1, ", Pile 2:", pile_2)

                    elif pile_1 > 0:
                        pile_1 -= 1
                        computer_stones += 1
                        print("\nComputer ->", "Remove 1 stones from pile 1")
                        print("Pile 1:", pile_1, ", Pile 2:", pile_2)

                    else:
                        a = 1

                else:
                    print("Invalid number of stones. Please try again.")

        elif pile == 2 and pile_2 > 0:
            b = 0

            while b == 0:
                rmv = int(input("\n:~Choose stones to remove from pile ~:"))

                if rmv < 1 or rmv > 3:
                    print("Invalid number of stones. Please try again.")
                    continue

                check = pile_2 - rmv
                if check >= 0:
                    pile_2 = check
                    human_stones += rmv
                    b = 1
                    print("\nPlayer ->", "Remove", rmv, "stones from pile 2")
                    print("Pile 1:", pile_1, ", Pile 2:", pile_2)

                    if pile_1 > 0:
                        pile_1 -= 1
                        computer_stones += 1
                        print("\nComputer ->", "Remove 1 stones from pile 1")
                        print("Pile 1:", pile_1, ", Pile 2:", pile_2)

                    elif pile_2 > 0:
                        pile_2 -= 1
                        computer_stones += 1
                        print("\nComputer ->", "Remove 1 stones from pile 2")
                        print("Pile 1:", pile_1, ", Pile 2:", pile_2)

                    else:
                        b = 1

                else:
                    print("Invalid number of stones. Please try again.")

        else:
            print("Pile must be 1 or 2 and non-empty. Please try again.")

    if pile_1 == 0 and pile_2 == 0:

        if human_stones % 2 == 0:
            print("\nStones -> human:", human_stones, "; computer:", computer_stones)
            print("Computer wins!")
            computer += 1

        else:
            print("\nStones -> human:", human_stones, "; computer:", computer_stones)
            print("CONGRATULATIONS! Player wins!")
            human += 1

        print("\nCurrent Score -> human:", human, "; computer:", computer)

    yn = input("\n:~Would you like to play again? (0=no, 1=yes) ~:")
print("\nThanks for playing! See you again soon!")
