##!/usr/bin/python

import Reader
import random


#book=['sawyer_clean.txt']
book=['sawyer_clean.txt','sherlock_clean.txt','war_of_the_worlds_clean.txt','wonderland_clean.txt']
numWords = 100



def createDict(books):
    Dict={}
    for book in books:
        #print book
        words=Reader.read_file(book).split()
        #print words
        a=1
        #print len(words)
        for word in words:
            #print word
            w=word
            x=words[a]
            y=words[a+1]
            a+=1
            newKey=w,x
            #print newKey
            if w in Dict:
                Dict[newKey].append(y)
            else:
                Dict[newKey]=[y]
            if a==len(words)-2:
                #print a
                break 
           #print Dict
    return Dict


def createSentence(length,book):
    d=createDict(book)
    sentence=''
    #print d
    first=random.choice(d.keys())
    #print first
    sentence+=random.choice(first)+" "
    previous=first
    i=0
    while i < length:
        #print previous
        try:
            Next=d[previous]
        except KeyError:
            previous=random.choice(d.keys())
            Next=d[previous]
        #Next=d[previous]
        #print Next
        #print '\n'
        previous=previous[1],Next[0]
        #print previous
        sentence+=Next[0]+" "
        #print sentence
        i+=1
    return sentence


#print 'Content-type: text/html\n\n'


#createSentence(500,book)
#print createSentence(500,["wonderland_clean.txt"])
#print createDict(['wonderland_clean.txt'])
#for a in book:
    #print createSentence(500,[a])
