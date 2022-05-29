#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from core import system

headers={ #"""nagłówki tabel"""
    "klienci":[
        "id",
        "imię",
        "nazwisko"
    ],
    "ksiazki":[ 
        "id",
        "tytuł",
        "gatunki",
        "rok",
        "ilość stron",
        "id autorzy"
    ],
    "autorzy":[
        "id",
        "imie",
        "nazwisko"
    ],
    "zamowienia":[ 
        "id",
        "id ksiazki",
        "id klienci",
        "wypożyczone"
    ]
}
data={ #"""dane tabeol"""
    "klienci":[],
    "ksiazki":[], 
    "autorzy":[],
    "zamowienia":[] 
}

def getColumnIndex(table, headerName):
    print("#szukanie indexu kolumny "+headerName+" w tableli "+table+"...")
    global headers
    tmp=-1
    for i in range(len(headers[table])):
        #print(i)
        if headers[table][i]==headerName:
            tmp=i
    print(tmp)
    return tmp

def getById(table, id):
    print("#szukanie id "+str(id)+" w tableli "+table+"...")
    global data
    idColumn=getColumnIndex(table, "id")
    result=None
    #print(idColumn)
    #print(data[table])
    for i in data[table]:
        print(str(i[idColumn])+"=="+str(id)+" --> "+str(i[idColumn])==str(id))
        if str(i[idColumn])==str(id):
            result=i
    print(result)
    return result


def initializeDB(): #"""jeśli baza danych nie istnieje to stwórz ją, jeśli tak to odczytaj"""
    try:
        print("baza danych nie została wykryta")
        os.mkdir(system.config["databaseLocation"])
        print("~ baza danych została stworzona ~")
        createTables()
    except FileExistsError: #"""przechwyt błędu tylko gdy próbuje się stworzyć istniejący plik"""
        print("baza danych wykryta!")
        readTables()

def createTables():
    global data #"""dane bazy danych są globalne"""
    for i in data:
        open(system.config["databaseLocation"]+"/"+i+".txt", "x")
        print("~ stworzono tabelę '"+i+"'  ~")

def writeTables():
    global data #"""dane bazy danych są globalne"""
    for i in data:
        print("-zapis tabeli "+i)
        for j in range(len(data[i])):
            tmp=[]
            for k in data[i][j]:
                tmp.append(str(k))
            data[i][j]=",".join(tmp) #"""łączenie listy z delimiterem ",""""
        data[i]="\n".join(data[i])
        f=open(system.config["databaseLocation"]+"/"+i+".txt", "w+")
        f.write(data[i])
        f.close()


def readTables():
    global data, headers #"""dane bazy danych są globalne"""
    for i in data:
        print("-odczyt tabeli "+i)
        data[i]=open(system.config["databaseLocation"]+"/"+i+".txt", "r").read()
        data[i]=data[i].split("\n")
        for j in range(len(data[i])):
            data[i][j]=data[i][j].split(",")
            if len(data[i][j])!=len(headers[i]):
                del data[i][j]
