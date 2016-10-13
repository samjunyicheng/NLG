# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:10:31 2016

@author: samanthacheng

ex:
family history of...
history of....
mother had...
mother died of.....
mother/father/(maternal/paternal) grandmother/grandfather/sister/brother/sibling/aunt/uncle
*names*
...diagnosed with....


"""

import nltk
from nltk.parse.generate import generate

grammar1 = nltk.CFG.fromstring("""
S1 -> NP VP | NP 'and' NP VP | NP ',' NP ', and' NP VP
NP -> MomDad | det MaleFamMem | det FemaleFamMem | det FamSide MaleFamMem| det FamSide FemaleFamMem | FamSide MaleFamMem | FamSide FemaleFamMem | MalePropN | FemalePropN | MaleFamMem MalePropN | FemaleFamMem FemalePropN
VP -> 'is' Adj | 'has' Diag | 'was' Adj | 'had' Adj | 'was diagnosed with' Diag | 'died of' Diag | 'suffered from' Diag | 'suffers from' Diag | 'smokes'
MomDad -> 'Mom' |'Dad'
PropN -> 'Vishal' | 'Marco' | 'Tony' | 'Zach' | 'Willi' | 'Eric'
FemalePropN -> 'Sophia' | 'Sharon' | 'Sana' | 'Rona' | 'Sarah' | 'Jamie'
det -> 'the'
FamSide -> 'maternal' | 'paternal'
MaleFamMem ->  'uncle' | 'grandpa' | 'grandfather' | 'cousin' | 'first degree relative' | 'second degree relative'
FemaleFamMem -> 'aunt'| 'grandma'  | 'grandmother' | 'cousin' | 'first degree relative' | 'second degree relative'
Adj -> 'obese' | 'overweight' | 'bulemic'
Diag1 -> 'obesity' | 'overweight' | 'bulemia' | 'cardiovascular disease' | 'cvd' | 'hypertension'
""")

grammar2 = nltk.CFG.fromstring("""
S2 -> 'No' HPhrase | HPhrase
HPhrase -> 'Family history of' Diag2 | 'History of' Diag2
Diag2 -> 'smoking' | Diag1
""")

grammar3 = nltk.CFG.fromstring("""
S3 -> 'Patient is obese'
""")

gram1list = []
for sentpieces1 in generate (grammar1, n = 100):   
    s1 = ' '.join(sentpieces1)     #makes strings of sentences in order based on the grammar
    stok1 = nltk.sent_tokenize(s1)        #converts the strings to lists of sentences
    gramlist.extend()
    gram1sents = ' '.join(gram1list)
    gram1sentslist = nltk.sent_tokenize(gram1sents)
    print(gram1sentslist)
"""

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


doctorsnotes = gram1sentslist + grammar2sentslist + grammar3sentslist
print(doctorsnotes)"""