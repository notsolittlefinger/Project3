# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
## only thing changing are probabiliteis
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
import nltk
import random
from nltk.book import text2

 #No need to tokenize in hw. just slice [:150]
#iterate create string of text
string = ""

tokens = text2[:150]
for word in tokens:
	string = string + " " + word

print ("**Original Text**")
print (string)
#print (tokens)

tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB": "an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.10,"VB":.10,"JJ":.10, "RB":.10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("**Final Text**")
print ("".join(final_words))

##

print("\n\nEND*******")
