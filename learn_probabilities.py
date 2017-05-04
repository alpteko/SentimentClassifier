import re
from os import listdir

# Global Variables
pos_probability = {}
neg_probability = {}
general_dictionary = {}


def tokenize(corpus):
    all_words = re.findall(r'\w+', corpus.lower())
    return all_words


def traverse_files(path, review_type):
    total_word = 0
    for file in listdir(path):
        if file.endswith(".txt"):
            corpus = open(path+'/'+file).read()
            word_list = tokenize(corpus)
            count = update_dictionary(word_list, review_type)
            total_word += count
    return total_word


def add_dictionary(word, review_type):
    global pos_probability
    global neg_probability
    if review_type is 1:
        if word in pos_probability:
            pos_probability[word] += 1
        else:
            pos_probability[word] = 0
    else:
        if word in neg_probability:
            neg_probability[word] += 1
        else:
            neg_probability[word] = 0


def update_dictionary(word_list, review_type):
    global general_dictionary
    for word in word_list:
        general_dictionary[word] = 0
        add_dictionary(word, review_type)
    return len(word_list)


def complete_general_dictionary(path):
    global general_dictionary
    for file in listdir(path):
        if file.endswith(".txt"):
            corpus = open(path+'/'+file).read()
            word_list = tokenize(corpus)
            for word in word_list:
                general_dictionary[word] = 0


