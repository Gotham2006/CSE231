################################################################################
#
# Computer Project 05
#
# This project creates a dna series and genes file.
# These series are extracted from the file.
# Main
# They are then operated upon using multiple functions.
# These functions include
#     a - Search and display gene sequences for a species
#     b - Search and display all unique gene names from all species
#     c - Calculate hamming distance between two species
#     d - Display list of genes and their average hamming distance
#     e - Display list of species with the longest gene sequence length
#     q - terminate the program'''
#
# That is all that can be done with this program.
#
#
################################################################################

import csv
from operator import itemgetter

################
# Start your function definitions here

def open_file():
    """ Prompts for and opens a species file, re-tries if not found, It opens the txt file """
    speciesfile = "unopened"
    while speciesfile == "unopened":
        file_name = input("\n:~Enter a species file name ~:")
        try:
            fp_species = open("{}".format(file_name), "r")
            speciesfile = "opened"
        except FileNotFoundError:
            print("Invalid file name; please try again.")
    return fp_species


def open_file_csv():
    """ Prompts for and opens a genes file in CSV format, re-tries if not found, It opens the csv file """
    genesfile = "unopened"
    while genesfile == "unopened":
        file_name = input("\n:~Enter a genes file name ~:")
        try:
            fp_genes = open("{}".format(file_name), "r")
            genesfile = "opened"
        except FileNotFoundError:
            print("Invalid file name; please try again.")
    return fp_genes


def read_file(fp_species, fp_genes):
    """ Reads and returns species and gene data from respective files, it is then added to a list and closed """
    fp_genes_reader = csv.reader(fp_genes)
    next(fp_genes_reader, None)
    species_lst = []
    genes_lst = []

    for row in fp_genes_reader:
        genes_lst.append(row)

    for row in fp_species:
        species_lst.append(row.strip("\n"))

    fp_species.close()
    fp_genes.close()

    return species_lst, genes_lst


def validity_of_species(genes_lst):
    """ Validates and returns genes data for a valid species, it prints error messages if any problem occurs """
    species_name_validity = "Invalid"
    list_of_genes = []
    total_genes = 0
    while species_name_validity != "Valid":
        species_name = input(":~Please enter the name of a species ~:")
        species_name_upper = species_name[:-1] + species_name[-1].upper()
        for spec in genes_lst:
            if spec[1] == species_name_upper:
                species_name_validity = "Valid"
                list_of_genes.append(spec)
                for i in spec[2]:
                    if i.isalpha():
                        total_genes += 1
        if species_name_validity != "Valid":
            print("No species found.")

    return list_of_genes, total_genes, species_name


def gene_sequences(genes_lst):
    """ Displays all genes and sequences for a given species, uses two other functions to achieve this """
    list_of_genes, total_genes, species_name = validity_of_species(genes_lst)
    results_sorted = sorted(list_of_genes, key=itemgetter(1, 0))
    print("\nGenes for {}:".format(species_name))
    print("\n{:<25} | {:<50}".format("Gene", "Sequence"))  # for the header
    print(80 * "-")
    for i in results_sorted:
        print("{:<25} | {:<50}".format(i[0], i[2]))  # for the rows
    print(80 * "-")
    print("Total genes: {}".format(total_genes))


def gene_unique(genes_lst):
    """ Returns a list of unique gene names from the gene list, It achieves the goals of option b """
    unique_genes = []
    for row in genes_lst:
        if row[0] not in unique_genes:
            unique_genes.append(row[0])
    unique_genes.sort()
    return unique_genes


def two_strings(species_lst):
    """ Prompts and validates for two species names and returns them, It requests names until proper name is returned """
    stringone_validity = "Invalid"
    while stringone_validity == "Invalid":
        species_name_one = input(":~Please enter the name of a species ~:")
        stringone = species_name_one[:-1] + species_name_one[-1].upper()
        if stringone in species_lst:
            stringone_validity = "Valid"
        else:
            print("No species found.")

    stringtwo_validity = "Invalid"
    while stringtwo_validity == "Invalid":
        species_name_two = input(":~Please enter the name of a species ~:")
        stringtwo = species_name_two[:-1] + species_name_two[-1].upper()
        if stringtwo in species_lst:
            stringtwo_validity = "Valid"
        else:
            print("No species found.")
    return stringone, stringtwo, species_name_one, species_name_two


def gene_finder(stringone, stringtwo, genes_lst):
    """ Finds and returns the gene data for two species based on a given gene name """
    gene_name = input(":~Please enter the name of the genes ~:")
    validity_of_string_one = "Invalid"
    validity_of_string_two = "Invalid"
    string_one_row = " "
    string_two_row = " "
    gene_name_lower = gene_name.lower()
    for row in genes_lst:
        if row[0] == gene_name_lower and row[1] == stringone:
            validity_of_string_one = "Valid"
            string_one_row = row

    for row_two in genes_lst:
        if row_two[0] == gene_name_lower and row_two[1] == stringtwo:
            validity_of_string_two = "Valid"
            string_two_row = row_two

    if validity_of_string_one == "Valid" and validity_of_string_two == "Valid":
        check = gene_length(string_one_row, string_two_row)
        if check == "Invalid":
            return "Invalid", string_one_row, string_two_row, gene_name
        else:
            return "Valid", string_one_row, string_two_row, gene_name
    else:
        print("Gene not found.")
        return "Invalid", string_one_row, string_two_row, gene_name


