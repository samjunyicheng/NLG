# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:25:17 2016

@author: samanthacheng
"""

import nltk
from nltk.parse.generate import generate
import random

#PROBLEM

grammar1 = nltk.CFG.fromstring("""
S -> Age 'patient presents with' Diag | Diag | Age 'with' Diag
Age -> '65 yo' | '50 yo' | '48 yo' | '78 yo' | 62 'yo' | '80 yo' | '83 yo' | '72 yo' | '76 yo' | '81 yo' | '63 yo'
Diag -> 'morbid obesity' | 'cvd' | 'hypertension' | 'diabetes' | 'coronary artery disease' | 'congenital heart defect' | 'gallbladder disease' | 'gallstones' | 'gout'
""")

#PAST MEDICAL HISTORY

grammar2a = nltk.CFG.fromstring("""
S -> NP VP
NP -> FPatientName | 'the patient'
FPatientName -> 'Lisa' | 'Shayn' | 'Annie' | 'Tammy' | 'Annette' | 'Jane' | 'Alice' | 'Abigail' | 'Kelly' | 'April' | 'Jenna' | 'Beatrice' | 'Leslie' | 'Alicia' | 'Katelyn' | 'Sandy' | 'Allison'
VP -> 'was previously seen for' Diag | 'was previously diagnosed with' Diag
Diag -> 'high bp' | 'diabetes' | 'hypertension' | 'high cholesterol'
""")

grammar2b = nltk.CFG.fromstring("""
S -> NP VP
NP -> MPatientName | 'the patient'
MPatientName -> 'Thomas' | 'Joe' | 'George' | 'Kyle' | 'Connor' | 'Julian' | 'Christopher' | 'Riley' | 'Andrew' | 'Arthur' | 'Steve' | 'Jeff' | 'Casey' | 'Lawrence' | 'Greg' | 'Robert' | 'Michael' | 'Eric' | 'Jared' | 'Evan' | 'Bill'
VP -> 'was previously seen for' Diag | 'was previously diagnosed with' Diag
Diag -> 'high bp' | 'diabetes' | 'hypertension' | 'high cholesterol'
""")

grammar3 = nltk.CFG.fromstring("""
S -> Sent
Sent -> 'Vital signs show increased risk' | 'Prior conditions were well-managed' | 'Patient was in good health until recently' | 'labs unremarkable'
""")

#FAMILY HISTORY

grammar4 = nltk.CFG.fromstring("""
Sent -> 'No known risks in family history' | 'Noncontributory' | 'No family history of' Diag | 'Strong family history of' Diag | 'None on file' | 'Strong positive family history for' Diag
Diag -> 'cancer' | 'heart disease' | 'obesity' | 'lung cancer' | 'bladder cancer' | 'premature cad'
""")

grammar5 = nltk.CFG.fromstring("""
S -> Sent
Sent -> 'Family history shows some risk' | 'Doesn't know about siblings' healths' | 'Children alive and well'
""")

grammar6a = nltk.PCFG.fromstring("""
S -> SingNP SingVP [0.25] | PluNP PluVP [0.25] | PluNPDegRel PluVP [0.25] | SingNPDegRel SingVP [0.25]
SingNP -> MomDad [0.2] | MotherFather [0.3] | MaleFamMem [0.1] | FemaleFamMem [0.1] | FamSide MaleFamMem [0.05]| FamSide FemaleFamMem [0.05] | MalePropN [0.05]| FemalePropN [0.05]| MaleFamMem MalePropN [0.05]| FemaleFamMem FemalePropN [0.05]
PluNP -> SingNP Conj SingNP [0.333] | SingNP Comma SingNP Conj SingNP [0.333] | SingnP SingNP SingNP [0.333]
SingNPDegRel -> DegreeRel [1]
PluNPDegRel -> DegreeRel Conj DegreeRel [1]
Conj -> 'and' [1]
Comma -> ',' [1]
SingVP -> 'is' Adj [0.1] | 'has' Diag [0.1] | 'was' Adj [0.1] | 'had' Diag [0.1] | 'was diagnosed with' Diag [0.1] | 'died of' Diag [0.1] | 'suffered from' Diag [0.1] | 'suffers from' Diag [0.1] | 'smokes' [0.1] | 'smoked' [0.1] 
PluVP -> 'are' Adj [0.1] | 'have' Diag [0.1] | 'were' Adj [0.1] | 'had' Diag [0.1] | 'were diagnosed with' Diag [0.1] | 'died of' Diag [0.1] | 'suffered from' Diag [0.1] | 'suffer from' Diag [0.1] | 'smoke' [0.1] | 'smoked' [0.1] 
MomDad -> 'Mom' [0.5] |'Dad' [0.5]
MotherFather -> 'Mother' [0.5] | 'Father' [0.5]
PropN -> 'Vishal' [0.1] | 'Marco' [0.1] | 'Tony' [0.1] | 'Zach' [0.1] | 'Willi' [0.1] | 'Eric' [0.1] | 'Alex' [0.1] | 'Jack' [0.1] | 'George' [0.1] | 'James' [0.1] 
FemalePropN -> 'Sophia' [0.1] | 'Sharon' [0.1] | 'Sana' [0.1] | 'Rona' [0.1] | 'Sarah' [0.1] | 'Jamie' [0.1] | 'Jane' [0.1] | 'Allison' [0.1] | 'Elizabeth' [0.1] | 'Jennifer' [0.1] 
FamSide -> 'maternal' [0.5] | 'paternal' [0.5] 
MaleFamMem ->  'uncle' [0.25] | 'grandpa' [0.25] | 'grandfather' [0.25] | 'cousin' [0.25]
DegreeRel -> 'first degree relative' [0.5] | 'second degree relative' [0.5]
FemaleFamMem -> 'aunt' [0.25] | 'grandma'  [0.25] | 'grandmother' [0.25] | 'cousin' [0.25]
Adj -> 'obese' [0.5] | 'overweight' [0.5]
Diag1 -> ChronicDiag1 [0.333] | AcuteDiag1 [0.333] | AcuteDiag1 'at' Age [0.333]
ChronicDiag1 ->'obesity' [0.1] | 'overweight' [0.1] | 'cardiovascular disease' [0.1] | 'cvd' [0.1] | 'hypertension' [0.1] | 'cad' [0.1] | 'coronary artery disease' [0.1] | 'osteoarthritis' [0.1] | 'sleep apnea' [0.1] | 'gall bladder disease' [0.1] 
AcuteDiag2 -> 'stroke' [0.333] | 'heart attack' [0.333] | 'MI' [0.333]
Age -> '70' [0.25] | '82' [0.25] | '74' [0.25] | 'mid 70s' [0.25]
""")

grammar6b = nltk.PCFG.fromstring("""
S -> Num Siblings 'alive and well,' FamMem 'deceased' [0.25] | Num Siblings 'alive and well' [0.25] | 1 Sibling 'alive and well' [0.25] | Num Siblings 'doing well' [0.25]
Num ->  '2' [0.55] | '3' [0.35] |'4' [0.1]
Sibling -> 'sibling' [0.333] | 'sister' [0.333] |'brother' [0.333]
Siblings -> 'siblings' [0.333] | 'sisters' [0.333] | 'brothers' [0.333]
FamMem -> 'father' [0.333] | 'mother' [0.333] | 'father and mother' [0.333]
""")

grammar6c = nltk.CFG.fromstring("""
S -> Mother 'lived to' Age ', had' Diag ', Father died at' Age | Father 'lived to' Age ', had' Diag ', Mother died at' Age
Age -> '80' | '85' | '73' | '90' | '92' | '95' | '83' | '88' | '78' | '96' | '81' | '87'
Diag -> 'lung cancer' | 'cad' | 'heart disease' | 'MI' | 'cancer' | 'stroke'
""")

grammar6d = nltk.CFG.fromstring("""
S -> 'On' FamSide 'side, there is history of' Diag
FamSide -> 'mothers' | 'fathers' | 'maternal' | 'paternal'
Diag -> 'hypertension' | 'diabetes' | 'high bp' | 'obesity' | 'lung cancer' | 'cancer' | 'metabolic disease' | 'arthritis'
""")

grammar6e = nltk.CFG.fromstring("""
S -> FamMem 'with' Diag | FamMem and FamMem 'with' Diag
FamMem -> 'Mother' | 'Father' | 'Gm' | 'Gf' | 'Uncle' | 'Aunt'
Diag -> 'diabetes' | 'hypertension' | 'lung cancer' | 'obesity' | 'gout' | 'osteoarthritis' | 'stroke'
""")

#SOCIAL HISTORY

grammar7 = nltk.CFG.fromstring("""
S -> 'Patient is' Employstatus | 'She was' Jobs | 'She was' Jobs 'for' Years | 'living independently prior to hospitalization' | 'worked in' JobLocation
Employstatus -> Unemployed | Jobs | 'retired but previously' Jobs
Unemployed -> 'recently unemployed' | 'unemployed'
Jobs -> 'a clinical psychologist' | 'a pediatrician' | 'a software engineer' | 'a middle school science teacher' | 'a pharmaceutical drug salesman' | 'a teacher' | 'a businessman' | 'a construction worker' | 'a real estate analyst' | 'an acutary' | 'an office secretary' | 'a nurse' | 'a lawyer' | 'a customer service representative' | 'an elementary school vice principal'
Years -> '20 years' | '30 years'
JobLocation -> 'a printing factory' | 'a doctors office' | 'a water plant' | 'a PECO plant' | 'a textiles factory' | 'furniture upholstery business'
""")

grammar8a = nltk.CFG.fromstring("""
S -> 'She is' MaritalStatus | MaritalStatus | 'lives with health care aide' | 'lives with health care aide,' DaughSon 'very involved in care' | MaritalStatus NumChildren
DaugSon -> 'daughter' | 'son'
MaritalStatus -> 'single and lives' FamMem | 'married for' Years 'to' Occupation 'and lives with him' | 'divorced' | 'married to' Occupation 'and lives with him' | 'married to retired' Occupation 'and lives with him' | 'married' | 'married and lives with spouse' | 'married, no children' | 'married, 2 children' | 'married, one son'
FamMem -> 'with her sister' | 'with her mother' | 'with her parents' | 'by herself' |'alone'
Years -> '45 years' | '50 years' | '10 years'
Occupation -> 'an elementary school teacher' | 'a clinical psychologist' | 'a firefigher' | 'an eminent pediatriac neurosurgeon' | 'an oncologist' | 'a social worker' | 'a health inspector' | 'a real estate agent' | 'a journalist' | 'a physical therapist'| 'a retail salesperson' | 'a truck driver' | 'a customer service rep' | 'a Microsoft developer' | 'flight attendant on American Airlines'
NumChildren -> ' 2 children' | '2 kids' | '1 son' | ' 3 kids' | '2 children'
""")

grammar8b = nltk.CFG.fromstring("""
S -> 'He is' MaritalStatus | MaritalStatus | 'He has' Number 'children live nearby' | MaritalStatus ',' NumChildren
MaritalStatus -> ' single and lives' FamMem | 'married to' Occupation 'and lives with spouse' | 'divorced and lives alone' | 'divorced' | 'married' | 'married and lives with spouse'
FamMem -> 'with his brother' | 'with a friend' | 'with his parents' | 'by himself'
Occupation -> 'a college professor' | 'a finacial analyst' | 'a restaurant hostess' | 'an ent surgeon' | 'a police officer' | 'a nurse' | 'a pilot' | 'a maintenance worker'
Number -> '2' | '3'
NumChildren -> '1 daughter' | 'daughter and son' | '3 kids' | '2 sons' | ' 2 children'
""")

grammar8aa = nltk.CFG.fromstring("""
S -> 'lives with husband'
""")

grammar8bb = nltk.CFG.fromstring("""
S -> 'lives with wife'
""")

grammar9 = nltk.CFG.fromstring("""
S -> 'Patient' DrugUse
DrugUse -> 'denies recreational drug use' | 'admits occasional use of illict drugs' | 'has not used illict drugs for 10 years' | 'Used recreational drugs 20 years ago, but has not since' | ' no drug use' | 'no illicit drugs' | 'no illicits'
""")

grammar10 = nltk.CFG.fromstring("""
S -> 'Patient is a prior smoker but hasnt smoked in' Years | 'Patient never smoked' | 'Patient smokes occasionally' | 'smoked for a year and a half' Years 'ago, but has stopped' | 'smoked infrequently in the past and has stopped for several years now' | 'patient is a nonsmoker' | 'prior tobacco usage 20 years ago' | 'no tobacco use' | 'quit' | 'former smoker'
Years -> '5 years' | '10 years' | '20 years'
""")

grammar11 = nltk.CFG.fromstring("""
S -> 'No known alcohol use' | 'Drinks casually-' HowCasual | 'Previous alcohol use-' AlcoholUse | 'Denies alcohol use' | Bottle of wine per week | 'has history of alocholism, but quit' Years 'ago' | 'very rare alcohol use'
HowCasual -> 'one glass of wine per week' | 'one beer per week' | 'drinks one glass of wine with dinner sometimes'
AlcoholUse -> '1-2x per week x5 years' | 'a drink per day 3 years ago, but has since quit' | 'a social drink now and then' | 'a 6-pack over the course of two days, but quit abruptly'
Years -> '20 years' | '10 years' | '15 years' | '8 years'
""")

grammar12 = nltk.CFG.fromstring("""
S -> 'Denies alcohol and drug use, denies smoking' | 'No alcohol nor drug use, no smoking history' | 'No drug use or smoking history' | 'Rarely drinks, only on certain social occasions' | 'No tobacco, alcohol, and illicit drug use'
""")

grammar13 = nltk.CFG.fromstring("""
S -> 'Tobacco use: Never, Alcohol Use: No, Drug Use: No' | Type 'use: quit' Years 'ago'
Type -> 'Tobacco' | 'Alcohol' | 'Drug'
Years -> '5 years' | '4 yrs' | '10yrs' |'15 years'
""")

grammar14 = nltk.CFG.fromstring("""
S -> 'History of' Abuse
Abuse -> 'polysubstance abuse including' Drugs | 'cocaine abuse' | 'alcohol abuse' | 'marijuana and tobacoo abuse' | 'marijuana abuse' | 'suicide attempts'
Drugs -> 'cocaine' | 'heroin' | 'intranasal and intravenous heroin'
Drugs -> Drugs | Drugs 'and' Drugs
""")



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

list = ['mother' , 'father', 'aunt' , 'uncle']
def grammar_notes(grammar, n, m):
    """ Generate n setnences from a particular grammar. Randomize sentences generated
    and select first m sentences.."""    
    gramfinallist = [nltk.sent_tokenize(' '.join(sentpieces)) for sentpieces in generate(grammar, n = n)]
    randomize(gramfinallist)
    return gramfinallist[:m]

"""words = nltk.word_tokenize(gramfinallist)
    if gramfinallist.count(words) is 0:
        del sent"""
"""if a sentence contains a name or family member that is already present in the set, remove the sentence"""
  
def make_notes(biglist):
    """Using a list of all the notes to be included, print output on patienthistories file.
    Leave an empty line between each set of doctors' notes."""
    setdoctorsnotes = []
    setdoctorsnotes.extend(biglist)
    outfile.write(noquotations(nobrackets(','.join(map(str,setdoctorsnotes)).lower())))
    outfile.write('\n\n')
    return nobrackets(noquotations(str(setdoctorsnotes).lower()))


