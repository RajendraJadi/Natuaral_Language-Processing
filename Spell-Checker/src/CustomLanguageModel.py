import math, collections

class CustomLanguageModel:

  def __init__(self, corpus):
#Initialize your data structures in the constructor."""
    self.unigramDict = collections.defaultdict(lambda:0)
    self.bigramDict = collections.defaultdict(lambda:0)
    self.trigramDict = collections.defaultdict(lambda:0)
    self.total = 0
    self.train(corpus)

# Takes a corpus and trains your language model. Compute any counts or other corpus statistics in this function.
  def train(self, corpus):
    for sentence in corpus.corpus:
        word_1 = '@NaN'
        word_2 = '<s>'
        word_3 = '@NaN'
        self.unigramDict[word_2] = self.unigramDict[word_2] + 1
        self.total += 1
        for datum in sentence.data:
            word_3 = datum.word
            self.total += 1
            self.bigramDict[(word_2,word_3)] = self.bigramDict[(word_2,word_3)] + 1
            self.unigramDict[word_3] = self.unigramDict[word_3] + 1
            if word_1 != '@NaN':
                self.trigramDict[(word_1,word_2,word_3)] = self.trigramDict[(word_1,word_2,word_3)] + 1
            word_1 = word_2
            word_2 = word_3	
	# end of sentence
    word_1 = word_2
    word_2 = word_3
    word_3 = '</s>'	
    self.total += 1
    self.bigramDict[(word_2,word_3)] = self.bigramDict[(word_2,word_3)] + 1
    self.unigramDict[word_3] = self.unigramDict[word_3] + 1
    self.trigramDict[(word_1,word_2,word_3)] = self.trigramDict[(word_1,word_2,word_3)] + 1


#Takes a list of strings as argument and returns the log-probability of the sentence using your language model. Use whatever data you computed in train() here.
  def score(self, sentence):
    value = 0.0
    word_1 = '@NaN'
    word_2 = '<s>'
    word_3 = '@NaN'
    count1 = self.unigramDict[word_2]
    for word in sentence:
        word_3 = word
        count3 = self.trigramDict[(word_1,word_2,word_3)]
        count2 = self.bigramDict[(word_2,word_3)]
        #Check if trigram exists
        if count3 > 0: #trigram exists
            value += math.log(count3)
            value -= math.log(self.bigramDict[(word_1,word_2)])
        ##Check if bigram exists
        elif count2 > 0: # no trigram, but bigram exists
            value += math.log(0.4) + math.log(count2)
            value -= math.log(self.unigramDict[word_2])
            #Check if there is no trigram
        else: # no trigram or bigram
            value += math.log(0.4) + math.log(self.unigramDict[word_3]+1)
            value -= math.log(self.total + (len(self.unigramDict)))
	# move everyone up
        word_1 = word_2
        word_2 = word_3

    # end of sentence case
    word_1 = word_2
    word_2 = word_3
    word_3 = '</s>'	
    
    #get unigram count
    count1 = self.unigramDict[word_3]
     #Get the number of trigrams for the given test data set
    count3 = self.trigramDict[(word_1,word_2,word_3)]
    #Get bigram count
    count2 = self.bigramDict[(word_2,word_3)]
    if count3 > 0: #trigram exists
        value += math.log(count3)
        value -= math.log(self.bigramDict[(word_2,word_3)])
    elif count2 > 0: # no trigram, but bigram exists
        value += math.log(0.4) + math.log(count2)
        value -= math.log(self.unigramDict[word_2])
    else: # no trigram or bigram
        value += math.log(0.4) + math.log(count1+1)
        value -= math.log(self.total + (len(self.unigramDict)))
    return value
