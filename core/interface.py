#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from core import tables, system

def printHeader(title):
    print()
    print("  ########################")
    print()
    print("    ~~~ Baza danych biblioteki ~~~")
    print("    "+title)
    print()

def printInterface(title, options): 
    printHeader(title)
    print("     OPCJE:")
    print()
    for i in options:
        print("     "+i)
    print()
    print("  ########################")
    print()
    order=input("     ~[wprowadź komendę]~>")
    print()
    return order

def unknowCommandPrompt():
    print("!!! nie rozpoznano komendy !!!")
    time.sleep(1) #"""czekaj sekundę"""

def printTableFromData(title, headers, data, pauseEnded=True):
    print("  ########################")
    print()
    print("     "+title)
    print()
    print("     "+"  |  ".join(headers))
    print()
    for i in data:
        tmp=[]
        for j in i:
            tmp.append(str(j))
        print("     "+"  |  ".join(tmp))
    if pauseEnded:
        input("     [wciśnij ENTER]                 ")

def printTable(name, pauseEnded=True):
    printTableFromData(name, tables.headers[name], tables.data[name], pauseEnded)

def specialInput(label):
    return input("     "+label)

def choiceFromTable(title):
    while True:
        choice=input("    czy chcesz wprowadzić nowy rekord? (y/n)")
        if choice=="y":
            tables.data[title].append(insertRow(title))
            return system.config["autoincrement"][title]
        elif choice=="n":
            printTable(title, False)
            tmp=input("     wybierz id "+title+":")
            return int(tmp)

def insertRow(title):
    inputData=[]
    print()
    print("     tabela "+title+" - wprowadzanie danych")
    print()
    for i in tables.headers[title]:
        if i=="id":
            inputData.append(system.autoincrement(title))
        elif i[:3]=="id ": #"""jeśli w nagłówku kolumny występuje 'id ' znaczy to że po spacji powinna być nazwa tabeli"""
            inputData.append(choiceFromTable(i[3:])) #"""wyświetla tabelę z którą relacja łączy się z tym polem"""
        else:
            tmp=input("     "+i+":").replace(",",".") #"""przecinek zamienia na kropkę"""
            inputData.append(tmp)

    print()
    print("     zakończono wprowadzanie danych")
    print()
    return inputData
