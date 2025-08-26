# Die Liste mit den Ausgangsdaten
liste = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

# Die Listenabstraktion:
# [wert FÜR wert IN liste WENN die Bedingung zutrifft]
liste_wochenende = [wert for wert in liste if wert.startswith("S")]

# Das Ergebnis ausgeben
print(liste_wochenende)

