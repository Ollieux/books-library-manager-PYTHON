#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import interface, system, tables


def menu():
    order=interface.printInterface("ksiazki", [
        "dodaj",
        "wypisz",
        "wypisz rosnąco",
        "wypisz malejąco",
        "wypisz konkretnego autorstwa",
        "wypisz chudsze niż",
        "wypisz grubsze niż",
        "wróć"
    ])
    if order=="dodaj":
        addBook()
        menu()
    elif order=="wypisz":
        printBooks()
        menu()
    elif order=="wypisz rosnąco":
        printBooksByColumn("descending")
        menu()
    elif order=="wypisz malejąco":
        printBooksByColumn()
        menu()
    elif order=="wypisz konkretnego autorstwa":
        printBooksByAuthorOnly()
        menu()
    elif order=="wypisz chudsze niż":
        printBooksBySize()
        menu()
    elif order=="wypisz grubsze niż":
        printBooksBySize("thicker")
        menu()
    elif order=="wróć":
        None
    else:
        interface.unknowCommandPrompt()
        menu()

def printBooksByColumn(mode="ascending"):
    print()
    for i in tables.headers["ksiazki"]:
        print("       "+i)
    print()
    column=tables.getColumnIndex("ksiazki", input("     wybierz kolumnę:"))
    tmp=[]
    result=[]
    for i in tables.data["ksiazki"]:
        tmp.append(str(i[column])+","+str(i[tables.getColumnIndex("ksiazki", "id")]))
    if mode=="ascending":
        tmp.sort()
    else:
        tmp.sort()
        tmp.reverse()
    for i in tmp:
        result.append(tables.getById("ksiazki",int(i.split(",")[1])))
    interface.printTableFromData(
        "książki",
        tables.headers["ksiazki"],
        result
    )

def printBooksBySize(mode="slimmer"):
    pageLimit=input("     wprowadź ilość stron:")
    pageCount=tables.getColumnIndex("ksiazki", "ilość stron")
    tmp=[]
    for i in tables.data["ksiazki"]:
        if mode=="slimmer":
            if int(i[pageCount])<=int(pageLimit):
                tmp.append(i)
        elif mode=="thicker":
            if int(i[pageCount])>=int(pageLimit):
                tmp.append(i)
    interface.printTableFromData(
        "książki",
        tables.headers["ksiazki"],
        tmp
    )

def printBooksByAuthorOnly():
    print()
    interface.printTable("autorzy", False)
    print()
    idSearched=int(input("     podaj id autora:"))
    tmp=[]
    for i in tables.data["ksiazki"]:
        #print(tables.getColumnIndex("ksiazki", "id autorzy"))
        #print(i)
        if i[tables.getColumnIndex("ksiazki", "id autorzy")]==idSearched:
            tmp.append(i)
    print(tables.getById("autorzy",idSearched))
    title="książki autorstwa "
    title=title+tables.getById("autorzy",idSearched)[1]
    title=title+" "
    title=title+tables.getById("autorzy",idSearched)[2]
    interface.printTableFromData(
        title,
        tables.headers["ksiazki"],
        tmp
    )

def printBooks():
    interface.printTable("ksiazki")

def addBook():
    tables.data["ksiazki"].append(interface.insertRow("ksiazki"))
