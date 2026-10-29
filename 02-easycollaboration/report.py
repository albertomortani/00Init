RegistroApparati = {}


def filtra_per_stato(apparati: dict, stato: str) -> list:
    return [apparato for apparato in apparati.values() if apparato["stato"] == stato]


def filtra_per_bus(apparati: dict, bus: str) -> list:
    return [apparato for apparato in apparati.values() if apparato["bus"] == bus]