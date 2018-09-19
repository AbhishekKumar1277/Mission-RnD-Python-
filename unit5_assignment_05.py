__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
# from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
	pass
	result=''
	final_result=''
	i=0
	if 'either' in sentence and 'or' in sentence and sentence[0:6]!='either':
		while i<len(sentence):
			if sentence[i]==' ':
				result+=' '
				i+=1
			elif sentence[i-1]==' ' and sentence[i]=='e' and sentence[i+1]=='i' and sentence[i+2]=='t' and sentence[i+3]=='h' and sentence[i+4]=='e' and sentence[i+5]=='r':
				i+=7         
			elif sentence[i-1]==' ' and sentence[i]=='o' and sentence[i+1]=='r':
				break
			else:
				result+=sentence[i]
				i+=1  
		if 'neither' in sentence:
			return result
		else:			 	     
			for j in range(0,len(result)-1):
				final_result+=result[j] 
			return final_result       
	else:
		return sentence  


def test_prune_either_or_student():
	pass
	assert 'we could go to a movie'==prune_either_or('we could either go to a movie or a hotel')
	assert 'we could go to a beach'==prune_either_or('we could either go to a beach or we can have a party')
	assert 'we could  go to a beach else we can have a party'==prune_either_or('we could  go to a beach else we can have a party')
	assert 'we can go either of the two beaches'==prune_either_or('we can go either of the two beaches')
	assert 'It is neither here nor there'==prune_either_or('It is neither here nor there')



# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
	servertests = pytest.importorskip("unit5_server_tests")
	servertests.test_prune_either_or(prune_either_or)