#!/bin/python3

#importing
print("import: importing is important")

import sys #system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #import as alias
print(dt.now())

def new_line():
	print("\n")
new_line()

#Advanced Strings
print("advanced strings")


my_name = "heath"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence"
print(sentence[:4]) #first word
print(sentence[-9:]) #last word
print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print("\n".join(sentence_split))
print(sentence_join)

#quoteception
quoteception = "he said ,'give me all the money'"
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) #improved - case sensitive

word2 = "Bingo"
print(letter.lower() in word.lower()) and not (letter.lower() in (word2.lower())) 

too_much_space = "                          hello                     "
print(too_much_space.strip())
full_name = "amian orina"
print(full_name.replace("amian","Damian"))
print(full_name.find("orina"))

movie = "The hangover"

print("my favorite movie is {}".format(movie))

def favorite_book(title,author):
	fav ="my favorite book id \"{}\" and it is written by {}".format(title,author)
	return fav
print(favorite_book("goat matata","felix rapogi"))

new_line()

#dictionaries
print("dictionaries are key and values")

drinks = {"white russians": 7,"coffee": 10,"cocacola": 12,"alchohol": 50,"juice":20} #drink is key price is value

print(drinks)

employees = {"finance": ["damian","linda","faith"],"IT": ["sydney","waweru","orina"],"Procurement":["laurence","juliet","abby"]}

print(employees)

employees["legal"] = ["mr clay","abunuasi","cassypool"]

print(employees)
employees.update({"sales":["ricky","andy"]})

print(employees)

drinks["white russians"] = 19
print(drinks)
print(drinks.get("white russians"))
print(drinks.get("fanta"))

new_line()
#lists and dictionaries
movies = ["the hangover","ghost rider","transformers","avatar"]
people = ["damian", "shelmith", "lawrence","charity"]

combined = zip(movies,people)
movie_dictionary ={key:value for key,value in combined}
print(movie_dictionary)






