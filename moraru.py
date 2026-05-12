# ### File principale `cognome.py`

# Nel `main()`:
# 1. Crea almeno 6 squadre di città diverse.
# 2. Crea almeno 8 partite tra queste squadre.
# 3. Per ogni partita, usa `applica_partita()` per aggiornare le squadre.
# 4. Stampa le informazioni di tutte le squadre.
# 5. Visualizza un istogramma con i punti di ogni squadra.

# **Dati di test da usare nel `main()`:**

# ```python
# # 6 squadre
# s1 = crea_squadra("Inter", "Milano", 23)
# s2 = crea_squadra("Milan", "Milano", 22)
# s3 = crea_squadra("Juventus", "Torino", 25)
# s4 = crea_squadra("Roma", "Roma", 20)
# s5 = crea_squadra("Napoli", "Napoli", 21)
# s6 = crea_squadra("Lazio", "Roma", 19)

# squadre = [s1, s2, s3, s4, s5, s6]

# # 8 partite (almeno)
# p1 = crea_partita("Milan", "Inter", 2, 1, "2026-04-01")
# p2 = crea_partita("Juventus", "Roma", 3, 0, "2026-04-02")
# p3 = crea_partita("Napoli", "Lazio", 2, 2, "2026-04-03")
# p4 = crea_partita("Inter", "Juventus", 1, 1, "2026-04-08")
# p5 = crea_partita("Milan", "Roma", 2, 0, "2026-04-09")
# p6 = crea_partita("Napoli", "Juventus", 1, 2, "2026-04-10")
# p7 = crea_partita("Milan", "Lazio", 3, 1, "2026-04-15")
# p8 = crea_partita("Inter", "Napoli", 1, 1, "2026-04-16")

# partite = [p1, p2, p3, p4, p5, p6, p7, p8]
# ```

# ---

# ## Requisiti

# - ✅ Codice pulito con commenti concisi
# - ✅ Nessun errore durante l'esecuzione (`python rossi.py`)
# - ✅ Grafico istogramma leggibile (punti per squadra)
# - ✅ Import relativi corretti tra i moduli
# - ✅ Funzioni che gestiscono i casi limite (liste vuote, nomi non trovati, ecc.)

# ---

# ## Output atteso

# ```
# CLASSIFICHE FINALI:
# - Milan (Milano) | 7 gol | 3V, 0P, 0S | Punti: 9
# - Juventus (Torino) | 5 gol | 1V, 2P, 0S | Punti: 5
# - Inter (Milano) | 3 gol | 0V, 2P, 1S | Punti: 2
# - Napoli (Napoli) | 3 gol | 0V, 2P, 1S | Punti: 2
# - Roma (Roma) | 0 gol | 0V, 0P, 2S | Punti: 0
# - Lazio (Roma) | 1 gol | 0V, 1P, 1S | Punti: 1