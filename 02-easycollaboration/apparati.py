

STATI_AMMESSI = ("OK", "ATTENZIONE", "OFFLINE")

APPARATI = {
    "NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
    "COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
    "SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}

Apparato = {}

def aggiungi_apparato(codice: str, nome: str, bus: str, stato: str) -> bool:
    
    if codice in APPARATI or stato not in STATI_AMMESSI:
        return False
    else if APPARATI[codice] = {"nome": nome, "bus": bus, "stato": stato}
        return True


def aggiorna_stato(codice: str, stato: str) -> bool:
    
    if codice not in APPARATI or stato not in STATI_AMMESSI:
        return False
    
    APPARATI[codice]["stato"] = stato_normalizzato
    return True