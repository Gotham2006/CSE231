################################################################################
# Computer Project 04
#
# The goal of the project is to create a DNA Alignment algorithm.
# A main menu displays all the possible options.
# You can add indels, delete indels, score and compress the DNA sequence.
# All of this is done through user inputted commands.
# The user than inputs what action they would like to choose.
#
#
#
#
#
#
################################################################################


# Start your function definitions here

def exiting():
    """ This function terminates the program and therefore is used in a while loop. """
    return "X"


def input_string():
    """ This function allows the user to input the DNA Strings."""

    dna_letters = "ATCGatcg"
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
    return stringone, stringtwo


def add_indel(stringone, stringtwo):
    """ This function allows the user to ass an indel to the DNA Strings."""
    strone = stringone
    strtwo = stringtwo

    choosestring = input("\n:~Work on which string (1 or 2) ~:")

    if choosestring == "1":
        choose_index_validity = "Invalid"

        while choose_index_validity == "Invalid":
            chooseindex = int(input(":~Before what index ~:"))

            if chooseindex > (len(strone) - 1):
                print("Insert index out of range\n")
                continue

            else:
                strone = strone[:chooseindex] + "-" + stringone[chooseindex:]
                choose_index_validity = "Valid"

    elif choosestring == "2":
        choose_index_validity = "Invalid"

        while choose_index_validity == "Invalid":
            chooseindex = int(input(":~Before what index ~:"))

            if chooseindex > (len(strtwo) - 1):
                print("Insert index out of range\n")
                continue

            else:
                strtwo = strtwo[:chooseindex] + "-" + stringtwo[chooseindex:]
                choose_index_validity = "Valid"
    return strone, strtwo

def del_indel(stringone,stringtwo):
    """ This function allows the user to delete an indel from the DNA Strings."""
    choosestring = input("\n:~Work on which string (1 or 2) ~:")
    strone = stringone
    strtwo = stringtwo

    if choosestring == "1":
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

                else:
                    print("Not an indel")

    elif choosestring == "2":
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

                else:
                    print("Not an indel")
    return strone, strtwo

def score(stringone,stringtwo):
    """ This function allows the user to score the DNA Strings."""

    matches = 0
    mismatches = 0
    strone = ""
    strtwo = ""

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

    print("\nMatches: {} Mismatches: {}".format(matches, mismatches))
    print("String 1: {}".format(strone))
    print("String 2: {}".format(strtwo))

def menh():
    """  This function is used to print the menu for option h """
    menu = '''\nPlease choose one of the options below:
    \tA. DNA Sequence Alignment
    \tC. DNA Sequence Compression
    \tH. Display the menu of options.
    \tX. Exit.'''
    print(menu)


def compressed():
    """This function allows the user to compress the DNA Strings."""
    dna_letters = "ATCG"
    validity_of_sequence = "Invalid"

    while validity_of_sequence == "Invalid":
        sequence = input(":~Enter DNA sequence ~:").upper()

        for i in sequence:
            if i not in dna_letters:
                validity_of_sequence = "Invalid"
                print("Invalid characters in the DNA sequence\n")
                break
            else:
                validity_of_sequence = "Valid"

    print("\nOriginal DNA Sequence:")
    print(sequence)

    compressed = ""
    i = 0
    n = len(sequence)

    while i < n:
        max_length = 0
        position = -1

        for j in range(i):
            length = 0
            while (i + length < n and j + length < i and sequence[j + length] == sequence[i + length]):
                length += 1

            if length >= 3 and length > max_length:
                max_length = length
                position = j

        if max_length >= 3:
            compressed += f'({position},{max_length})'
            i += max_length
        else:
            compressed += sequence[i]
            i += 1

    print("\nCompressed DNA Sequence:")
    print(compressed)


def main():
    "This function executes the entire code"

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

    menu = '''\nPlease choose one of the options below:
    \tA. DNA Sequence Alignment
    \tC. DNA Sequence Compression
    \tH. Display the menu of options.
    \tX. Exit.'''

    action = '''\n:~What do you want to do:
        a (add indel)
        d (delete indel)
        s (score)
        q (quit) ~:'''

    exiting_string = " "

    # Print the initial banner and menu to the user
    print(banner)
    print(menu)

    # Complete your code for the main function from here
    while exiting_string != "X":

        option = input("\n:~Enter option ~:")

        if option in "xX":  # Exiting Menu
            exiting_string = exiting()

        elif option in "hH":  # Returning to Menu
            menh()

        elif option in "cC":
            compressed()

        elif option in "aA":
            stringone,stringtwo=input_string()
            validity_of_action = "Invalid"

            while validity_of_action == "Invalid":
                actionone = input(action)

                if actionone in "aA":
                    stringone,stringtwo=add_indel(stringone,stringtwo)

                elif actionone in "dD":
                    stringone,stringtwo=del_indel(stringone,stringtwo)

                elif actionone in "sS":
                    score(stringone,stringtwo)

                elif actionone in "qQ":
                    validity_of_action = "Valid"

                else:
                    continue

        else:
            print("Invalid options. Please try again")
            print(menu)
    print("Exiting program...\nBeware of computational biologist they screw genes and protein!")


# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in a function.
if __name__ == "__main__":
    main()


