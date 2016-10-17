# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:10:31 2016

@author: samanthacheng

maybe make separate grammars for different family members

"""

import nltk
from nltk.parse.generate import generate
import random

#----------------------------------------Grammar for Doctor 1-------------------------------------------------------#

grammar1 = nltk.CFG.fromstring("""
S1 -> SingNP SingVP | PluNP PluVP | PluNPDegRel PluVP | SingNPDegRel SingVP
SingNP -> MomDad | MotherFather | MaleFamMem | FemaleFamMem | FamSide MaleFamMem| FamSide FemaleFamMem | MalePropN | FemalePropN | MaleFamMem MalePropN | FemaleFamMem FemalePropN
PluNP -> SingNP Conj SingNP | SingNP Comma SingNP Conj SingNP | SingnP SingNP SingNP
SingNPDegRel -> DegreeRel
PluNPDegRel -> DegreeRel Conj DegreeRel
Conj -> 'and'
Comma -> ','
SingVP -> 'is' Adj | 'has' Diag | 'was' Adj | 'had' Diag | 'was_diagnosed with' Diag | 'died_of' Diag | 'suffered_from' Diag | 'suffers_from' Diag | 'smokes' | 'smoked'
PluVP -> 'are' Adj | 'have' Diag | 'were' Adj | 'had' Diag | 'were_diagnosed with' Diag | 'died_of' Diag | 'suffered_from' Diag | 'suffer_from' Diag | 'smoke' | 'smoked'
MomDad -> 'Mom' |'Dad'
MotherFather -> 'Mother' | 'Father'
PropN -> 'Vishal' | 'Marco' | 'Tony' | 'Zach' | 'Willi' | 'Eric'
FemalePropN -> 'Sophia' | 'Sharon' | 'Sana' | 'Rona' | 'Sarah' | 'Jamie'
FamSide -> 'maternal' | 'paternal'
MaleFamMem ->  'uncle' | 'grandpa' | 'grandfather' | 'cousin'
DegreeRel -> 'first degree relative' | 'second degree relative'
FemaleFamMem -> 'aunt'| 'grandma'  | 'grandmother' | 'cousin'
Adj -> 'obese' | 'overweight' | 'bulemic'
Diag1 -> ChronicDiag1 | AcuteDiag1
ChronicDiag1 ->'obesity' | 'overweight' | 'bulemia' | 'cardiovascular disease' | 'cvd' | 'hypertension' | 'cad' | 'coronary artery disease'
AcuteDiag2 -> 'stroke' | 'heart attack'
""")

grammar2 = nltk.PCFG.fromstring("""
S1 -> HPhrase Diag2 [1.0]
HPhrase -> 'Family history of' [1.0]
Diag2 -> 'smoking' [0.1] | 'obesity' [0.1] | 'overweight' [0.1] | 'cardiovascular disease' [0.1] | 'cvd' [0.1] | 'hypertension' [0.1] | 'cad' [0.1] | 'coronary artery disease' [0.1] | 'stroke' [0.1] | 'heart attack' [0.1]
""")

grammar3 = nltk.PCFG.fromstring("""
S1 -> 'Patient is' Adj [1.0]
Adj -> 'obese' [0.75] | 'hypertensive' [0.25]
""")

grammar4 = nltk.PCFG.fromstring("""
S1 -> 'Patient has' Diag [0.45] | HPhrase [0.45] | 'Patient has' HPhrase [0.1]
HPhrase -> ' history of' [1.0]
Diag -> 'high BP' [0.2] | 'hypertension' [0.2] | 'cvd' [0.2] | 'insomnia' [0.2] | 'arrhythmia' [0.2]
""")



#-----------------------------------------------Grammar for Doctor 2---------------------------------------------------------#


grammar5 = nltk.CFG.fromstring("""
S2 -> NP Comma Diag | NP Diag 'at' Age
NP -> 'uncle' | 'grandpa' | 'grandfather' | 'cousin' | 'aunt'| 'grandma'  | 'grandmother'
Comma -> ','
Diag -> AcuteDiag | ChronicDiag
AcuteDiag -> 'heart attack' | 'stroke'
Age -> '70' | '80' | '76' | '52'
""")

grammar6 = nltk.CFG.fromstring("""
S2 -> NP Comma Diag | NP Diag
NP -> 'uncle' | 'grandpa' | 'grandfather' | 'cousin' | 'aunt'| 'grandma'  | 'grandmother'
Comma -> ','
Diag -> AcuteDiag | ChronicDiag
ChronicDiag -> 'breast cancer'| 'cvd' | 'hypertension' | 'asthma'
""")

grammar7 = nltk.CFG.fromstring("""
S2 -> Diagd'age' Age | Diagd 'in' ApproxAge |  Diagd 'in' ApproxAage 'still living' | Diagd 'in' ApproxAage Died | Diaged 'with'
Diagd -> 'Diagnosed' | 'Dxd' | 'Dxed'
Age -> '70' | '63' | '82' | '54'
ApproxAge -> '70s' | '80s'| '90s' | 'late 70s' | 'late 60s' | 'late 50s'
Died -> 'deceseased' | 'died'
Diag -> 'hypertension' | 'cvd' | 'high bp'
""")

grammar8 = nltk.CFG.fromstring("""
S2 -> NP Comma Diag 'at' 'Age' Age Comma Diag 'at' 'Age' Age | NP Comma Diag 'at' 'Age' Age Comma Diag 'in' ApproxAge
NP -> '70' | '63' | '82' | '54'
Comma -> ','
ApproxAge -> '70s' | '80s'| '90s' | 'late 70s' | 'late 60s' | 'late 50s'
Diag -> 'hypertension' | 'cvd' | 'high bp' | 'cad'
""")


#------------------------------------Grammar for Doctor 3------------------------------------------------------#

#Each grammar as a separate family member with a list of their relevant medical history




#------------------------------------------Doctors' Notes in New File-----------------------------------------------#

def randomize(list):
    """Shuffle items in a list."""    
    random.shuffle(list)
    return list

def nobrackets(str):
    """Remove brackets in a string."""
    return str.replace('[', ' ').replace(']','')

def noquotations(str):
    """Remove single quotations in a string."""
    return str.replace("'", "")

def makegrammarnotes(grammar, n, m):
    gramlist = []  
    for sentpieces in generate (grammar, n):    
        sents = nltk.sent_tokenize(' '.join(sentpieces))
        gramlist.insert(-1,sents)
        gramfinallist= []
        if gramfinallist.count(sents) is 0:
            gramfinallist.extend(gramlist)
    randomize(gramfinallist)   
    return gramfinallist[:m]

def makenotes(biglist):
    """Using a list of all the notes to be included, print output on patienthistories file"""
    setdoctorsnotes = []
    setdoctorsnotes.extend(biglist)
    outfile.write(noquotations(nobrackets(','.join(map(str,setdoctorsnotes)))))
    outfile.write('\n\n')
    return nobrackets(noquotations(str(setdoctorsnotes)))


outfile = open('patienthistories.txt', 'w')
outfile.write('Patient History Notes \n\n')

for doctorsnotes1 in range(3):


    gram1notes = makegrammarnotes(grammar1, n = 10000, m = 10)
    gram2notes = makegrammarnotes(grammar2, n = 4, m = 3)
    gram3notes = makegrammarnotes(grammar3, n = 1, m = 1)
    gram4notes = makegrammarnotes(grammar4, n = 1, m = 5)
    gram5notes = makegrammarnotes(grammar5, n = 500, m = 1)
    gram6notes = makegrammarnotes(grammar6, n = 500, m = 1)
    gram7notes = makegrammarnotes(grammar7, n = 500, m = 1)

    gram1list = []  
    for sentpieces1 in generate (grammar1, n =  10000):    
        sents1 = nltk.sent_tokenize(' '.join(sentpieces1))
        gram1list.insert(-1,sents1)
        gram1finallist= []
        if gram1finallist.count(sents1) is 0:
            gram1finallist.extend(gram1list)
    randomize(gram1finallist)   
    gram1notes = gram1finallist[:10]
    

    gram2list = []
    for sentpieces2 in generate (grammar2, n = 4):    
        sents2 = nltk.sent_tokenize(' '.join(sentpieces2))
        gram2list.insert(-1,sents2)
        gram2finallist= []
        if gram2finallist.count(sents2) is 0:
            gram2finallist.extend(gram2list)
    randomize(gram2finallist)  
    gram2notes = gram2finallist[:3]   


    gram3list = []
    for sentpieces3 in generate (grammar3, n = 1):    
        sents3 = nltk.sent_tokenize(' '.join(sentpieces3))
        gram3list.insert(-1,sents3)
        gram3finallist= []
        if gram3finallist.count(sents3) is 0:
            gram3finallist.extend(gram3list)
    randomize(gram3finallist)
    gram3notes = gram3finallist[:1]


    gram4list = []
    for sentpieces4 in generate (grammar4, n = 1):    
        sents4 = nltk.sent_tokenize(' '.join(sentpieces4))
        gram4list.insert(-1,sents4)
        gram4finallist= []
        if gram4finallist.count(sents3) is 0:
            gram4finallist.extend(gram4list)
    randomize(gram4finallist)
    gram4notes = gram4finallist[:1]    
    

    gram5list = []  
    for sentpieces5 in generate (grammar5, n =  500):    
        sents5 = nltk.sent_tokenize(' '.join(sentpieces5))  
        gram5list.insert(-1,sents5)
        gram5finallist= []
        if gram5finallist.count(sents5) is 0:
            gram5finallist.extend(gram5list)
    randomize(gram5finallist)
    gram5notes = gram5finallist[:1]


    gram6list = []  
    for sentpieces6 in generate (grammar6, n =  500):    
        sents6 = nltk.sent_tokenize(' '.join(sentpieces6))  
        gram6list.insert(-1,sents6)
        gram6finallist= []
        if gram6finallist.count(sents6) is 0:
            gram6finallist.extend(gram6list)
    randomize(gram6finallist)
    gram6notes = gram6finallist[:1]


    gram7list = []
    for sentpieces7 in generate (grammar7, n =  500):    
        sents7 = nltk.sent_tokenize(' '.join(sentpieces7))  
        gram7list.insert(-1,sents6)
        gram7finallist= []
        if gram7finallist.count(sents7) is 0:
            gram7finallist.extend(gram7list)
    randomize(gram7finallist)
    gram7notes = gram7finallist[:1]    
    
    
    d1 = gram1notes + gram2notes
    d2 = randomize(gram3notes + gram4notes)
    d3 = gram5notes + gram6notes + gram7notes
    biglist = d1 + d2 + d3
    print(makenotes(biglist))


for doctorsnotes2 in range(3):
    
    gram5list = []  
    for sentpieces5 in generate (grammar5, n =  500):    
        sents5 = nltk.sent_tokenize(' '.join(sentpieces5))  
        gram5list.insert(-1,sents5)
        gram5finallist= []
        if gram5finallist.count(sents5) is 0:
            gram5finallist.extend(gram5list)
    randomize(gram5finallist)
    gram5notes = gram5finallist[:1]


    gram6list = []  
    for sentpieces6 in generate (grammar6, n =  500):    
        sents6 = nltk.sent_tokenize(' '.join(sentpieces6))  
        gram6list.insert(-1,sents6)
        gram6finallist= []
        if gram6finallist.count(sents6) is 0:
            gram6finallist.extend(gram6list)
    randomize(gram6finallist)
    gram6notes = gram6finallist[:1]


    gram7list = []
    for sentpieces7 in generate (grammar7, n =  500):    
        sents7 = nltk.sent_tokenize(' '.join(sentpieces7))  
        gram7list.insert(-1,sents6)
        gram7finallist= []
        if gram7finallist.count(sents7) is 0:
            gram7finallist.extend(gram7list)
    randomize(gram7finallist)
    gram7notes = gram7finallist[:1]    
    
    biglist = randomize(gram5notes + gram6notes + gram7notes)
    print(makenotes(biglist))


outfile.close()

#--------------------------------N-Gram Tagging----------------------------------------------#

"""
from nltk import word_tokenize
from nltk.util import ngrams

