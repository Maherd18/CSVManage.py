import csv

# Hilfsfunktion zum Laden von CSV-Dateien
def load_csv(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Fehler: Datei {filename} nicht gefunden.")
        return []
    except Exception as e:
        print(f"Fehler beim Einlesen von {filename}: {e}")
        return []

# Korrekte Pfadangaben für Windows (angepasst mit r'')
studierende = load_csv(r"C:\Users\MDarweesh\OneDrive - apsolut GmbH\Documents\Studierende.csv")
studiengaenge = load_csv(r"C:\Users\MDarweesh\OneDrive - apsolut GmbH\Documents\studiengaenge.csv")
zugeordnete_studiengaenge = load_csv(r"C:\Users\MDarweesh\OneDrive - apsolut GmbH\Documents\zugeordnete_studiengaenge.csv")

# Mapping für Studiengänge erstellen (Prüfung auf KeyError)
studiengang_dict = {sg.get('Studiengang_ID', ''): sg.get('Studiengang_Name', 'Unbekannt') for sg in studiengaenge}

# Studierende mit Studiengängen verknüpfen
def get_students_with_programs():
    student_programs = {}
    for entry in zugeordnete_studiengaenge:
        student_id = entry.get('Studenten_ID', '')
        if student_id not in student_programs:
            student_programs[student_id] = []
        student_programs[student_id].append(studiengang_dict.get(entry.get('Studiengang_ID', ''), 'Unbekannt'))
    return student_programs

student_programs = get_students_with_programs()

# Ausgabe der Liste
print("Vorname | Nachname | Studiengang")
print("-" * 40)
for student in studierende:
    student_id = student.get('Studenten_ID', '')
    studiengang_list = student_programs.get(student_id, ['Kein Studiengang'])
    for studiengang in studiengang_list:
        print(f"{student.get('Vorname', 'Unbekannt')} | {student.get('Nachname', 'Unbekannt')} | {studiengang}")

# Funktion zum Ändern eines Studiengangs
def change_study_program(student_id, old_program_id, new_program_id, file_path):
    changed = False
    for entry in zugeordnete_studiengaenge:
        if entry.get('Studenten_ID') == student_id and entry.get('Studiengang_ID') == old_program_id:
            entry['Studiengang_ID'] = new_program_id
            changed = True

    if changed:
        try:
            with open(file_path, mode='w', encoding='utf-8', newline='') as file:
                fieldnames = ['Studenten_ID', 'Studiengang_ID']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(zugeordnete_studiengaenge)
            print("Studiengang erfolgreich geändert!")
        except Exception as e:
            print(f"Fehler beim Schreiben der Datei: {e}")
    else:
        print("Kein Eintrag gefunden, der geändert werden konnte.")

# Beispielaufruf (Anpassen der ID-Werte nötig)
# change_study_program('1', '2', '3', r'C:\Users\MDarweesh\OneDrive - apsolut GmbH\Documents\Studium\.vscode\Python\zugeordnete_studiengaenge.csv')
