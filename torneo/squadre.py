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