outfile = open('CFGpatienthistories2.txt', 'w')
outfile.write('Patient History Notes \n\n')


for F_notes in range(4):

    print('\n\n')
    outfile.write('\n\n')
    
    gram1 = grammar_notes(grammar1, n = 10000, m = 1)
    print('PROBLEM \n')      
    outfile.write('PROBLEM \n')
    print(make_notes(gram1))

    gram2a = grammar_notes(grammar2a, n = 500, m = 1)
    gram3 = grammar_notes(grammar3, n = 10, m = 1)
    print('PAST MEDICAL HISTORY\n')    
    outfile.write('PAST MEDICAL HISTORY \n')
    gram_FFamHistory = gram2a + gram3
    print(make_notes(gram_FFamHistory))
    
    gram4 = grammar_notes(grammar4, n = 20, m = 1 )
    gram5 = grammar_notes(grammar5, n = 100, m = 1)
    gram6a = grammar_notes(grammar6a, n = 5000, m = 3)
    gram6b = grammar_notes(grammar6b, n = 1000, m = 1)
    gram6c = grammar_notes(grammar6c, n = 100, m = 1)
    gram6d = grammar_notes(grammar6d, n = 100, m = 1)
    gram6e = grammar_notes(grammar6e, n = 50, m = 1)
    gram6 = random.sample([gram6a] + [gram6b] + [gram6c] + [gram6d] +[gram6e], 1)    
    famhistgrams = [gram5 + gram6]
    YNFamHistory = random.sample(gram4 + famhistgrams + famhistgrams,1)
    print('FAMILY HISTORY \n')    
    outfile.write('FAMILY HISTORY \n')
    print(make_notes(YNFamHistory))
    
    gram7 = grammar_notes(grammar7, n = 30, m = 1 )
    gram8a = grammar_notes(grammar8a, n = 500, m = 1)
    gram8aa = grammar_notes(grammar8aa, n = 50, m = 1)
    gram8 = random.sample(gram8a + gram8aa, 1)
    gram9 = grammar_notes(grammar9, n = 20, m = 1)    
    gram10 = grammar_notes(grammar10, n = 50, m = 1)
    gram11 = grammar_notes(grammar11, n = 50, m =1)
    gram12 = grammar_notes(grammar12, n = 50, m = 1)
    gram13 = grammar_notes(grammar13, n = 50 , m = 1)
    gram14 = grammar_notes(grammar14, n = 100, m = 1)
    g9_10 = [gram9 + gram10]
    g9_10_11 = [gram9 + gram10 + gram11]
    g10_9_11 = [gram10 + gram9 + gram11]
    g11_10 = [gram11 + gram10]
    YNUse = random.sample(g9_10 + g9_10_11 + g10_9_11 + g11_10 + gram12 + gram13 + gram14, 1)
    print('SOCIAL HISTORY \n')    
    outfile.write('SOCIAL HISTORY\n')
    gram_FSocialHist = gram7 + gram8 + YNUse
    print(make_notes(gram_FSocialHist))


