import os

def leer_cloro_simulado():
    if not os.getenv("PLC_PASSWORD"):
        raise RuntimeError("Falta la variable PLC_PASSWORD")

    return {
        "planta": "Maipo Sur - laboratorio",
        "cloro_mg_l": 0.7
    }