def gene_length(string_one_row, string_two_row):
    """ Validates if the lengths of two gene sequences are the same """
    if len(string_one_row[2]) == len(string_two_row[2]):
        return "Valid"
    else:
        print("Gene sequences from both species must have the same length.")
        return "Invalid"


def hamming_distance(species_lst, genes_lst):
    """ Calculates and displays the Hamming distance between two species for a specific gene """
    total_hamming = 0
    total_distance = 0
    stringone, stringtwo, species_name_one, species_name_two = two_strings(species_lst)
    next_step, string_one_row, string_two_row, gene_name = gene_finder(stringone, stringtwo, genes_lst)
    if next_step != "Invalid":
        for i in range(len(string_one_row[2])):
            total_hamming += 1
            if string_one_row[2][i] != string_two_row[2][i]:
                total_distance += 1
        hamming_distance = total_distance / total_hamming
        print("\nCalculated hamming distance between '{}' and '{}':".format(species_name_one, species_name_two))
        print("{}: {:10.4f}".format(gene_name, hamming_distance))


def avg_hamming_distance(genes_lst, species_lst):
    """ Calculates the average Hamming distance between all species pairs for each unique gene """
    unique_genes = gene_unique(genes_lst)
    unique_pairs = []
    for i in range(0,len(species_lst)-1):
        for j in range(i+1, len(species_lst)):
            unique_pairs.append([species_lst[i], species_lst[j]])
    list_of_hamming_distances = []
    for gene in unique_genes:
        list_of_hamming_distances.append(hamming_distance_preconceived(gene, unique_pairs, genes_lst))
    list_of_hamming_distances = sorted(list_of_hamming_distances, key=itemgetter(1, 0), reverse=True)
    for p in list_of_hamming_distances:
        print(("{}: {:10.4f}".format(p[0], p[1])))


def hamming_distance_preconceived(gene, unique_pairs, genes_lst):
    """Calculates the Hamming distance for a given gene across all species pairs"""
    total_hamming = 0
    total_distance = 0
    string_one_row = None
    string_two_row = None
    for pair in unique_pairs:
        for row in genes_lst:
            if row[0] == gene and row[1] == pair[0]:
                string_one_row = row

        for row_two in genes_lst:
            if row_two[0] == gene and row_two[1] == pair[1]:
                string_two_row = row_two
    
        
        if string_one_row != None and string_two_row != None:
            if len(string_one_row[2]) == len(string_two_row[2]):
                string_one_seq = string_one_row[2].strip()
                string_two_seq = string_two_row[2].strip()
                value_of_range = min([len(string_one_seq),len(string_two_seq)])
                total_hamming += len(string_two_seq)
                for i in range(value_of_range):
                    if string_one_seq[i] != string_two_seq[i]:
                        total_distance += 1

    return [gene, total_distance / total_hamming]


def longest_gene_sequence(genes_lst, species_lst):
    """ Displays the species with the longest gene sequence length using two other lists """
    list_of_longest = []
    for specie in species_lst:
        max_length = 0
        max_row = None
        for row in genes_lst:
            if row[1] == specie:
                if len(row[2]) > max_length:
                    max_length = len(row[2])
                    max_row = row
        list_of_longest.append([specie.lower(), max_row[0], max_length])
    list_of_longest = sorted(list_of_longest, key = itemgetter(2,0), reverse = True)
    for long in list_of_longest:
        print(long)


def termination():
    """ Terminates the program by returning the string "q", it is used as a termination """
    return "q"


def banner():
    """ Returns the banner string to welcome the user when the program starts """
    return "\nBack to DNA"


def menu():
    """ Returns the available menu options for the user, given in the starter code """
    return '''\nOptions:
    a - Search and display gene sequences for a species
    b - Search and display all unique gene names from all species
    c - Calculate hamming distance between two species
    d - Display list of genes and their average hamming distance
    e - Display list of species with the longest gene sequence length
    q - terminate the program'''


def main():
    """ Executes all the code in the required format, using fourteen different functions """

    print(banner())

    species = open_file()
    gene = open_file_csv()
    species_lst = []
    genes_lst = []
    species_lst, genes_lst = read_file(species, gene)

    option = " "
    print(menu())
    while option != "q":

        option = input("\n:~Enter one of the listed options ~:").lower()

        if option == "a":
            gene_sequences(genes_lst)
            print(menu())

        elif option == "b":
            unique_genes = gene_unique(genes_lst)
            print(",".join(unique_genes))
            print(menu())

        elif option == "c":
            hamming_distance(species_lst, genes_lst)
            print(menu())

        elif option == "d":
            avg_hamming_distance(genes_lst, species_lst)
            print(menu())

        elif option == "e":
            longest_gene_sequence(genes_lst, species_lst)
            print(menu())

        elif option == "q":
            option = termination()

        else:
            print("Invalid option! Try again")

    print("\nThanks for using this program!\nHave a good day!\n")

# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()