for M_notes in range(4):

    print('\n\n')
    outfile.write('\n\n')

    gram1 = grammar_notes(grammar1, n = 10000, m = 1)
    outfile.write('PROBLEM \n')
    print('PROBLEM \n')    
    print(make_notes(gram1))

    gram2b = grammar_notes(grammar2b, n = 500, m = 1)
    gram3 = grammar_notes(grammar3, n = 10, m = 1)    
    print('PAST MEDICAL HISTORY \n')    
    outfile.write('PAST MEDICAL HISTORY \n')
    gram_MFamHistory = gram2b + gram3
    print(make_notes(gram_MFamHistory)) 
    
    gram4 = grammar_notes(grammar4, n = 20, m = 1 )
    gram5 = grammar_notes(grammar5, n = 100, m = 1)
    gram6a = grammar_notes(grammar6a, n = 5000, m = 3)
    gram6b = grammar_notes(grammar6b, n = 1000, m = 1)
    gram6c = grammar_notes(grammar6c, n = 100, m = 1)
    gram6d = grammar_notes(grammar6d, n = 100, m = 1)
    gram6e = grammar_notes(grammar6e, n = 50, m = 1)
    gram6 = random.sample([gram6a] + [gram6b] + [gram6c] + [gram6d] + [gram6e], 1)    
    famhistgrams = [gram5 + gram6]
    YNFamHistory = random.sample(gram4 + famhistgrams + famhistgrams,1)
    print('FAMILY HISTORY \n')    
    outfile.write('FAMILY HISTORY \n')
    print(make_notes(YNFamHistory))    
    
    
    gram7 = grammar_notes(grammar7, n = 30, m = 1 )
    gram8b = grammar_notes(grammar8b, n = 500, m = 1)
    gram8bb = grammar_notes(grammar8aa, n = 50, m = 1)
    gram8 = random.sample(gram8a + gram8aa, 1)
    gram9 = grammar_notes(grammar9, n = 20, m = 1)    
    gram10 = grammar_notes(grammar10, n = 50, m = 1)
    gram11 = grammar_notes(grammar11, n = 50, m =1)
    gram12 = grammar_notes(grammar12, n = 50, m = 1)
    gram13 = grammar_notes(grammar13, n = 50 , m = 1)
    gram14 = grammar_notes(grammar14, n = 100, m = 1)
    g9_10 = [gram9 + gram10]
    g9_10_11 = [gram9 + gram10 + gram11]
    g10_9_11 = [gram10 + gram9 + gram11]
    g11_10 = [gram11 + gram10]
    YNUse = random.sample(g9_10 + g9_10_11 + g10_9_11 + g11_10 + gram12 + gram13 + gram14, 1)
    print('SOCIAL HISTORY \n')    
    outfile.write('SOCIAL HISTORY\n')
    gram_MSocialHist = gram7 + gram8 + YNUse
    print(make_notes(gram_MSocialHist))


