# markov-sentance-generator

A fun little script that generates new sequences of words or single words that are statistically similar in structure to an input text file using the Markov Chain model

Usage:

`python generate.py <-w or -s> <input.txt> <length of sampling unit from text> <desired output length>`

* -w generates individual words
* -s generates sentances

e.g:

`python generate.py -s sample-data.txt 2 9`

sample output: 

`even and a half days since i saw his tall spare figure pass twice in a dark silhouette`

