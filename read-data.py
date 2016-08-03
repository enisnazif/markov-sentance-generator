import sys
import string

#What I want to do is construct a function that looks at all the words, and finds the most common two character sequences



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


################################################################################


#open the text file given in the argument
f = open(sys.argv[1])

#get ngrams and convert the dict to a list
nGrams = get_charNGrams(sys.argv[2], f).items()
get_charNGrams(sys.argv[2], f)

#print out each element in the list
for i in nGrams:
    if(i[1] >= int(sys.argv[3])):
        print i