for F_notes in range(1):

    print('\n\n')
    outfile.write('\n\n')

    gram1 = grammar_notes(grammar1, n = 10000, m = 1)
    print('PROBLEM \n')      
    outfile.write('PROBLEM \n')
    print(make_notes(gram1))

    gram2a = grammar_notes(grammar2a, n = 500, m = 1)
    gram3 = grammar_notes(grammar3, n = 10, m = 1)
    print('PAST MEDICAL HISTORY \n')    
    outfile.write('PAST MEDICAL HISTORY \n')
    gram_FFamHistory = gram2a + gram3 + YNFamHistory
    print(make_notes(gram_FFamHistory))
    
    
    gram4 = grammar_notes(grammar4, n = 20, m = 1 )
    gram5 = grammar_notes(grammar5, n = 100, m = 1)
    gram6a = grammar_notes(grammar6a, n = 5000, m = 3)
    gram6b = grammar_notes(grammar6b, n = 1000, m = 1)
    gram6c = grammar_notes(grammar6c, n = 100, m = 1)
    gram6d = grammar_notes(grammar6d, n = 100, m = 1)
    gram6e = grammar_notes(grammar6e, n = 50, m = 1)
    gram6 = random.sample([gram6a] + [gram6b] + [gram6c] + [gram6d] + [gram6e], 1)    
    famhistgrams = [gram5 + gram6]
    YNFamHistory = random.sample(gram4 + famhistgrams + famhistgrams,1)
    print('FAMILY HISTORY \n')    
    outfile.write('FAMILY HISTORY \n')
    print(make_notes(YNFamHistory))    
    
    gram7 = grammar_notes(grammar7, n = 30, m = 1 )
    gram8a = grammar_notes(grammar8a, n = 500, m = 1)
    gram8aa = grammar_notes(grammar8aa, n = 50, m = 1)
    gram8 = random.sample(gram8a + gram8aa, 1)
    print('SOCIAL HISTORY \n')    
    outfile.write('SOCIAL HISTORY\n')
    gram_FSocialHist = gram7 + gram8
    print(make_notes(gram_FSocialHist))
    
    
