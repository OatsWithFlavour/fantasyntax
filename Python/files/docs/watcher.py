import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import hashlib
import threading

MAIN_PATH = Path("F:/Git/fantasyntax/Python/main.py")
WATCH_DIR = Path(__file__).parent.resolve()
DEBUG = False
DEBOUNCE_SECONDS = 1.0

letzte_verarbeitung = {}

def hash_datei(pfad: Path) -> str:
    try:
        with open(pfad, "rb") as f:
            return hashlib.sha1(f.read()).hexdigest()
    except Exception as e:
        if DEBUG:
            print(f"[DEBUG] Fehler beim Hashen: {e}")
        return ""

def verarbeite_datei(pfad: Path):
    jetzt = time.time()
    datei_hash = hash_datei(pfad)

    info = letzte_verarbeitung.get(pfad)
    if info:
        letzte_zeit, letzter_hash = info
        if datei_hash == letzter_hash and (jetzt - letzte_zeit) < DEBOUNCE_SECONDS:
            if DEBUG:
                print(f"[DEBUG] Ignoriere {pfad} (Hash gleich, kürzlich verarbeitet)")
            return

    letzte_verarbeitung[pfad] = (jetzt, datei_hash)
    print(f"[Watcher] Geändert: {pfad}")
    if DEBUG:
        print(f"[DEBUG] Starte Verarbeitung von {pfad}")
    subprocess.run(["python", str(MAIN_PATH), str(pfad)])

class TxtFileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith(".txt"):
            return

        pfad = Path(event.src_path).resolve()
        if DEBUG:
            print(f"[DEBUG] Event erhalten: modified → {pfad}")

        # Verarbeitung in eigenem Thread mit kurzer Verzögerung
        threading.Timer(0.3, verarbeite_datei, args=[pfad]).start()

def start_watching():
    if not MAIN_PATH.exists():
        raise FileNotFoundError(f"main.py nicht gefunden: {MAIN_PATH}")
    
    event_handler = TxtFileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, str(WATCH_DIR), recursive=True)
    observer.start()
    print(f"[Watcher] Überwache rekursiv: {WATCH_DIR}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watching()
