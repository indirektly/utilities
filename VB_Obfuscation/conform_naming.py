'''
This helps replace random strings with words that can be easily recognized

Modes:
    - Every word (cycles through all the unique words)
    - Entropy (not tested/ in-beta)
    - length bounds 
'''
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


def list_check(file_name, unique_found):
    with open(file_name, 'r') as to_check:
        split_list = to_check.split("\n")
        previous_checked = []
        duplicates = []
        count = 0
        for item in split_list:
            if(item not in previous_checked):
                previous_checked.append[item]
                count += 1
            else:
                duplicates.append(item)
            if(duplicates != []):
                print("ERROR: The following duplicates were found in" + file_name + "\n\n" +str(duplicates))
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
    split_by_line = input_file.split("\n")
    if(mode == 0):
        for line in split_by_line:
            words_within_split = findall("[A-Za-z0-9\_]+", line)
            for word in words_within_split:
                if(word not in unique_words):
                    unique_words.append(word)
    elif(mode == 1):
        for line in split_by_line:
            words_within_split = findall("[A-Za-z0-9\_]+", line)
            for word in words_within_split:
                if(word not in unique_words):
                    if(shannon_entropy(word) > 4):
                        unique_words.append(word)
    elif(mode == 2):
        for line in split_by_line:
            words_within_split = findall("[A-Za-z0-9\_]+", line)
            for word in words_within_split:
                if(word not in unique_words):
                    if(len(word) > 6):
                        unique_words.append(word)
    
    
    
    
    # This performs some checks before creating translations
    list_check(list_name, len(unique_words))
    
    # Creates the translation dictionary
    counter = 0
    with open(list_name, 'r') as to_split:
        translation = to_split.split('\n')
        for item in unique_words:
            ask = input("WORD:\t" + str(item) + "\tadd to list (y/n)?")
            if(ask.lower()[0] == "y"):
                translated_dict[word] = translation[counter]
                counter += 1
    to_split.close()
    
    if(new_file_name == 0):
        if("." in file_name):
            new_file_name = file_name.split('.')[0] + "-new" + file_name.split('.')[1]
        else:
            new_file_name = file_name + "-new"
    for item in translated_dict:
        input_file.replace(item, translated_dict[item])
    new_file = open("new_file_name", 'w') = input_file
    input_file.close()
    new_file.close()