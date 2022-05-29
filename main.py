#!/usr/bin/env python
# -*- coding: utf-8 -*-




"""funkcje mechaniki programu"""

from core import interface, system, tables
"""interface - funkcje graficzne"""
"""tables - obsługa bazy danych"""
"""system - funkcje startowe, konfiguracja"""

"""części aplikacji"""

import orders #"""zarządzanie zamówieniami"""
import books #"""zarządzanie książkami"""
import authors #"""zarządzanie autorami"""
import clients #"""zarządzanie klientami"""





def main():
    system.boot()
    while True:
        print("UWAGA! zapis danych następuje przy wpisaniu komendy 'wyjdź'")
        menu()

def menu():
    order=interface.printInterface("główne menu", [
        "książki",
        "autorzy",
        "klienci",
        "zamówienia",
        "wyjdź"
    ])
    if order=="książki":
        books.menu()
    elif order=="autorzy":
        authors.menu()
    elif order=="klienci":
        clients.menu()
    elif order=="zamówienia":
        orders.menu()
    elif order=="wyjdź":
        system.quitting()
    else:
        interface.unknowCommandPrompt()

main()
