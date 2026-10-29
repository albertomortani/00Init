SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 860, "controlli_ok": False},
    {"codice": "I-GHI", "modello": "A220", "ore_volo": 1035, "controlli_ok": True},
    {"codice": "I-JKL", "modello": "ATR72", "ore_volo": 540, "controlli_ok": True},
]


def stampa_riepilogo(aeromobili) -> None:
    print("Ecco gli aeromobili:")

    for aeromobile in aeromobili:
        print(
            f"- {aeromobile['codice']} ({aeromobile['modello']}), "
            f"{aeromobile['ore_volo']} ore di volo, "
            f"controlli {'ok' if aeromobile['controlli_ok'] else 'non validi'}"
        )


def filtra_controlli_non_validi(aeromobili: list) -> list[dict]:

    return [
        aeromobile
        for aeromobile in aeromobili
        if aeromobile["controlli_ok"] is False
    ]


def filtra_oltre_soglia(aeromobili: list, soglia: int) -> list:

    return [
        aeromobile
        for aeromobile in aeromobili
        if isinstance(aeromobile["ore_volo"], int)
        and aeromobile["ore_volo"] > soglia
    ]

def stampa_segnalazioni(titolo: str, segnalazioni: list) -> None:
    print(f"\n{titolo}:")

    if not segnalazioni:
        print("Nessuna segnalazione.")
        return

    for aeromobile in segnalazioni:
        print(f"- {aeromobile['codice']} ({aeromobile['modello']})")


def main() -> None:
    stampa_riepilogo(aeromobili)
    stampa_segnalazioni("Aeromobili con controlli non validi", filtra_controlli_non_validi(aeromobili))
    stampa_segnalazioni(f"Aeromobili oltre la soglia di {SOGLIA_ORE} ore", filtra_oltre_soglia(aeromobili, SOGLIA_ORE))

if __name__ == "__main__":
    main()
