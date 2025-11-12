# buscador_empleo.py  ← versión pública segura
import requests, time, hashlib, urllib.parse, os
from bs4 import BeautifulSoup

TOKEN = os.getenv("TOKEN")        # ← Fly.io lo inyecta
CHAT_ID = os.getenv("CHAT_ID")    # ← Fly.io lo inyecta
PALABRAS = "python developer remoto"
UBICACION = "Mexico"
INTERVALO = 600

def enviar(texto, url=None):
    payload = {"chat_id": CHAT_ID, "text": texto[:4000], "parse_mode": "HTML"}
    if url: payload["reply_markup"] = {"inline_keyboard": [[{"text": "Ver oferta ➜", "url": url}]]}
    try: requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
    except: pass

vistas = set()
enviar("Bot empleo 24/7 en Fly.io GRATIS y SEGURO!")

# ← PEGA AQUÍ LAS 3 FUNCIONES indeed(), computrabajo(), occ() que ya tienes

while True:
    nuevas = 0
    for func in [indeed, computrabajo, occ]:
        try:
            for t,e,l,u,f in func()[:10]:
                idd = hashlib.md5((t+e).encode()).hexdigest()
                if idd not in vistas:
                    vistas.add(idd)
                    enviar(f"<b>{t}</b>\n{e}\n{u}\n{f}", l)
                    nuevas += 1
                    time.sleep(2)
        except: pass
    print(f"{nuevas} nuevas")
    time.sleep(INTERVALO)
