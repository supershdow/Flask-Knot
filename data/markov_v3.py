#markov chain text generator with variable key length

import Reader as reader
from random import choice
from random import random

KEY_SIZE = 5
book_dir = './data/book/'
FILE = book_dir + 'sherlock_clean.txt'

def generate_chains( fname, key_size ):
    chains = {}
    text = reader.read_file( fname )
    
    words = text.split()
    i = 0
    while i < len(words) - key_size:
        key = ' '.join( words[i : i+key_size] ) 
        value = words[i + key_size]
        if key in chains:
            chains[ key ].append( value )
        else:
            new_list = []
            new_list.append( value )
            chains[ key ] = new_list
        i+= 1
    return chains


def generate_text( chains, num_words, key_size ):
    key = choice( chains.keys() )
    s = key
    i = 0
    while i < num_words:
        word = choice( chains[ key ] )
        s+= ' ' + word
        key = ' '.join(key.split()[1 : key_size + 1])
        if key_size > 1:
            key+= ' '        
        key+= word
        i+= 1
    return s



# chains = generate_chains( FILE, KEY_SIZE )
# print chains

# text = generate_text( chains, 300, KEY_SIZE )

# print text.capitalize()

def markov_generator(bookname):
    if bookname == 'Alice in Wonderland':
        wonder_chains= generate_chains( book_dir +
                                        'wonderland_clean.txt', 5 )
        markov= generate_text( wonder_chains, 500, 5 )
        #print wonder_text
        #return wonder_text
    
    if bookname == 'Sherlock Holmes':
        sherlock_chains= generate_chains(book_dir +
                                         'sherlock_clean.txt', 5 )
        markov= generate_text(sherlock_chains , 500, 5)
        #print sherlock_text
        #return sherlock_text
    
    if bookname == 'Tom Sawyer':
        sawyer_chains= generate_chains(book_dir + 'sawyer_clean.txt', 5)
        markov= generate_text (sawyer_chains , 500, 5)
        #print sawyer_text
    if bookname == 'War of the Worlds':
        war_chains= generate_chains( book_dir + 'war_of_the_worlds_clean.txt', 5)
        markov= generate_text (war_chains, 500, 5)
    return markov.capitalize()
