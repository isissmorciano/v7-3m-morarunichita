"""
Test suite per verifica v7 - Torneo Calcio
"""

import sys
import os

# Aggiungi il path al package
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import pytest
from torneo.squadre import (
    crea_squadra, info_squadra, punti_squadra,
    differenza_reti, aggiorna_statistiche
)
from torneo.partite import (
    crea_partita, info_partita, applica_partita
)


class TestSquadre:
    """Test modulo squadre.py"""
    
    def test_crea_squadra(self):
        """Test creazione squadra"""
        s = crea_squadra("Inter", "Milano", 23)
        assert s["nome"] == "Inter"
        assert s["città"] == "Milano"
        assert s["giocatori"] == 23
        assert s["vittorie"] == 0
        assert s["pareggi"] == 0
        assert s["sconfitte"] == 0
        assert s["gol_segnati"] == 0
        assert s["gol_subiti"] == 0
    
    def test_punti_squadra(self):
        """Test calcolo punti"""
        s = crea_squadra("Inter", "Milano", 23)
        assert punti_squadra(s) == 0
        
        s["vittorie"] = 2
        s["pareggi"] = 1
        assert punti_squadra(s) == 7  # 2*3 + 1*1
    
    def test_differenza_reti(self):
        """Test differenza reti"""
        s = crea_squadra("Inter", "Milano", 23)
        s["gol_segnati"] = 10
        s["gol_subiti"] = 4
        assert differenza_reti(s) == 6
    
    def test_aggiorna_statistiche_vittoria(self):
        """Test aggiornamento dopo vittoria"""
        s = crea_squadra("Inter", "Milano", 23)
        aggiorna_statistiche(s, 2, 1)
        
        assert s["vittorie"] == 1
        assert s["pareggi"] == 0
        assert s["sconfitte"] == 0
        assert s["gol_segnati"] == 2
        assert s["gol_subiti"] == 1
    
    def test_aggiorna_statistiche_pareggio(self):
        """Test aggiornamento dopo pareggio"""
        s = crea_squadra("Inter", "Milano", 23)
        aggiorna_statistiche(s, 2, 2)
        
        assert s["vittorie"] == 0
        assert s["pareggi"] == 1
        assert s["sconfitte"] == 0
        assert s["gol_segnati"] == 2
        assert s["gol_subiti"] == 2
    
    def test_aggiorna_statistiche_sconfitta(self):
        """Test aggiornamento dopo sconfitta"""
        s = crea_squadra("Inter", "Milano", 23)
        aggiorna_statistiche(s, 0, 2)
        
        assert s["vittorie"] == 0
        assert s["pareggi"] == 0
        assert s["sconfitte"] == 1
        assert s["gol_segnati"] == 0
        assert s["gol_subiti"] == 2
    
    def test_info_squadra(self):
        """Test info squadra formattata"""
        s = crea_squadra("Inter", "Milano", 23)
        aggiorna_statistiche(s, 2, 1)
        aggiorna_statistiche(s, 3, 0)
        aggiorna_statistiche(s, 0, 1)
        
        info = info_squadra(s)
        assert "Inter" in info
        assert "Milano" in info
        assert "5" in info  # gol (2+3)
        assert "6" in info  # punti (2*3)


class TestPartite:
    """Test modulo partite.py"""
    
    def test_crea_partita(self):
        """Test creazione partita"""
        p = crea_partita("Inter", "Milan", 2, 1, "2026-05-01")
        assert p["squadra1"] == "Inter"
        assert p["squadra2"] == "Milan"
        assert p["gol1"] == 2
        assert p["gol2"] == 1
        assert p["data"] == "2026-05-01"
    
    def test_info_partita(self):
        """Test info partita formattata"""
        p = crea_partita("Inter", "Milan", 2, 1, "2026-05-01")
        info = info_partita(p)
        assert "Inter" in info
        assert "Milan" in info
        assert "2" in info
        assert "1" in info
        assert "2026-05-01" in info
    
    def test_applica_partita(self):
        """Test applicazione partita e aggiornamento squadre"""
        s1 = crea_squadra("Inter", "Milano", 23)
        s2 = crea_squadra("Milan", "Milano", 22)
        squadre = [s1, s2]
        
        p1 = crea_partita("Inter", "Milan", 2, 1, "2026-05-01")
        
        # Applica partita
        applica_partita(squadre, p1)
        
        # Verifica Inter: 1V = 3 punti
        assert punti_squadra(squadre[0]) == 3
        assert squadre[0]["gol_segnati"] == 2
        assert squadre[0]["gol_subiti"] == 1


class TestIntegration:
    """Test integrazione fra moduli"""
    
    def test_soluzione_completa(self):
        """Test che la soluzione esegue correttamente"""
        # Crea 6 squadre
        s1 = crea_squadra("Inter", "Milano", 23)
        s2 = crea_squadra("Milan", "Milano", 22)
        s3 = crea_squadra("Juventus", "Torino", 25)
        s4 = crea_squadra("Roma", "Roma", 20)
        s5 = crea_squadra("Napoli", "Napoli", 21)
        s6 = crea_squadra("Lazio", "Roma", 19)
        
        squadre = [s1, s2, s3, s4, s5, s6]
        
        # Crea 8 partite
        partite = [
            crea_partita("Milan", "Inter", 2, 1, "2026-04-01"),
            crea_partita("Juventus", "Roma", 3, 0, "2026-04-02"),
            crea_partita("Napoli", "Lazio", 2, 2, "2026-04-03"),
            crea_partita("Inter", "Juventus", 1, 1, "2026-04-08"),
            crea_partita("Milan", "Roma", 2, 0, "2026-04-09"),
            crea_partita("Napoli", "Juventus", 1, 2, "2026-04-10"),
            crea_partita("Milan", "Lazio", 3, 1, "2026-04-15"),
            crea_partita("Inter", "Napoli", 1, 1, "2026-04-16"),
        ]
        
        # Applica tutte le partite
        for partita in partite:
            applica_partita(squadre, partita)
        
        # Verifica che Milan sia primo
        milan = squadre[1]
        assert punti_squadra(milan) == 9  # Milan: 3 vittorie
        
        # Verifica che tutte le squadre siano state aggiornate
        assert len(squadre) == 6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
