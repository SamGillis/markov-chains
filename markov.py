"""Generate Markov text from text files."""

import random
import string
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Name variable to open file
    the_file = open(file_path)
    the_file = the_file.read()
    the_file = the_file.replace('\n', ' ')

    return the_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    #Set variable chains to empty dictionary 
    chains = {}
    #Set variable to a list which contains text_strings without space
    words = text_string.split(' ')
    #Look through list of word
    for i in range(len(words)-3):
        #Creates key
        chains[(words[i], words[i+1])] = (chains.get((words[i], words[i+1]), []))
        chains[(words[i], words[i+1])].append(words[i+2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # Get random key to start with bigram
    bigram = random.choice(list(chains))
    while bigram[0][0].upper() != bigram[0][0]:
        bigram = random.choice(list(chains))

    #Add bigram (key)
    words.append(bigram[0])
    words.append(bigram[1])
    
    #Perform if bigram is a key in chains (i.e., ('a', 'house', 'hi'))
    while bigram in chains.keys():
        next_word = random.choice(chains[bigram])

        #Add new word to list
        words.append(next_word) 
        bigram = (words[-2], words[-1])
        
    #Return string of list without comma and space added
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1]) + open_and_read_file(sys.argv[2])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
