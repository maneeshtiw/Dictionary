#Creating a dictionary in python
# Importing data from json file

import json

#To get close matches of word we use difflib module
from difflib import get_close_matches

#importing words data in data variable
data=json.load(open("data.json"))

#creating a function that returns meanings of words
def translate(word):
    #making words in lowercase
    word.lower()

    #if word is in data it will reurn meanigof that word
    if word in data:
        return data[word]

    #else if word is a title
    elif word.title() in data:
        return data[word.title()]

    #else if word is a Capital case
    elif word.upper() in data:
        return data[word.upper()]

    #else get the close matches
    # if len()>0(i.e the word is not empty string) then only it makes sence to get close match
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead "%get_close_matches(word,data.keys())[0])
        decision=input("Enter y for yes n for no :")
        if decision=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decision=="n":
            return print("You have entered a wrong word")
        else:
            return print("You have enter a wrong input enter y or n only.")
    else:
        return print("The entered word is not in dictionary")

#Creating a word variable that will store word you want to search
word=input("Enter the word you want to search :")
output=translate(word)

#Now to show the sentence in a proper format we make it into list
if output==list:
    for i in output:
        print(i)
else:
    print(output)