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
S2 -> Diagd 'age' Age | Diagd 'in' ApproxAge |  Diagd 'in' ApproxAage 'still living' | Diagd 'in' ApproxAage Died | Diagd 'with'
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

grammar9 = nltk.CFG.fromstring("""
S3 -> NP VP
NP -> 'Mom' | 'Mother' | 'Mother and Father'
VP -> Diagd 'age' Age ',' Diag | Diagd 'in' ApproxAge ',' Diag | Diagd 'in' ApproxAge Diag ',' 'still living' | Diagd 'in' ApproxAge 'with' Diag ',' Died | Diagd 'with' Diag | 'good health'
Diagd -> 'Diagnosed' | 'Dxd' | 'Dxed'
Age -> '70' | '63' | '82' | '54'
ApproxAge -> '70s' | '80s'| '90s' | 'late 70s' | 'late 60s' | 'late 50s'
Died -> 'deceseased' | 'died'
Diag -> 'hypertension' | 'cvd' | 'high bp'
""")

grammar10 = nltk.CFG.fromstring("""
S3 -> NP VP
NP -> 'Father'
VP -> 'has' ChronicDiag | ',' 'history of' ChronicDiag | 'had' AcuteDiag in 'ApproxAge' | Died
Diagd -> 'Diagnosed' | 'Dxd' | 'Dxed'
ApproxAge -> '70s' | '80s'| '90s' | 'late 70s' | 'late 60s' | 'late 50s'
Died -> 'deceased' | 'died'
ChronicDiag -> 'prostate cancer' |'bladder cancer' | 'hypertension'
AcuteDiag -> 'heart attack' | 'stroke'
""")

grammar11 = nltk.CFG.fromstring("""
S3 -> 'No siblings' | NP VP
NP -> 'sister' | 'brother' |
VP -> Diagd 'with' ChronicDiag ',' Age | Diagd 'with' ChronicDiag ',' ApproxAge | ChronicDiag | ChronicDiag
Diagd -> 'Diagnosed' | 'Dxd' | 'Dxed'
Age -> '10' | '12' |'15'
ApproxAge -> '20s'
ChronicDiag -> 'prostate cancer' |'bladder cancer' | 'hypertension'
""")

grammar12 = nltk.CFG.fromstring("""
S3 -> NP VP
NP -> 'grandparents' | 'grandfather' | 'gm' | 'gf'
VP -> 'has' Diag | Diagd 'with' Diag in 'ApproxAge' | Died
Diagd -> 'Diagnosed' | 'Dxd' | 'Dxed'
ApproxAge -> '70s' | '80s'| '90s' | 'late 70s' | 'late 60s' | 'late 50s'
Died -> 'deceased' | 'died'
ChronicDiag -> 'prostate cancer' |'bladder cancer' | 'hypertension'
Diag -> 'heart attack' | 'stroke'
""")



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

def grammar_notes(grammar, n, m):
    """ Generate n setnences from a particular grammar. Randomize sentences generated
    and select first m sentences.."""    
    gramlist = []  
    for sentpieces in generate (grammar, n=n):    
        sents = nltk.sent_tokenize(' '.join(sentpieces))
        gramlist.insert(-1,sents)
        gramfinallist= []
        if gramfinallist.count(sents) is 0:
            gramfinallist.extend(gramlist)
    randomize(gramfinallist)   
    return gramfinallist[:m]

def make_notes(biglist):
    """Using a list of all the notes to be included, print output on patienthistories file.
    Leave an empty line between each set of doctors' notes."""
    setdoctorsnotes = []
    setdoctorsnotes.extend(biglist)
    outfile.write(noquotations(nobrackets(','.join(map(str,setdoctorsnotes)).lower())))
    outfile.write('\n\n')
    return nobrackets(noquotations(str(setdoctorsnotes).lower()))



outfile = open('patienthistories.txt', 'w')
outfile.write('Patient History Notes \n\n')

for doctorsnotes1 in range(3):


    gram1notes = grammar_notes(grammar1, n = 10000, m = 10)
    gram2notes = grammar_notes(grammar2, n = 4, m = 3)
    gram3notes = grammar_notes(grammar3, n = 1, m = 1)
    gram4notes = grammar_notes(grammar4, n = 1, m = 5)
    gram5notes = grammar_notes(grammar5, n = 500, m = 1)
    gram6notes = grammar_notes(grammar6, n = 500, m = 1)
    gram7notes = grammar_notes(grammar7, n = 500, m = 1)

    
    d1 = gram1notes + gram2notes
    d2 = randomize(gram3notes + gram4notes)
    d3 = gram5notes + gram6notes + gram7notes
    full_list_1 = d1 + d2 + d3
    print(make_notes(full_list_1))


for doctorsnotes2 in range(3):
   
   
    gram5notes = grammar_notes(grammar5, n = 500, m = 1)
    gram6notes = grammar_notes(grammar6, n = 500, m = 1)
    gram7notes = grammar_notes(grammar7, n = 500, m = 1)
   
    
    full_list_2 = randomize(gram5notes + gram6notes + gram7notes)
    print(make_notes(full_list_2))


for doctorsnotes3 in range(2):
    
    
    gram9notes = grammar_notes(grammar9, n = 100, m = 1)
    gram10notes = grammar_notes(grammar10, n = 100, m= 1)
    gram11notes = grammar_notes(grammar11, n = 100, m = 1)
    gram12notes = grammar_notes(grammar12, n = 100, m = 1)
    full_list_3 = gram9notes + gram10notes + gram11notes + gram12notes
    
    print(make_notes(full_list_3))


outfile.close()


#--------------------------------Some Useless Trash I Guess I'm Still Keeping-----------------------------------#


'''
def ngrams(input, n):
    input = word_tokenize(input)
    output = {}
    for i in range(len(input)-n+1):
        g = ' '.join(input[i:i+n])
        output.setdeafult(g,0)
        output[g] += 1
    return output

text = open('IceCream.txt','r')
print(ngrams(text, 2))

text = open('IceCream.txt', 'r').read()
table = string.maketrans(" ", " ")
text = text.translate(Table, string.punctuation)
tokens = word_tokenize(text.lower())
bigram = nltk.bigrams(tokens)

def word_grams(words):
    s = []
    for ngram in ngrams(words, 3):
        s.append(' '.join(str(i) for i in ngram))
    return str(s)
 
print(word_grams(text))
 
def prep_txt(txt):
    f = open(txt,'r')
    for word in f.read().split():
        return word

with open ('IceCream.txt', 'r') as f:
    for line in f:
        for word in line.split():
            print(word_grams(word))

txt = str('IceCream.txt')
tokenized_notes = word_tokenize(txt)
ngramnotes = ngrams('one two three four five',2)
print(ngramnotes)


starting_words = bigramnotes.generate(100)[-2:]
print(' '.join(bigramnotes))
practicenotes = ngrams(3,tokenized_notes)

starting_words = practicenotes.generate(100)
newnotes = practicenotes.generate(starting_words)
print(' '.join(newnotes))
'''