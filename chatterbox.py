import wikipedia
import re
import spacy

regex = "\(.*\)|\s-\s.*"

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
for token in doc:
    if token.pos_ == "PROPN":
    	mystring = wikipedia.summary(token.text,sentences=3)
    	result = re.sub(regex,"",mystring)
    	print(result)
