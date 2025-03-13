import csv

# Datei einlesen
def load_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

studium = load_csv("C:\Users\MDarweesh\OneDrive - apsolut GmbH\Documents\studium.csv")

# Ausgabe der Liste
print("Vorname | Nachname | Studiengang")
print("-" * 40)
for student in studium:
    print(f"{student['Vorname']} | {student['Nachname']} | {student['Studiengang']}")

# Beispielhafte Änderung des Studiengangs eines Studierenden
def change_study_program(student_vorname, student_nachname, new_program):
    for student in studium:
        if student['Vorname'] == student_vorname and student['Nachname'] == student_nachname:
            student['Studiengang'] = new_program
            break  # Falls es mehrere mit dem gleichen Namen gibt, nur den ersten ändern
    
    # Änderungen speichern
    with open("C:\Users\MDarweesh\OneDrive - apsolut GmbH\Documents\studium.csv", mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ['Vorname', 'Nachname', 'Studiengang']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(studium)
    print("Studiengang erfolgreich geändert!")

# Beispielaufruf (muss mit existierenden Namen ausgeführt werden)
# change_study_program('Max', 'Müller', 'Informatik')
