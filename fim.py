import hashlib
import os
import json

def calcular_hash(ruta_archivo, algoritmo='sha256'):
    """Calcula el hash SHA-256 de un archivo en bloques de 4KB."""
    hash_func = getattr(hashlib, algoritmo)()
    try:
        with open(ruta_archivo, 'rb') as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hash_func.update(bloque)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None

def crear_linea_base(directorio, archivo_base):
    """Escanea el directorio y guarda los hashes originales en JSON."""
    linea_base = {}
    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            linea_base[ruta_completa] = calcular_hash(ruta_completa)
    with open(archivo_base, 'w') as f:
        json.dump(linea_base, f, indent=4)
    print(f"[*] Línea base creada en: {archivo_base}")

def verificar_integridad(directorio, archivo_base):
    """Compara hashes actuales contra la línea base guardada."""
    with open(archivo_base, 'r') as f:
        linea_base = json.load(f)
    archivos_actuales = set()
    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            archivos_actuales.add(ruta_completa)
            if ruta_completa not in linea_base:
                print(f"[ALERTA] Archivo NUEVO: {ruta_completa}")
            elif calcular_hash(ruta_completa) != linea_base[ruta_completa]:
                print(f"[ALERTA] Archivo MODIFICADO: {ruta_completa}")
            else:
                print(f"[OK] Intacto: {ruta_completa}")
    for ruta in linea_base:
        if ruta not in archivos_actuales:
            print(f"[ALERTA] Archivo ELIMINADO: {ruta}")