for M_notes in range(1):

    print('\n\n')
    outfile.write('\n\n')    
    
    gram1 = grammar_notes(grammar1, n = 10000, m = 1)
    outfile.write('PROBLEM \n')
    print('PROBLEM \n')    
    print(make_notes(gram1))

    gram2b = grammar_notes(grammar2b, n = 500, m = 1)
    gram3 = grammar_notes(grammar3, n = 10, m = 1)    
    print('PAST MEDICAL HISTORY \n')    
    outfile.write('PAST MEDICAL HISTORY \n')
    gram_MFamHistory = gram2b + gram3
    print(make_notes(gram_MFamHistory)) 
    
    gram4 = grammar_notes(grammar4, n = 20, m = 1 )
    gram5 = grammar_notes(grammar5, n = 100, m = 1)
    gram6a = grammar_notes(grammar6a, n = 5000, m = 3)
    gram6b = grammar_notes(grammar6b, n = 1000, m = 1)
    gram6c = grammar_notes(grammar6c, n = 100, m = 1)
    gram6d = grammar_notes(grammar6d, n = 100, m = 1)
    gram6e = grammar_notes(grammar6e, n = 50, m = 1)
    gram6 = random.sample([gram6a] + [gram6b] + [gram6c] + [gram6d] + [gram6e], 1)    
    famhistgrams = [gram5 + gram6]
    YNFamHistory = random.sample(gram4 + famhistgrams + famhistgrams,1)
    print('FAMILY HISTORY \n')    
    outfile.write('FAMILY HISTORY \n')
    print(make_notes(YNFamHistory))    
    
    gram7 = grammar_notes(grammar7, n = 30, m = 1 )
    gram8b = grammar_notes(grammar8b, n = 500, m = 1)
    gram8bb = grammar_notes(grammar8aa, n = 50, m = 1)
    gram8 = random.sample(gram8a + gram8aa, 1)
    print('SOCIAL HISTORY \n')    
    outfile.write('SOCIAL HISTORY\n')
    gram_FSocialHist = gram7 + gram8
    print(make_notes(gram_FSocialHist))


outfile.close()
