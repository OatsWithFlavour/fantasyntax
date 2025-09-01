import pandas as pd

# CSV-Datei einlesen
df = pd.read_csv("files/docs/Thema1/messdaten.csv")

# Spaltennamen ggf. anpassen für LaTeX (keine Sonderzeichen)
df.columns = ["Masse $m$ (g)", "Periode $T$ (s)", "$T^2$ (s$^2$)"]

# Als LaTeX-Tabelle exportieren
latex_code = df.to_latex(
    index=False,
    caption="Messdaten: Schwingungsdauer in Abhängigkeit der Masse",
    label="tab:messdaten",
    float_format="%.3f",
    column_format="c c c",  # Spaltenausrichtung (z. B. l, c, r)
    escape=False  # Damit $...$ funktioniert
)

# In Datei schreiben
with open("tabelle_messdaten.tex", "w", encoding="utf-8") as f:
    f.write(latex_code)
