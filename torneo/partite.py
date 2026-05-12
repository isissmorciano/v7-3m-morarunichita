from .squadre import aggiorna_statistiche

# ### Modulo `partite.py`

# Una partita è rappresentata da un dizionario con:
# - `squadra1`: nome squadra 1
# - `squadra2`: nome squadra 2
# - `gol1`: gol segnati da squadra1
# - `gol2`: gol segnati da squadra2
# - `data`: data della partita (stringa "YYYY-MM-DD")

# **Funzioni da implementare:**

# 1. **`crea_partita(squadra1, squadra2, gol1, gol2, data)`**  
#    Crea una partita.

# 2. **`info_partita(partita)`**  
#    Restituisce stringa formattata.  
#    Es: `"Inter 2 - 1 Milan (2026-05-07)"`

# 3. **`giocate_per_squadra(partite, nome_squadra)`**  
#    Restituisce numero di partite giocate da una squadra.

# 4. **`gol_totali_squadra(partite, nome_squadra)`**  
#    Restituisce gol segnati da una squadra in tutte le partite.

# 6. **`applica_partita(squadre, partita)`**  
#    Aggiorna le statistiche di due squadre dopo una partita.  
#    Cerca le squadre per nome e chiama `aggiorna_statistiche` per entrambe.
      
def crea_partita(squadra1, squadra2, gol1, gol2, data):
    partita = {
        "squadra1": squadra1,
        "squadra2": squadra2,
        "gol1": gol1,
        "gol2": gol2,
        "data": data
    }
    return partita

def info_partita(partita):
    testo = f"{partita["squadra1"]} {partita["gol1"]} {partita["gol2"]} {partita["squadra2"]} {partita["data"]}"
    return testo

def giocate_per_squadra(partite, nome_squadra):
    contatore = 0
    for partita in partite:
        if partita["squadra1"] == nome_squadra or partita["squadra2"] == nome_squadra:
            contatore = contatore + 1
    return contatore

def gol_totali_squadra(partite, nome_squadra):
    totale_gol = 0
    for partita in partite:
        if partita ["squadra1"] == nome_squadra:
            totale_gol = totale_gol + partita["gol1"]
        if partita ["squadra2"] == nome_squadra:
            totale_gol = totale_gol + partita["gol2"]
    return totale_gol

def applica_partita(squadre, partita):
    aggiorna_statistiche(squadre, partita)

if __name__ == "__main__":
    p1 = crea_partita("Inter", "Milan", 2, 1, "(2026-05-07)")
    p2 = crea_partita("Juve", "Inter", 1, 1, "(2026-05-10)")

    lista_partite = [p1, p2]

    print("Info partita 1: ")
    print("info_partita(p1)")
    