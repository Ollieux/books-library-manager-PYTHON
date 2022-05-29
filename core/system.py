#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import tables
import time
import json

config={
    "databaseLocation":"./db",
    "autoincrement":{
        "ksiazki":0,  
        "klienci":0,
        "autorzy":0,
        "zamowienia":0  
    }
}

def boot():
    print("START MANAGERA BIBLIOTECZNEGO...")
    time.sleep(2)
    configLoading()
    tables.initializeDB() #"""jeśli baza nie istnieje to stwórz

def autoincrement(title):
    global config
    config["autoincrement"][title]=config["autoincrement"][title]+1
    return config["autoincrement"][title]

def decrement(title):
    global config
    config["autoincrement"][title]=config["autoincrement"][title]-1
    return config["autoincrement"][title]

def configLoading():
    global config #"""konfiguracja jest globalna"""
    try: #"""jeśli config.json istnieje
        tmp=json.loads(open("config.json", "r").read()) #"""odczytaj plik jako string i odczytaj z tego stringa dane w formacje JSON"""
        config=tmp
        print("konfiguracja została odczytana z config.json")
    except: #"""jeśli config.json nie istnieje
        print("ERROR: konfiguracja nie została odczytana")
        print("~ config.json został stworzony ~")
        updateConfig()

def updateConfig():
    cnfg=open("config.json", "w+")
    cnfg.write(json.dumps(config,indent=4))
    cnfg.close()

def quitting():
    while True:
        print()
        print()
        print()
        print("     CZY CHCESZ ZAPISAĆ ZMIANY? (y/n)")
        order=input("   ")
        print()
        if order=="y":
            print("~ config.json został zaktualizowany ~")
            updateConfig()
            tables.writeTables() #"""zapis dokonanych zmian """
            break
        elif order=="n":
            print("zmiany zostały porzucone")
            break
    exit()
