# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:42:18 2016

@author: samanthacheng
"""

import random

'''Note- the generator should use the prior two words to select the next word, not use the current word to select the next word.'''

class MarkovChain:
    
    def __init__(self):
        self.memory = {}

    def _learn_key(self, key, value):
        if key not in self.memory:
            self.memory[key] = []
        self.memory[key].extend(value)        
        
    def learn(self, text):
        tokens = text.split(" ")
        trigrams = [(tokens[i], tokens[i + 1], tokens[i + 2]) for i in range(0, len(tokens) - 2)]
        for trigram in trigrams:
            self._learn_key(trigram[0], (trigram[1], trigram[2]))

    def _next(self, current_state):
        next_possible = self.memory.get(current_state)
        if not next_possible:
            next_possible = self.memory.keys()
        return random.sample(next_possible, 1)[0]

    def generate_babble(self, amount, state=' '):
        if not amount:
            return state
        next_word = self._next(state)
        return state + ' ' + self.generate_babble(amount - 1, next_word.lower())


mc = MarkovChain()


f = open('SeniorThesis.txt', 'rU', encoding = 'utf8')
raw = f.read()
mc.learn(raw)
'''print(mc.memory)'''

outfile = open('Markovpatienthistories.txt', 'w')
outfile.write('Markov Chain Text \n\n')

for Markov_Notes in range(3):
    
    newtext = mc.generate_babble(50).replace("\n", "")
    print(newtext)   
    outfile.write(newtext)
    outfile.write('\n\n')


#---------------------------NLTK N-Gram Text Generation-------------------------------------------#
'''

import nltk
from nltk import word_tokenize
from nltk import bigrams
import heapq

def randomize(list):
    """Shuffle items in a list."""    
    random.shuffle(list)
    return list

def generate_model(cfdist, word, num = 30):
    for i in range(num):
        print(word, end = ' ')
        x = randomize(heapq.nlargest(10, cfdist, key = cfdist.get))[0]
        word = x

f = open('IceCream.txt', 'r', encoding = 'utf8')
raw = f.read()
tokens = word_tokenize(raw)
bigrams = list(nltk.bigrams(tokens))
cfd = nltk.ConditionalFreqDist(bigrams)
print(cfd['they'])
generate_model(cfd, 'they')





def generate_model2(cfdist , word, num = 30):
    for i in range(num):
        print(word, end = ' ')
        word = cfdist[word].max()


f = open('SeniorThesis.txt', 'r', encoding = 'utf8')
raw = f.read()
tokens = word_tokenize(raw)
bigrams = list(nltk.bigrams(tokens))
cfd = nltk.ConditionalFreqDist(bigrams)
print(cfd['he'])
generate_model2(cfd, 'he')
'''
#----------------------------What is Dis------------------------------------------------------------#
'''
      def create_chains(self, text, n): 
        f = open(text, 'r', encoding = 'utf8')
        raw = f.read()
        words = word_tokenize(raw)
        for word in words:
            for x in range(len(words) - n + 1): 
                if x == len(words) - n: self.next_states[tuple(words[x:])].add('\\')
                else: self.next_states[tuple(words[x:x+n])].add(words[x+n])
                
      
      def make_text2 (self, current_phrase = No ne):
        if current_phrase == None:
            current_phrase = random.choice(self.next_states.keys())
            text.append(current_phrase)
            next_phrase = random.sample(self.next_states[current_phrase],1)
            current_phrase = next_phrase[0]
            ' '.join(current_phrase, next_phrase)
        if current_phrase == '\\':
            print 
        else:
            next_phrase = random.sample(self.next_states[current_phrase],1)
            current_phrase = next_phrase[0]
            ' '.join(current_phrase, next_phrase))

    
    
    def make_text(self, current_phrase=None, acc=None):
        if current_phrase == None:
            acc = ""
            current_phrase = random.choice(self.next_states.keys())
            next_phrase = random.sample(self.next_states[current_phrase], 1)[0]
            acc += ' '.join(list(current_phrase)) + ' ' + next_phrase
        if current_phrase[len(current_phrase) - 1] == '\\': 
            print(acc); return
        else:
            next_phrase = random.sample(self.next_states[current_phrase], 1)[0]
            acc += ' ' + next_phrase
        current_phrase = tuple([x for x in current_phrase[1:]] + [next_phrase])
        self.make_text(current_phrase, acc)
'''

'''

import pickle
  
fh = open("IceCream.txt", "r", encoding = 'utf8')
  
chain = {}
  
def generate_trigram(words):
    if len(words) < 3:
        return
    for i in range(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])
  
for line in fh.readlines():
    words = line.split()
    for word1, word2, word3 in generate_trigram(words):
        key = (word1, word2)
        if key in chain:
            chain[key].append(word3)
        else:
            chain[key] = [word3]
  
pickle.dump(chain, open("chain.p", "wb" ))
  
chain = pickle.load(open("chain.p", "rb"))
  
new_review = []
sword1 = "BEGIN"
sword2 = "NOW"
  
while True:
    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
    if sword2 == "END":
        break
    new_review.append(sword2)
  
print(' '.join(new_review))

from nltk import word_tokenize
import Markov

f = open('SeniorThesis.txt', 'r', encoding = 'utf8')
raw = f.read()
tokens = word_tokenize(raw)

model = Markov.build_model(tokens, 3)
print(Markov.generate(model, 3))

'''