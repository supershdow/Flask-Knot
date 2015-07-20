from random import random
import Reader


Dict=Reader.getCsvDict('data/wordlist.csv')
Subjects=Dict['nouns']
Verbs=Dict['verbs']
Adjectives=Dict['adjectives']
Adverbs=Dict['adverbs']
Objects=Subjects



"""
lines=Reader.getCsvList('wordlist.csv')

Subjects=lines[0]
Subjects.pop(0)
Verbs=lines[1]
Verbs.pop(0)
Adjectives=lines[2]
Adjectives.pop(0)
Adverbs=lines[3]
Adverbs.pop(0)
Objects=Subjects
"""



#Subjects=["Stanley","Lev","Spencer","Josh","Michael","Topher","JonAlf","Chris","Abdullah","Zane","Justin"]
#Verbs=["walks","runs","strolls","saunters","travels","drives","presents","explains","projects"]


#Adjectives=["cool","boring","ghetto","stupid","swell","hungry"]
Articles=["the","a"]
#Objects=["store","house","job","school","computer","bed","game","presentation"]
#Adverbs=["quickly","intelligently","magically","mightily","carefully"]


def oneOf(listIn):
    return listIn[int(random()*len(listIn))]

def probabilityTrue(chance):
    if random()<=chance:
        return True
    else:
        return False

def nounPhrase():
    nounPhrase=""
    if probabilityTrue(.5)==True:
        nounPhrase+=oneOf(Articles)+" "
    while probabilityTrue(.5)==True:
        nounPhrase+=oneOf(Adjectives)+" "
    nounPhrase+=oneOf(Subjects)
    return nounPhrase.capitalize()
    
def verbPhrase():
    verbPhrase=oneOf(Verbs)
    if probabilityTrue(.5)==True:
        verbPhrase+=" "+oneOf(Objects)
    if probabilityTrue(.5)==True:
        verbPhrase+=" "+oneOf(Adverbs)
    return verbPhrase

def senGen(n):
    sentences=''
    for i in range(n):
        sentences+= nounPhrase()+" "+verbPhrase()+"! "
    return sentences

#senGen(1)

