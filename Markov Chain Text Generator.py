# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:42:18 2016

@author: samanthacheng
"""

import nltk.data
import random
from collections import defaultdict
from nltk import word_tokenize

class TextGenerator:
    
    def __init__(self):
        self.next_states = defaultdict(set)

    def create_ngrams(self,text,n):
        f = open(text, 'r', encoding = 'utf8')
        raw = f.read()
        words = word_tokenize(raw)        
        return zip(*[words[i:] for i in range(n)])

    def make_text(self, current_phrase = None):
        text = []
        if current_phrase == '\\':
            return text
        if current_phrase == None:
            text.extend(current_phrase)
            next_phrase = random.sample(self.next_states[current_phrase],1)
            ' ' .join(current_phrase,next_phrase)
            current_phrase = next_phrase[0]
        else:
            next_phrase = random.sample(self.next_states[current_phrase],1)
            ' ' .join(current_phrase,next_phrase)                
            current_phrase = next_phrase[0]
        return text

text_generator = TextGenerator()

text_generator.create_ngrams('IceCream.txt', 3)
print(text_generator.make_text('he'))


'''
      def create_chains(self, text, n): 
        f = open(text, 'r', encoding = 'utf8')
        raw = f.read()
        words = word_tokenize(raw)
        for word in words:
            for x in range(len(words) - n + 1): 
                if x == len(words) - n: self.next_states[tuple(words[x:])].add('\\')
                else: self.next_states[tuple(words[x:x+n])].add(words[x+n])
                
      
      def make_text2 (self, current_phrase = None):
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