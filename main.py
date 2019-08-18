from random import randint
import requests
import os

clear = lambda: os.system("cls")

site = input("JSON Link? ")
json = requests.get(site).json()

main_lang = []
second_lang = []

for x in json["translate"]:
    if json["translate"][x]:
        main_lang.append(x)
        second_lang.append(json["translate"][x])

def gen_word():
    if len(main_lang) <= 1: return # to stop any crashes
    rand = randint(0, len(main_lang)-1) # choose a random number between 0 and the length of the list minus one since the start of a list is always 0, not 1
    word = main_lang[rand]

    return word, second_lang[rand]

input("Continue when ready")
clear()

while True:
        word, tran = gen_word()
        user_input = input("Translate '"+word+"'. ")
        if user_input.lower() == tran.lower():
                print("Correct, Well done!")
        else:
                print("Incorrect")
        input()
        clear()

# install googles translating stuff in future