tokenized_notes = word_tokenize('IceCream.txt')
ngramnotes = ngrams(tokenized_notes,2)
print(ngramnotes)

starting_words = bigramnotes.generate(100)[-2:]
print(' '.join(bigramnotes))
practicenotes = ngrams(3,tokenized_notes)

starting_words = practicenotes.generate(100)
newnotes = practicenotes.generate(starting_words)
print(' '.join(newnotes))

"""






















#-------------------------------Trash Storage---------------------------------#

"""       
grammar2list = []
for sentpieces2 in generate (grammar2, n = 2):    
    sent2 = ' '.join(sentpieces2)
    sentz2 = nltk.sent_tokenize(sent2)  
    grammar2list = list(sentz2)
    random.shuffle(grammar2list)
    grammar2sents = ' '.join(grammar2list)
    grammar2sentslist = nltk.sent_tokenize(grammar2sents)
    print(grammar2sentslist)

grammar3list = []
for sentpieces3 in generate (grammar3, n = 1):    
    sent3 = ' '.join(sentpieces3)
    sentz3 = nltk.sent_tokenize(sent3)
    grammar3list = list(sentz3)
    random.shuffle(grammar3list)
    grammar3sents = ' '.join(grammar3list)
    grammar3sentslist = nltk.sent_tokenize(grammar3sents)
    print(grammar3sentslist)
"""