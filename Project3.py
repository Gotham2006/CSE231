################################################################################
#
# Computer Project 03
#
# The goal of the project is to create a DNA Alignment algorithm.
# A main menu displays all the possible options.
# The user than inputs what action they would like to choose.
#
#
#
#
#
################################################################################

banner = r"""
============================================
    PROJECT HELIX: DNA ALIGNMENT
============================================
    🧬 Optimizing DNA Storage & Transmission   
    🚀 Accelerating Bioinformatics Research  

    A--T   C--G   G--C   T--A   A--T   G--C
    |      |      |      |      |      |
    T--A   G--C   C--G   A--T   T--A   C--G
============================================
"""

# Print the initial banner and menu to the user
print(banner)  # The project banner

exit = " "

menu = '''\nPlease choose one of the options below:
\tA. DNA Sequence Alignment
\tH. Display the menu of options.
\tX. Exit.'''  # Main menu

action = '''\n:~What do you want to do:
    a (add indel)
    d (delete indel)
    s (score)
    q (quit) ~:'''  # The possible actions on the string

# Constant of allowed characters
dna_letters = "ATCGatcg"

print(menu)

while exit != "X":

    option = input("\n:~Enter option ~:")

    if option in "xX":  # Exiting Menu
        exit = "X"

    elif option in "hH":  # Returning to Menu
        print(menu)

    elif option in "aA":

        validity_of_string_one = "Invalid"

        while validity_of_string_one == "Invalid":
            stringone = input("\n:~Input String 1 ~:")  # String 1

            for i in stringone:

                if i not in dna_letters:
                    validity_of_string_one = "Invalid"
                    print("Invalid characters in the DNA sequence\n")
                    break

                else:
                    validity_of_string_one = "Valid"

        validity_of_string_two = "Invalid"

        while validity_of_string_two == "Invalid":

            stringtwo = input(":~Input String 2 ~:")  # String 2

            for i in stringtwo:

                if i not in dna_letters:
                    validity_of_string_two = "Invalid"
                    print("Invalid characters in the DNA sequence\n")
                    break

                else:
                    validity_of_string_two = "Valid"

        validity_of_action = "Invalid"

        while validity_of_action == "Invalid":
            actionone = input(action)

            if actionone in "aA":

                choosestring = input("\n:~Work on which string (1 or 2) ~:")

                if choosestring == "1":
                    strone = stringone
                    choose_index_validity = "Invalid"

                    while choose_index_validity == "Invalid":
                        chooseindex = int(input(":~Before what index ~:"))

                        if chooseindex > (len(strone) - 1):
                            print("Insert index out of range\n")
                            continue

                        else:
                            strone = strone[:chooseindex] + "-" + stringone[chooseindex:]
                            stringone = strone
                            choose_index_validity = "Valid"

                elif choosestring == "2":

                    strtwo = stringtwo
                    choose_index_validity = "Invalid"

                    while choose_index_validity == "Invalid":
                        chooseindex = int(input(":~Before what index ~:"))

                        if chooseindex > (len(strtwo) - 1):
                            print("Insert index out of range\n")
                            continue

                        else:
                            strtwo = strtwo[:chooseindex] + "-" + stringtwo[chooseindex:]
                            stringtwo = strtwo
                            choose_index_validity = "Valid"

            elif actionone in "dD":

                choosestring = input("\n:~Work on which string (1 or 2) ~:")

                if choosestring == "1":
                    strone = stringone
                    delete_what_validity = "Invalid"

                    while delete_what_validity == "Invalid":
                        deletewhat = int(input(":~Delete what  ~:"))

                        if deletewhat > (len(strone) - 1):
                            print("Delete index out of range\n")
                            continue

                        else:
                            delete_what_validity = "Valid"

                            if strone[deletewhat] == "-":
                                strone = strone[:deletewhat] + stringone[deletewhat + 1:]
                                stringone = strone

                            else:
                                print("Not an indel")

                elif choosestring == "2":
                    strtwo = stringtwo
                    delete_what_validity = "Invalid"

                    while delete_what_validity == "Invalid":
                        deletewhat = int(input(":~Delete what  ~:"))

                        if deletewhat > (len(strtwo) - 1):
                            print("Delete index out of range\n")
                            continue

                        else:
                            delete_what_validity = "Valid"

                            if strtwo[deletewhat] == "-":
                                strtwo = strtwo[:deletewhat] + stringtwo[deletewhat + 1:]
                                stringtwo = strtwo


                            else:
                                print("Not an indel")

            elif actionone in "sS":
                matches = 0
                mismatches = 0
                strone = ""
                strtwo = ""
                max = 0

                if len(stringone) == len(stringtwo):
                    minimum = len(stringone)

                    for i in range(minimum):

                        if stringone[i] == stringtwo[i]:
                            matches += 1
                            strone = strone + stringone[i].lower()
                            strtwo = strtwo + stringtwo[i].lower()

                        else:
                            mismatches += 1
                            strone = strone + stringone[i].upper()
                            strtwo = strtwo + stringtwo[i].upper()

                elif len(stringone) < len(stringtwo):
                    minimum = len(stringone)
                    extrachar = len(stringtwo) - len(stringone)


                    for i in range(minimum):

                        if stringone[i] == stringtwo[i]:
                            matches += 1
                            strone = strone + stringone[i].lower()
                            strtwo = strtwo + stringtwo[i].lower()

                        else:
                            mismatches += 1
                            strone = strone + stringone[i].upper()
                            strtwo = strtwo + stringtwo[i].upper()

                    strone += "-" * extrachar
                    strtwo += stringtwo[-extrachar:].upper()
                    mismatches += extrachar

                else:
                    minimum = len(stringtwo)
                    extrachar = len(stringone) - len(stringtwo)

                    for i in range(minimum):

                        if stringone[i] == stringtwo[i]:
                            matches += 1
                            strone = strone + stringone[i].lower()
                            strtwo = strtwo + stringtwo[i].lower()

                        else:
                            mismatches += 1
                            strone = strone + stringone[i].upper()
                            strtwo = strtwo + stringtwo[i].upper()



                    strtwo += "-" * extrachar
                    strone += stringone[-extrachar:].upper()
                    mismatches += extrachar

                print(len(strone))
                print(len(strtwo))
                print("\nMatches: {} Mismatches: {}".format(matches, mismatches))
                print("String 1: {}".format(strone))
                print("String 2: {}".format(strtwo))

            elif actionone in "qQ":
                validity_of_action = "Valid"

            else:
                continue

    else:
        print("Invalid options. Please try again")
        print(menu)

print("Exiting program...\nBeware of computational biologist they screw genes and protein!")
