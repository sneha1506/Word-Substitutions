#!/usr/bin/env python2.7
# Author : Sneha GUNDA

"""
Usage: The Usage of this code is simple. You can either call the 
file from cmd line or can import the file as module. 

Ex: 
1) Call from cmdline :
$ python word_substitution.py

returns: 
  output in a outfile 'wordlist-substituted.txt' in working directory
  
2) import the file as module in python prompt:

>>> from word_substitution import *
>>> substitute('crypt')
['cryp7', 'cryp+']
>>> substitute('madman')
['m@dm@n', 'm4dm4n']
>>> substitute('random')
['r$om', 'rand0m', 'r4ndom', 'r@ndom']
>>> substitute('glyph')
[]
>>>

"""

import sys
from string import Template

#create an output file to store the wordlist after substitution
out_file = open('wordlist-substituted.txt','w')

#declare a global substitution dictionary
substitute_dict = {'a':['4','@'],'and':['&'],'e':['3'],'f':['ph'],
	'i':['!'],'o':['0'],'s':['5','$'],'t':['7','+']}

def substitute(text, s_dict = substitute_dict):
	""" this function reads word & try to replace the character 
	with predefined characters
	"""
	
	stack = []
	if 'and' in text:
		_text = text.replace('and','$')
		stack.append(_text.strip())

	
	for word in text.strip():
		if word in s_dict.keys():
			'''Check for word is in substitute_dict keys'''
			if word in s_dict[word]:
				'''exit loop if the values of particular 
				key is present in text'''
				break
			for v in s_dict[word]:
				'''Loop thru text & replace characters with 
				predefined values from substitute_dict'''
				_text = text.replace(word,v)
				
				#Append the substituted words to list stack 
				stack.append(_text.strip())
		
# eliminate the duplicate entries in list	
	stack = list(set(stack))

	if stack: 
		'''Return empty list [] if word has no match'''
		return stack
	else: 
		return []

def scan_file(file):
	'''This function parses thru the 
	input file lines, calls function substitute and 
	writes the final list to output file'''
	with open(file, 'r') as f:
	    for line in f.readlines():
	        try:
	        	if line:
	        		word = substitute(line)            	
	        except: continue
	        print >>out_file, word

if __name__ == '__main__':

    scan_file('wordlist.txt')
    out_file.close()
