import os
import pandas as pd
import matplotlib.pyplot as plt

def get_tabellen_verzeichnis(dateipfad: str) -> str:
    """Gibt den Pfad zum Tabellen-Unterordner zurück basierend auf dem Pfad zur Ausgangsdatei."""
    verzeichnis = os.path.dirname(dateipfad)
    tabellen_pfad = os.path.join(verzeichnis, "Tabellen")
    return tabellen_pfad

def finde_csv_dateien(verzeichnis: str) -> list[str]:
    """Findet alle CSV-Dateien im übergebenen Verzeichnis."""
    return [
        os.path.join(verzeichnis, datei)
        for datei in os.listdir(verzeichnis)
        if datei.lower().endswith(".csv")
    ]

def lade_csv_als_dataframe(csv_pfad: str) -> pd.DataFrame:
    """Lädt eine CSV-Datei als DataFrame."""
    return pd.read_csv(csv_pfad)


def plotte_dataframe_als_pdf(df, ziel_pfad, kopf="zeile"):
    fig, ax = plt.subplots(figsize=(len(df.columns)*1.8, len(df)*0.4+0.5))
    ax.axis('off')

    table = ax.table(
        cellText=df.values, colLabels=df.columns,
        cellLoc='center', loc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    if kopf == "zeile":
        for col in range(len(df.columns)):
            table[(0, col)].set_facecolor('#D3D3D3')
    elif kopf == "spalte":
        for row in range(len(df)+1):
            table[(row, 0)].set_facecolor('#D3D3D3')
    else:
        raise ValueError("kopf muss 'zeile' oder 'spalte' sein")

    # WICHTIG: Canvas einmal zeichnen, damit renderer existiert
    fig.canvas.draw()

    # Bounding-Box der Tabelle ermitteln
    bbox = table.get_window_extent(fig.canvas.get_renderer())

    # In fig-inch Koordinaten umwandeln
    bbox_inches = bbox.transformed(fig.dpi_scale_trans.inverted())

    # Speichern nur des exakten Bereichs
    fig.savefig(ziel_pfad, format='pdf',
                bbox_inches=bbox_inches, pad_inches=0)
    plt.close(fig)


def verarbeite_alle_csvs(dateipfad: str):
    """Hauptfunktion, die alles kombiniert und PDFs für alle CSVs erzeugt."""
    tabellen_verzeichnis = get_tabellen_verzeichnis(dateipfad)
    csv_dateien = finde_csv_dateien(tabellen_verzeichnis)
    
    for csv_pfad in csv_dateien:
        df = lade_csv_als_dataframe(csv_pfad)
        pdf_name = os.path.splitext(os.path.basename(csv_pfad))[0] + ".pdf"
        pdf_pfad = os.path.join(tabellen_verzeichnis, pdf_name)
        plotte_dataframe_als_pdf(df, pdf_pfad)

def plotte_einzelne_csv(dateipfad: str, csv_name: str, kopf: str = "zeile"):
    """
    Plottet eine einzelne CSV-Datei im Tabellenordner basierend auf Dateipfad und CSV-Dateinamen.
    Speichert den Plot als PDF mit gleichem Namen.
    """
    tabellen_verzeichnis = get_tabellen_verzeichnis(dateipfad)
    csv_pfad = os.path.join(tabellen_verzeichnis, csv_name)
    
    if not os.path.exists(csv_pfad):
        raise FileNotFoundError(f"CSV-Datei nicht gefunden: {csv_pfad}")
    
    df = lade_csv_als_dataframe(csv_pfad)
    pdf_name = os.path.splitext(csv_name)[0] + ".pdf"
    pdf_pfad = os.path.join(tabellen_verzeichnis, pdf_name)
    plotte_dataframe_als_pdf(df, pdf_pfad, kopf=kopf)
