#coding: utf-8
# import speech_recognition as sr 
# import nltk
from gensim.models import Word2Vec
import gensim
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"

# #getting the audio in variable
# recognize=sr.Recognizer()

# #source is microphone
# with sr.Microphone() as source:
# 	audio = recognize.listen(source)
	
# #try:
# 	#converting the speech to text and encoding the characters with UTF-8
# 	text = recognize.recognize_google(audio).encode('utf-8')
# 	#it converts the text to token of list
# 	tokens = nltk.word_tokenize(text)
# 	#it marks the words with verb,noun,adverb etc type is tuple
# 	# tagged = nltk.pos_tag(tokens)
tokens=[['Neeraj','Boy'],['Sarwan','is'],['good','boy']] 
	# creating a training model from given tokens
TrainingModel = gensim.models.Word2Vec(tokens, min_count=1,size=300,workers=4)

print(TrainingModel.similarity('boy','Neeraj'))

#except Exception as e:
#	print('something fishy')
