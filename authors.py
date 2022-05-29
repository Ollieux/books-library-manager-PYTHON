#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import interface, system, tables


def menu():
    order=interface.printInterface("autorzy", [
        "dodaj",
        "wypisz",
        "wróć"
    ])
    if order=="dodaj":
        addAuthor()
        menu()
    elif order=="wypisz":
        printAuthors()
        menu()
    elif order=="wróć":
        None
    else:
        interface.unknowCommandPrompt()
        menu()

def printAuthors():
    interface.printTable("autorzy")

def addAuthor():
    tables.data["autorzy"].append(interface.insertRow("autorzy"))
