def eingabe_schritte():
    """Funktion für die Eingabe der Schritte"""
    while True:
        try:
            schritte = int(input("Nennen Sie die Anzahl der Schritte, die Sie gemacht haben.\n"))
            if schritte < 0:
                raise ValueError("Die Eingabe darf nicht negativ sein")
            return schritte
        except ValueError as e:
            print(f"Fehler: {e}, bitte eine gültige Zahl eingeben.")

def eingabe_trainingszeit():
    """Funktion für die Eingabe der Trainingszeit"""
    while True:
        try:
            trainingszeit = int(input("Nennen Sie, wie viele Minuten Sie heute trainiert haben.\n"))
            if trainingszeit < 0:
                raise ValueError("Die Eingabe darf nicht negativ sein")
            return trainingszeit
        except ValueError as e:
            print(f"Fehler: {e}, bitte eine gültige Zahl eingeben.")

def eingabe_kalorienverbrauch():
    """Funktion für die Eingabe des Kalorienverbrauchs"""
    while True:
        try:
            kalorienverbrauch = int(input("Nennen Sie, wie viele Kalorien Sie verbrannt haben.\n"))
            if kalorienverbrauch < 0:
                raise ValueError("Die Eingabe darf nicht negativ sein")
            return kalorienverbrauch
        except ValueError as e:
            print(f"Fehler: {e}, bitte eine gültige Zahl eingeben.")

def tage_speichern(fitness_daten, schritte, trainingszeit, kalorienverbrauch):
    """Speichert die Tag-Daten in einer Liste"""
    tag = {
        "Tag": len(fitness_daten) + 1,
        "Schritte": schritte,
        "Trainingszeit": trainingszeit,
        "Kalorienverbrauch": kalorienverbrauch,
    }
    fitness_daten.append(tag)

def daten_anzeigen(tag_ask, fitness_daten):
    """Zeigt die Daten an, je nachdem, ob der Benutzer einen bestimmten Tag oder alle sehen möchte"""
    if tag_ask == "bestimmten":
        try:
            tag_num = int(input("Welchen Tag möchten Sie sehen?"))
            if 0 < tag_num <= len(fitness_daten):
                print(fitness_daten[tag_num - 1])  # Gibt den Tag basierend auf der Eingabe aus
            else:
                print("Ungültiger Tag!")
        except ValueError:
            print("Ungültige Eingabe!")
    elif tag_ask == "alle":
        print(fitness_daten)  # Gibt alle gespeicherten Tage aus
    else:
        print("Falsche Eingabe")

def zusammenfassung_daten(gesamt_schritte, gesamt_trainingszeit, gesamt_kalorienverbrauch):
    """Gibt eine Zusammenfassung der gesammelten Daten aus"""
    print(f"\nHier ist eine Zusammenfassung Ihrer Daten:\n"
          f"Gesamte Schritte: {gesamt_schritte}\n"
          f"Gesamte Trainingszeit: {gesamt_trainingszeit} Minuten\n"
          f"Gesamter Kalorienverbrauch: {gesamt_kalorienverbrauch} Kalorien")

def fitness_tracker():
    """Die Hauptfunktion für den Fitness Tracker"""
    print("Willkommen zum Fitness Tracker")
    
    fitness_daten = []  # Liste für die täglichen Daten
    
    # Initialisierung der Gesamtwerte
    gesamt_schritte = 0
    gesamt_trainingszeit = 0
    gesamt_kalorienverbrauch = 0
    
    try:
        while True:
            # Benutzereingabe für Schritte, Trainingszeit und Kalorienverbrauch
            schritte = eingabe_schritte()
            trainingszeit = eingabe_trainingszeit()
            kalorienverbrauch = eingabe_kalorienverbrauch()
            
            # Daten speichern
            tage_speichern(fitness_daten, schritte, trainingszeit, kalorienverbrauch)
            
            # Aktuelle Gesamtwerte berechnen
            gesamt_schritte += schritte
            gesamt_trainingszeit += trainingszeit
            gesamt_kalorienverbrauch += kalorienverbrauch
            
            print("\nWas möchten Sie tun?")
            print("1. Weitere Daten eingeben (ja)")
            print("2. Bestimmten Tag oder alle Tage anzeigen (anzeigen)")
            print("3. Zusammenfassung anzeigen (zusammenfassung)")
            print("4. Programm beenden (beenden)")
            
            again = input("Ihre Wahl: ").lower()
            
            if again == "ja":
                schritte = eingabe_schritte()
                trainingszeit = eingabe_trainingszeit()
                kalorienverbrauch = eingabe_kalorienverbrauch()
                
                tage_speichern(fitness_daten, schritte, trainingszeit, kalorienverbrauch)
                
                gesamt_schritte += schritte
                gesamt_trainingszeit += trainingszeit
                gesamt_kalorienverbrauch += kalorienverbrauch
                
            elif again == "anzeigen":
                tag_ask = input("Möchten Sie nur einen bestimmten Tag sehen oder alle? (bestimmten/alle): ").lower()
                daten_anzeigen(tag_ask, fitness_daten)
                
            elif again == "zusammenfassung":
                zusammenfassung_daten(gesamt_schritte, gesamt_trainingszeit, gesamt_kalorienverbrauch)
                
            elif again == "beenden":
                break
            else:
                print("Ungültige Eingabe. Bitte 'ja', 'nein', 'anzeigen', 'zusammenfassung' oder 'beenden' eingeben.")
                continue
    except ValueError as e:
        print(f"Fehler: {e}")

    print("Danke, dass Sie den Fitness Tracker benutzt haben")  
    
fitness_tracker()
