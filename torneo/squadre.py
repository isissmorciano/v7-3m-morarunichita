# ## Esercizio: Gestione Torneo Calcio

# Realizzi un package Python che modella un **torneo di calcio** con **squadre** e **partite** giocate.

# ### Modulo `squadre.py`

# Una squadra è rappresentata da un dizionario con:
# - `nome`: nome della squadra
# - `città`: città di provenienza
# - `giocatori`: numero di giocatori in rosa
# - `vittorie`: numero di partite vinte
# - `pareggi`: numero di pareggi
# - `sconfitte`: numero di partite perse
# - `gol_segnati`: totale goal fatti
# - `gol_subiti`: totale goal subiti

# **Funzioni da implementare:**

# 1. **`crea_squadra(nome, città, giocatori)`**  
#    Crea una squadra con statistiche iniziali a 0.

# 2. **`info_squadra(squadra)`**  
#    Restituisce una stringa formattata con tutte le informazioni della squadra.  
#    Es: `"Inter (Milano) | 10 gol | 25 vittorie, 3 pareggi, 2 sconfitte"`

# 3. **`punti_squadra(squadra)`**  
#    Calcola i punti totali: vittorie * 3 + pareggi * 1.

# 4. **`differenza_reti(squadra)`**  
#    Calcola la differenza tra gol segnati e gol subiti.

# 5. **`aggiorna_statistiche(squadra, gol_fatti, gol_subiti)`**  
#    Aggiorna i dati della squadra dopo una partita:
#    - Se `gol_fatti > gol_subiti`: +1 vittoria
#    - Se `gol_fatti == gol_subiti`: +1 pareggio
#    - Se `gol_fatti < gol_subiti`: +1 sconfitta
#    - Aggiorna gol segnati e subiti

def crea_squadra(nome, città, giocatori):
    squadra = {
        "nome": nome,
        "città": città,
        "giocatori": giocatori,
        "vittorie": 0,
        "pareggi": 0,
        "sconfitte": 0,
        "gol_segnati": 0,
        "gol_subiti": 0
    }
    squadra["gol_subiti"] = 0
    return squadra

def info_squadra(squadra):
    testo = f"{squadra["nome"]} ({squadra["città"]}) | {squadra["gol_segnati"]} gol | {squadra["vittorie"]} vittorie, {squadra["pareggi"]} pareggi, {squadra["sconfitte"]} sconfitte"
    return testo

def punti_squadra(squadra):
    punti = (squadra["vittorie"] *3) + (squadra["pareggi"] *1)
    return punti

def differenza_reti(squadra):
    differenza = squadra["gol_segnati"] - squadra["gol_subiti"]
    return differenza

def aggiorna_statistiche(squadra, gol_fatti, gol_subiti):
    squadra["gol_segnati"] = squadra["gol_segnati"] + gol_fatti
    squadra["gol_subiti"] = squadra["gol_subiti"] + gol_subiti

    if gol_fatti > gol_subiti:
        squadra["vittorie"] = squadra["vittorie"] + 1
    elif gol_fatti == gol_subiti:
        squadra["pareggi"] = squadra["pareggi"] + 1
    else:
        squadra["sconfitte"] = squadra["sconfitte"] + 1

if __name__ == "__main__":
    mia_squadra = crea_squadra("Inter", "Milano", 25)

    aggiorna_statistiche(mia_squadra, 3, 1)
    aggiorna_statistiche(mia_squadra, 1, 1)

    print("Informazioni squadra:")
    print(info_squadra(mia_squadra))

    print("/nPunti totali: ")
    print(punti_squadra(mia_squadra))

    print()