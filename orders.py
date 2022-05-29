#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import interface, system, tables


def menu():
    order=interface.printInterface("zamówienia", [
        "dodaj",
        "wypisz",
        "wróć",
        "wypisz niewyporzyczone"
    ])
    if order=="dodaj":
        addOrder()
        menu()
    elif order=="wypisz":
        printOrders()
        menu()
    elif order=="wypisz niewyporzyczone":
        printAvailableBooks()
        menu()
    elif order=="wróć":
        None
    else:
        interface.unknowCommandPrompt()
        menu()

def printOrders():
    interface.printTable("zamowienia")

def printAvailableBooks():
    tmp=[]
    idBooks=tables.getColumnIndex("ksiazki", "id")
    idBooksOrders=tables.getColumnIndex("zamowienia", "id ksiazki")
    tmpBooks=[]
    tmpOrders=[]
    for i in tables.data["ksiazki"]:
        tmpBooks.append(i[idBooks])
    for i in tables.data["zamowienia"]:
        tmpOrders.append(i[idBooksOrders])
    for i in range(len(tmpOrders)):
        for j in range(len(tmpOrders)):
            #############
            None

def addOrder():
    tables.data["zamowienia"].append(interface.insertRow("zamowienia"))
