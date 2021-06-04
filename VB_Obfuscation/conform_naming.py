'''
This helps replace random strings with words that can be easily recognized

Modes:
    - Every word (cycles through all the unique words)
    - Entropy (not tested/ in-beta)
    - length bounds 
'''
from sys import argv
from re import findall
from collections import Counter
from math import log


def shannon_entropy(a_string):
    # I definitally took this from somewhere but dont remember the origin
    probabilities = []
    for x,n_x in Counter(a_string).items():
        probabilities.append( n_x/len(a_string))
    e_x = []
    for p_x in probabilities:
        e_x.append(-p_x*log(p_x,2))
    return sum(e_x)


def list_check(list_name, unique_found):
    with open(list_name, 'r') as to_check:
        split_list = to_check.read().split("\n")
        previous_checked = []
        duplicates = []
        count = 0
        for item in split_list:
            if(item not in previous_checked):
                previous_checked.append(item)
                count += 1
            else:
                duplicates.append(item)
            if(duplicates != []):
                print("ERROR: The following duplicates were found in" + list_name + "\n\n" +str(duplicates))
        to_check.close()
        '''
        if(list_word_count < unique_found):
            ask = input("Word list provided is shorter than the unique words found: " + str(list_word_count) + " vs " + str(unique_found) + "\nProceed? (y/n) ")
        if(ask.lower()[0] == "n"):
            quit()
        '''



def find_and_replace(file_name, list_name="Unique_words.txt", mode=0, new_file_name=0):
    unique_words = []
    translated_dict = {}
    input_file = open(file_name, 'r')
    input_file_full_contents = input_file.read()
    split_by_line = input_file_full_contents.split("\n")
    if(mode == 0):
        for line in split_by_line:
            words_within_split = findall("([A-Za-z0-9\_\"\']+)", line)
            for word in words_within_split:
                if(word not in unique_words and (word[0] != "\"" or word[0] != "\'")):
                    unique_words.append(word)
    elif(mode == 1):
        for line in split_by_line:
            words_within_split = findall("([A-Za-z0-9\_\"\']+)", line)
            for word in words_within_split:
                if(word not in unique_words and (word[0] != "\"" or word[0] != "\'")):
                    if(shannon_entropy(word) > 4):
                        unique_words.append(word)
    elif(mode == 2):
        for line in split_by_line:
            words_within_split = findall("([A-Za-z0-9\_\"\']+)", line)
            for word in words_within_split:
                if(word not in unique_words and (word[0] != "\"" or word[0] != "\'")):
                    if(len(word) > 6):
                        unique_words.append(word)
    
    
    
    
    # This performs some checks before creating translations
    list_check(list_name, len(unique_words))
    
    # Creates the translation dictionary
    counter = 0
    with open(list_name, 'r') as to_split:
        translation = to_split.read().split('\n')
        for item in unique_words:
            ask = input("WORD:\t" + str(item) + "\t\tadd to list (y/n)?")
            if(ask.lower()[0] == "y"):
                translated_dict[item] = translation[counter]
                counter += 1
    to_split.close()
    
    if(new_file_name == 0):
        if("." in file_name):
            new_file_name = file_name.split('.')[0] + "-new" + file_name.split('.')[1]
        else:
            new_file_name = file_name + "-new"
    for item in translated_dict:
        print("FROM:\t" + str(item) + "\tTO:\t" + str(translated_dict[item]))
        input_file_full_contents = input_file_full_contents.replace(item, translated_dict[item])
    new_file = open(new_file_name, 'w')
    new_file.write(str(input_file_full_contents))
    input_file.close()
    new_file.close()


if(__name__ == "__main__"):
    usage = """Usage: python conform_naming.py FILE_NAME -n NEW_LIST -m MODE -o NEW_FILE_NAME
    \nDescription:
        This script finds obfuscated variable/function names and replaces
        them with easy names to remember

        FILE_NAME:
            The name of the file to be edited
        NEW_LIST
            The name of the file with the new unique names (defaults to "Unique_words.txt" if not supplied)
        MODE:
            An option to speed up the process
                0: (default) Go through every word. This results in high fidelity.
                1: Shannon Entropy. This utilizes entropy of name to help eliminate common english words (in beta/not recommended)
                2. Length. Set a limited length as obfuscated tools usually choose lengthy random strings.
        NEW_FILE_NAME:
            The name of the new file to be outputed
            (defaults to adding a "-new" to the end of the file name)
    """
    if(len(argv) == 1 or argv[1].lower() == "-h" or argv[1].lower() == "--help"):
        print(usage)
    else:
        #find_and_replace(argv[1], list_name="Unique_words.txt", mode=0, new_file_name=0)
        if("-o" in argv):
            new_file_name = argv[argv.index("-o")+1]
        else:
            new_file_name = 0
        if("-m" in argv):
            mode = int(argv[argv.index("-m")+1])
        else:
            mode=0
        if("-n" in argv):
            list_name = argv[argv.index("-n")+1]
        else:
            list_name = "Unique_words.txt"
        find_and_replace(argv[1], list_name, mode, new_file_name)