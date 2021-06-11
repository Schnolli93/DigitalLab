import mysql
import mysql.connector


def add_zutat():
    fridge = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "NfKcXsl3E43yMZVbEmJC",
        database = "kühlschrank")
    fr = fridge
    mycursor = fr.cursor()

    Einkauf = dict()

    zutat_vorhanden = True

    while True:
        zutat_check_query = ("SELECT zutat_id FROM lebensmittel WHERE zutat_name = %s")
        aktualisieren_query = ("UPDATE lebensmittel SET menge = %s WHERE zutat_name = %s")
        #hier wird noch überschrieben, statt berechnet

        Lebensmittel = str(input("Welches Lebensmittel möchtest du hinzufügen? (Drücke 'Enter' zum stoppen.) "))
        mycursor.execute(zutat_check_query, (Lebensmittel,))
        zutat_available = mycursor.fetchone()

        if zutat_available == False:
            for x in zutat_available:
                print("")
                print("Zutat ist bereits vorhanden.")
                print("Menge wird aktualisiert.")
                mycursor.execute(aktualisieren_query, (menge, Lebensmittel,))


        elif Lebensmittel == "":
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

        Einkauf[Lebensmittel]= menge, einheit

add_zutat()