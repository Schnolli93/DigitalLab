import mysql
import mysql.connector

def add_zutat():
    fridge = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "NfKcXsl3E43yMZVbEmJC",
        database = "digitallabdb")
    fr = fridge
    mycursor = fr.cursor(buffered=True)


    Einkauf = dict()

    while True:
        Einkauf = dict()
        lebensmittel = input("Welches Lebensmittel möchtest du hinzufügen? (Drücke 'Enter' zum stoppen.) ")

        mycursor.execute("SELECT name FROM food WHERE name = %s", (lebensmittel,))
        msg = mycursor.fetchone()

        # check if it is empty and print error
        if msg:
            print("Zutat ist bereits enthalten. Menge wird aktualisiert.")
            menge = int(input("Welche Menge? "))
            mycursor.execute("UPDATE food SET quantity = %s WHERE name = %s", (menge, lebensmittel,))
            fr.commit()
            print("Menge erfolgreich überschrieben.")
            print("")

        else:
            if lebensmittel == "":
                print("")
                print("Dein Einkauf: ")
                print("")
                print(Einkauf)
                break

            else:
                liste = dict()
                print("ist nicht enthalten")
                menge = int(input("Welche Menge? "))
                einheit = input("Welche Einheit? stk, g, ml? ")
                for key, value in Einkauf.items():
                    print("")
                    mycursor.execute("INSERT INTO food (name, quantity, unit) VALUES (%s, %s, %s)", (key, menge, einheit))
                    fr.commit()
                print("Zutat(en) erfolgreich hinzugefügt.")
                print("")
                liste[lebensmittel] = menge, einheit

        #elif not msg:
        #    print("ist nicht enthalten")
        #    menge = int(input("Welche Menge? "))
        #    einheit = input("Welche Einheit? stk, g, ml? ")
        #    for key, value in Einkauf.items():
        #        print("")
        #        mycursor.execute("INSERT INTO lebensmittel (zutat_name, menge, einheit) VALUES (%s, %s, %s)", (key, menge, einheit))
        #        fr.commit()
        #    print("Zutat(en) erfolgreich hinzugefügt.")
        #    print("")

        #elif lebensmittel.isalpha() == False:
        #    print("")
        #    print("Dein Einkauf: ")
        #    print("")
        #    print(Einkauf)
            #for key, value in Einkauf.items():
            #    print("")
            #    mycursor.execute("INSERT INTO lebensmittel (zutat_name, menge, einheit) VALUES (%s, %s, %s)", (key, menge, einheit))
            #    fr.commit()
            #print("Zutat(en) erfolgreich hinzugefügt.")
        #    break
        #menge = int(input("Welche Menge? "))
        #einheit = input("Welche Einheit? stk, g, ml? ")
        #Einkauf[lebensmittel]= menge, einheit



add_zutat()