import sys
import string
import random

#return a dict containing all word level n grams and the number of times they occur within input
def get_wordNGrams(n, input):
    nGrams = {}
    n = int(n)

    for line in input:
        line = line.lower()
        line = line.translate(string.maketrans("",""), string.punctuation)
        words = line.split(" ")

        for i in range(len(words)-n+1):
                pair = tuple(words[i:i+n])
                if(not nGrams.has_key(pair)):
                    nGrams[pair] = 1
                else:
                    nGrams[pair] = nGrams[pair]+1
    return nGrams

#returns a dict containing all char level n grams and the number of times they occur within the input
def get_charNGrams(n, input):
    charNGrams = {}
    n = int(n)

    for line in input:
        line = line.lower()
        line = line.translate(string.maketrans("",""), string.punctuation)
        words = line.split(" ")

        for i in range(len(words)):
            for j in range(len(words[i])-n+1):
                pair = words[i][j:j+n]
                if(not charNGrams.has_key(pair)):
                    charNGrams[pair] = 1
                else:
                    charNGrams[pair] = charNGrams[pair]+1
    return charNGrams


#want to look at each ngram and see what comes after it
def getSentanceModel(n, input):
    model = {}
    n = int(n)

    for line in input:
        line = line.lower()
        line = line.translate(string.maketrans("",""), string.punctuation)
        line = line.strip()
        words = line.split(" ")


        for word in words:
            word = word.strip()

        for i in range(len(words)-(2*n)+1):
            nGram = tuple(words[i:i+n])
            following_nGram = tuple(words[i+n:i+(2*n)])
            if(not model.has_key(nGram)):
                model[nGram] = [following_nGram]
            else:
                model[nGram].append(following_nGram)

    return model

def getWordModel(n, input):
    model = {}
    n = int(n)

    for line in input:
        line = line.lower()
        line = line.translate(string.maketrans("",""), string.punctuation)
        line = line.strip()
        words = line.split(" ")

        for word in words:
            word = word.strip()

        for i in range(len(words)):
            for j in range(len(words[i])-2*n+1):
                nGram = words[i][j:j+n]
                following_nGram = words[i][j+n:j+2*n]

                if(not model.has_key(nGram)):
                    model[nGram] = [following_nGram]
                else:
                    model[nGram].append(following_nGram)

    return model

def returnRandomFromList(list):
    return list[random.randrange(0, len(list))]

###############################################################################

#open the text file given in the argument
f = open(sys.argv[2])
requiredLength = int(sys.argv[4])

#if the sentance generation flag is chosen
if(sys.argv[1] == '-s'):
    model = getSentanceModel(sys.argv[3], f)
    key = returnRandomFromList(model.keys())
    for i in range(requiredLength):

        while (not model.has_key(key)):
            key = returnRandomFromList(model.keys())

        nextPhrase = returnRandomFromList(model[key])
        while(len(nextPhrase) == 0):
            nextPhrase = returnRandomFromList(model[key])

        for element in nextPhrase:
            print element,

        key = nextPhrase

#if the word generation flag is chosen
if(sys.argv[1] == '-w'):
    model = getWordModel(sys.argv[3], f)
    key = returnRandomFromList(model.keys())

    for i in range(requiredLength):

        while (not model.has_key(key)):
            key = returnRandomFromList(model.keys())

        nextPhrase = returnRandomFromList(model[key])
        while(len(nextPhrase) == 0):
            nextPhrase = returnRandomFromList(model[key])

        for element in nextPhrase:
            sys.stdout.write(element),

        key = nextPhrase

    print ''
