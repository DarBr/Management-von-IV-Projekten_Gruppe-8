import requests
import os
from dotenv import load_dotenv

# Lade Umgebungsvariablen aus der .env Datei
load_dotenv()

API_KEY = os.getenv("API_KEY")

MODEL_NAME = "gemini-2.5-flash"
url = f"https://generativelanguage.googleapis.com/v1/models/{MODEL_NAME}:generateContent?key={API_KEY}"


data_for_ai = """
1. Projekt A: Ziel = Effizienzsteigerung, Branche = IT, Methode = Agile, Budget = 50k€
2. Projekt B: Ziel = Wissensaufbau, Branche = IT, Methode = Scrum, Budget = 55k€
3. Projekt C: Ziel = Kundenzufriedenheit, Branche = Marketing, Methode = Agile, Budget = 60k€
"""

prompt = f"Analysiere diese Projekte auf Gemeinsamkeiten:\n{data_for_ai}"

payload = {
    "contents": [
        {
            "role": "user",
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

response = requests.post(url, json=payload)
data = response.json()

if "error" in data:
    print("Fehler von der API:", data["error"])
else:
    try:
        # Nur den Text der KI-Antwort ausgeben
        text = data['candidates'][0]['content']['parts'][0]['text']
        print("\n=== KI-Antwort ===\n")
        print(text)
    except (KeyError, IndexError):
        print("Antwortformat unbekannt:", data)
