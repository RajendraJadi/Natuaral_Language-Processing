
import math, collections
#Laplace Unigram Model to spell errors
class LaplaceUnigramLanguageModel:

  def __init__(self, corpus):
    #Initializing the variables and data structures that will be used for trainining model
    self.unigramLaplaceDict = collections.defaultdict(lambda:0)
    self.total_val = 0
    self.train(corpus)
    
  # Training Model..Takes corpus and trains the model based on the training data. Based on test results we will correcting the dev data  
  def train(self, corpus):
      #Get data from teh training corpus
    for wordDictionary in corpus.corpus:
        for datum in wordDictionary.data:
            word = datum.word
            #Increment the count  if teh word is found in dataum and building a unigram count that would be helpful to evaluate teh score in the scocre function.
            self.unigramLaplaceDict[word] = self.unigramLaplaceDict[word] + 1
            self.total_val += 1
#End of train fuction



# Function to calculate teh score value based on which correction is made. This score value is used for correction in spell errors.
  def score(self, wordDictionary):
    value = 0.0
    for word in wordDictionary:
        num_count = self.unigramLaplaceDict[word]
        if num_count > 0:
            #Calculate the value
            value += math.log(num_count+1)
            value -= math.log(self.total_val + len(self.unigramLaplaceDict))
        else:
            value -= math.log(self.total_val + len(self.unigramLaplaceDict))

    return value
#End of score funtion which return value to the main(spellCorrect.py)