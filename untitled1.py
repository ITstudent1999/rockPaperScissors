# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:42:54 2020

@author: Julian
"""


import secrets
lista = ["papier","kamien","nozyce"]
while True:
    choice = input()
    drawn = secrets.choice(lista)
    print(f"Wybrales: {choice}, komputer wylosowal {drawn}")
    if(choice == drawn):
        print("Remis")
    else:
        if(choice == "papier"):
            if(drawn == "kamien"):
                print("Wygrales!")
            elif(drawn == "nozyce"):
                print("Przegrales!")
        elif(choice == "kamien"):
            if(drawn == "nozyce"):
                print("Wygrales!")
            elif(drawn == "papier"):
                print("Przegrales!")
        elif(choice == "nozyce"):
            if(drawn == "papier"):
                print("Wygrales!")
            elif(drawn == "kamien"):
                print("Przegrales!")