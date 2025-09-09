import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API")
steam_id = "76561198843060066" # Questo è lo SteamID64 di Gabe Newell :)

# Costruisci l'URL per l'endpoint GetPlayerSummaries
url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"

# Esegui la richiesta GET
response = requests.get(url)

# Controlla se la richiesta è andata a buon fine
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Errore: {response.status_code}")