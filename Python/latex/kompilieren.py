import subprocess
import os
import shutil

def _alte_hilfsdateien_entfernen(verzeichnis: str, tex_name: str):
    """Löscht alte Hilfsdateien im gegebenen Verzeichnis."""
    for ext in [".aux", ".log", ".out", ".toc", ".lof", ".lot", ".synctex.gz"]:
        datei = os.path.join(verzeichnis, f"{tex_name}{ext}")
        if os.path.exists(datei):
            os.remove(datei)

def kompiliere_tex(tex_pfad: str, pdf_zielpfad: str = None, versuche: int = 2):
    """
    Kompiliert eine .tex-Datei zu PDF.
    Die gesamte Kompilierung erfolgt im Unterordner 'latex_helper'.
    Nur das finale PDF wird ins Ursprungsverzeichnis zurückkopiert.
    """
    tex_verzeichnis = os.path.dirname(tex_pfad)
    tex_datei = os.path.basename(tex_pfad)
    tex_name, _ = os.path.splitext(tex_datei)

    hilfsordner = os.path.join(tex_verzeichnis, "latex_helper")
    tex_hilfspfad = os.path.join(hilfsordner, tex_datei)
    pdf_datei_name = f"{tex_name}.pdf"
    pdf_temp_pfad = os.path.join(hilfsordner, pdf_datei_name)
    pdf_endziel = pdf_zielpfad or os.path.join(tex_verzeichnis, pdf_datei_name)

    try:
        os.makedirs(hilfsordner, exist_ok=True)
        _alte_hilfsdateien_entfernen(hilfsordner, tex_name)

        # Kopiere die .tex-Datei in das Hilfsverzeichnis
        shutil.copy2(tex_pfad, tex_hilfspfad)

        # Führe die Kompilierung im Hilfsverzeichnis aus
        for _ in range(versuche):
            subprocess.run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    tex_datei
                ],
                cwd=hilfsordner,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )

        if not os.path.exists(pdf_temp_pfad):
            raise FileNotFoundError(f"PDF-Datei wurde nicht erzeugt: {pdf_temp_pfad}")

        shutil.move(pdf_temp_pfad, pdf_endziel)
        print(f"✅ PDF erfolgreich gespeichert unter: {pdf_endziel}")

    except subprocess.CalledProcessError as e:
        print("❌ Fehler beim Kompilieren der .tex-Datei:", e)
    except Exception as e:
        print("❌ Allgemeiner Fehler:", e)
