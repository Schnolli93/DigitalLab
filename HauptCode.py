import mysql
import mysql.connector

#import pandas as pd
#import numpy as np
#from openpyxl import load_workbook

#Verbindung zur Datenbank herstellen
fridge = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "NfKcXsl3E43yMZVbEmJC",
    database = "digitallabdb")
fr = fridge

#cursor einrichten, der die datenbank verwendet
mycursor = fr.cursor()

def fr_aufbau():
    mycursor.execute("DESCRIBE food")
    for x in mycursor:
        print(x)

def check_fridge():
    fridge = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "NfKcXsl3E43yMZVbEmJC",
        database = "digitallabdb")
    mycursor.execute("SELECT * FROM food WHERE quantity > 1")
    for x in mycursor:
        print(x)

def check_zutat():
    fridge = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "NfKcXsl3E43yMZVbEmJC",
        database = "digitallabdb")
    fr = fridge
    mycursor = fr.cursor()

    menge_select_query = ("SELECT quantity FROM food WHERE name = %s")
    einheit_select_query = ("SELECT unit FROM food WHERE name = %s")

    zutat = str(input("Zutat: "))

    mycursor.execute(menge_select_query, (zutat,))
    menge = mycursor.fetchone()

    mycursor.execute(einheit_select_query, (zutat,))
    einheit = mycursor.fetchone()

    for x in menge:
        print("Menge: ", x)
    for y in einheit:
        print("Einheit: ", y)

def add_zutat():
    fridge = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "NfKcXsl3E43yMZVbEmJC",
        database = "digitallabdb")
    fr = fridge
    mycursor = fr.cursor()

    Einkauf = dict()
    while True:
        lebensmittel = input("Welches Lebensmittel möchtest du hinzufügen? (Drücke 'Enter' zum stoppen.)")

        mycursor.execute("SELECT name FROM food WHERE name = %s", (lebensmittel,))
        msg = mycursor.fetchone()
        # check if it is empty and print error
        if msg:
            print("Ist enthalten.")
            print("Menge wird aktualisiert.")

        if not msg:
            print("ist nicht enthalten")

        if lebensmittel == "":
            print("")
            print("Dein Einkauf: ")
            print("")
            print(Einkauf)
            print("")
            for key, value in Einkauf.items():
                print("")
                mycursor.execute("INSERT INTO lebensmittel (zutat_name, menge, einheit) VALUES (%s, %s, %s)", (key, menge, einheit))
                fr.commit()
            print("Zutat(en) erfolgreich hinzugefügt.")
            break
        menge = int(input("Welche Menge? "))
        einheit = input("Welche Einheit? stk, g, ml? ")
        Einkauf[lebensmittel]= menge, einheit

def run_software():
    print("Hallo!")
    while True:
        task = str(input("Was möchtest du tun? Gebe ein: 'Check', 'Abfrage', 'Add' oder 'End' zum Beenden. ")).lower()

        if task == "check":
            print("")
            check_fridge()
            print("")

        elif task == "abfrage":
            print("")
            check_zutat()
            print("")

        elif task == "add":
            print("")
            add_zutat()
            print("")

        elif task == "end":
            print("")
            print("Bis zum nächsten Mal!")

            break

#fr_aufbau()
run_software()