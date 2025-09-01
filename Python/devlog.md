

## Erledigt

### 05.06.25

- komplette text zu tex Formatierung
- tex in kompilierbares Format bringen
- latex Klasse einbinden
- 2 Modul zum Ausführen schreiben

### 06.06.25

- 1. Modul führt main aus und übergibt main.py save_path von txt bei save
- 2. Modul wird in main ausgeführt und such nach save_path wenn es vom 1. Modul ausgeführt wird
und gibt den save_path an main zurück
- latex_klassen unter klassen/ einbindung vom klassenpfad in .tex datei, vielleicht exta Modul

### 07.06.25

- Muster erstellen, nehme ein fertiges Dokument und erstelle die Muster dazu

### 08.06.25

- geschachtelte Klammerumgebung schaffen

- z.B hat man den Ausdruck: $(a_(s) + wurzel(b + c_(g + d)))/(a + b(c))$

0: "(1)/(2)",
1: "a_(3) + wurzel(4)",
2: "a + b(5)",
3: "s",
4: "b + c_(6)",
5: "c",
6: "g + d"

dann möchte man wurzel(irgendwas) vielleicht austauchen gegen sqrt{irgendwas}

Statt den Ausdruck danach zu durchsuchen soll das dict danach durchsucht werden und dort ausgetauscht werden.

Anschließend soll das dict wieder zu den Ausdruck zusammengebaut werden und eine andere Funktion die alles zusammenfässt.

4 Funktionen:

str -> dict 
dict, str -> dict
dict -> str 
str -> str

- mehr Muster erstellen

- Gibt es ein Format in dem man die Tabellen einträge noch auswählen kann,
 es aber schon eine fertige Tabelle zum einbindne in Latex ist

- Latexfunktionen für Abbildungen, Formeln, Quellen und Tabellen.

- Gedanken zu Speicherort (Unterordner), Verzeichnisse, Referenzen, Funktionsname, Parameter, 
Zusatzinformationen(Beschriftung, Namen, Legende(Formeln: Einheiten), Quellverweise)

### 09.06.25

- Erstellung von Python Tabellen aus csv im Unterordner csv

- delta und avg 

- Funktionen für Zeilentabelle und grafik einbinden

- Praktikum Schwerebeschleungigung


## TODO

- Zitierart dokumentieren

- Darstellung einer Funktion als Block

- Einbinden von Funktionen in Muster - Ersatz

- Übersicht Erstellung von Literaturverzeichnissen

- Einbindung von Funktionen in Transformation

- Auslagerung der Tabellen-, Abbildungs-, Formel-, Literaturquellen, Symboldaten

- um die Inputs von anderen tex Dateien kümmern



- Vorbereitung Praktikum

- Latexklasse erweitern vorallem Quellen, Referenzen und Formatierungen sind wichtig