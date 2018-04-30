import math, collections

class LaplaceBigramLanguageModel:

    
#Initialize your data structures in the constructor.
  def __init__(self, corpus):
    self.bigramLaplaceDict = collections.defaultdict(lambda:0)
    self.words = collections.defaultdict(lambda:0)
    self.total = 0
    self.train(corpus)

 # Takes a corpus and trains your language model.Compute any counts or other corpus statistics in this function
  def train(self, corpus):
    for wordDictionary in corpus.corpus:
        word_1 = '<s>'
        self.words[word_1] = self.words[word_1] + 1
        word_2 = ''
        for datum in wordDictionary.data:
            word_2 = datum.word
            self.total += 1
            self.bigramLaplaceDict[(word_1,word_2)] = self.bigramLaplaceDict[(word_1,word_2)]+1
            self.words[word_2] = self.words[word_2] + 1
            word_1 = datum.word
    word_2 = '</s>'
    self.bigramLaplaceDict[(word_1,word_2)] = self.bigramLaplaceDict[(word_1,word_2)]+1
    self.words[word_2] = self.words[word_2] + 1
 

#Takes a list of strings as argument and returns the log-probability of the sentence using your language model. Use whatever data you computed in train() here.
  def score(self, wordDictionary):
    value = 0.0
    word_1 = '<s>'
    word_2 = ''
    for word in wordDictionary:	
        word_2 = word
        count = self.bigramLaplaceDict[(word_1,word_2)]
        if count > 0:
            value += math.log(count+1)
        value -= math.log(self.words[word_1] + len(self.words))
        word_1 = word  
    word_2 = '</s>'
    count = self.bigramLaplaceDict[(word_1,word_2)]
    if count > 0:
        value += math.log(count+1)
    value -= math.log(self.words[word_1] + len(self.words))
    
    return value
