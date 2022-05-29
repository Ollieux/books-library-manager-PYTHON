#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import interface, system, tables


def menu():
    order=interface.printInterface("klienci", [
        "dodaj",
        "wypisz",
        "wróć"
    ])
    if order=="dodaj":
        addClient()
        menu()
    elif order=="wypisz":
        printClients()
        menu()
    elif order=="wróć":
        None
    else:
        interface.unknowCommandPrompt()
        menu()

def printClients():
    interface.printTable("klienci")

def addClient():
    tables.data["klienci"].append(interface.insertRow("klienci"))
