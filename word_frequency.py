#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True
    
def display(list):
    for i in list:
        print(i," = ",list[i])

def calculate(sentence):
    sentence=sentence.lower()
    list1=sentence.split()
    list2={}
    for i in list1:
        if i[-1] == '.':
            i = i[0:len(i) - 1]
        if i in list2:
            list2[i] += 1
        else:
            list2.update({i: 1})
    display(list2)
        

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

calculate(user_sentence)
