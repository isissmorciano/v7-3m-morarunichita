# v7-3m

## Setup per la Verifica

Seguire questi step **nell'ordine** per minimizzare il tempo di connessione a internet.

### 1. Creare la cartella workspace
```bash
mkdir workspace
cd workspace
```

### 2. Creare il virtual environment
```bash
# Cartella corrente: workspace/
python -m venv .venv
```

### 3. Attivare e installare i packages
**Su Linux/Mac:**
```bash
# Cartella corrente: workspace/
source .venv/bin/activate
pip install matplotlib
```

**Su Windows (PowerShell):**
```powershell
# Cartella corrente: workspace/
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
.venv/Scripts/activate
pip install matplotlib
```

### 4. Clonare il repository
```bash
# Cartella corrente: workspace/
git clone <repo-url>
```

### 5. Copiare il venv dentro al repository
**Su Linux/Mac:**
```bash
# Cartella corrente: workspace/ (rimani qui!)
cp -r .venv v7-3m/
```

**Su Windows (PowerShell):**
```powershell
# Cartella corrente: workspace/ (rimani qui!)
Copy-Item -Recurse .venv v7-3m
```

### 6. ⚠️ **STACCARE INTERNET QUI**

### Struttura finale dopo tutti gli step

```
workspace/                    ← cartella principale
├── .venv/                    ← venv originale
└── v7-3m/                    ← repository clonato (dentro workspace)
    ├── .venv/                ← copia del venv
    ├── torneo/
    ├── v7_test.py
    ├── v7_student.py
    ├── v7_solution.py
    ├── v7.md
    └── README.md
```

### 7. Per i ragazzi: usare il progetto
```bash
cd v7-3m
source .venv/bin/activate    # su Linux/Mac
# .venv/Scripts/activate     # su Windows
python v7_test.py
```