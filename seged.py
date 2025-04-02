# seged.py

import requests

#  Segédfüggvény az időjárás lekéréséhez
def leker_idojaras(varos):
    url = f"https://wttr.in/{varos}?format=j1"
    try:
        valasz = requests.get(url)
        if valasz.status_code == 200:
            adat = valasz.json()
            aktualis = adat['current_condition'][0]
            homerseklet = aktualis['temp_C']
            leiras = aktualis['weatherDesc'][0]['value']
            paratartalom = aktualis['humidity']
            return [homerseklet, leiras, paratartalom]
        else:
            return ["nincs adat", "-", "-"]
    except:
        return ["hiba", "-", "-"]





#  Segédfüggvény a névnap lekéréséhez
def leker_nevnap(orszag_kod, datum_str):
    """Pl. ország: 'hu', dátum: '03-25'"""
    try:
        honap, nap = datum_str.split("-")
        url = f"https://nameday.abalin.net/api/V2/date?day={int(nap)}&month={int(honap)}"
        response = requests.get(url)
        adat = response.json()
          #  a 'data' kulcs alatt vannak országkódok
        nev_str = adat.get("data", {}).get(orszag_kod.lower(), "")
        if nev_str:
            return [nev.strip() for nev in nev_str.split(",")]
        else:
            return []
    except Exception as e:
        print(f"Hiba történt: {e}")
        return []