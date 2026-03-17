<div align="center">

```
███████╗██╗███╗   ███╗    ██╗   ██╗███████╗██████╗ ██╗███████╗██╗███████╗██████╗ 
██╔════╝██║████╗ ████║    ██║   ██║██╔════╝██╔══██╗██║██╔════╝██║██╔════╝██╔══██╗
█████╗  ██║██╔████╔██║    ██║   ██║█████╗  ██████╔╝██║█████╗  ██║█████╗  ██████╔╝
██╔══╝  ██║██║╚██╔╝██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝  ██║██╔══╝  ██╔══██╗
██║     ██║██║ ╚═╝ ██║     ╚████╔╝ ███████╗██║  ██║██║██║     ██║███████╗██║  ██║
╚═╝     ╚═╝╚═╝     ╚═╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
```

# 🔐 File Integrity Monitor — FIM Tool

**Herramienta de monitoreo de integridad de archivos en tiempo real.**  
Detecta archivos nuevos, modificados o eliminados usando criptografía SHA-256.

---

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Security](https://img.shields.io/badge/Category-Cybersecurity-00ff41?style=for-the-badge&logo=shield&logoColor=white)](https://github.com/)
[![Hashing](https://img.shields.io/badge/Algoritmo-SHA--256-red?style=for-the-badge&logo=hashnode&logoColor=white)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)](https://github.com/)

</div>

---

## 📌 ¿Qué es este proyecto?

Un **File Integrity Monitor (FIM)** es una herramienta de seguridad defensiva que protege archivos críticos del sistema detectando cualquier alteración no autorizada.

Funciona calculando una **firma criptográfica única (hash SHA-256)** para cada archivo. Si un atacante modifica, inyecta o elimina un archivo — aunque sea un solo carácter — el hash cambia completamente y la herramienta emite una alerta inmediata.

```
Archivo Original  →  SHA-256  →  a3f9d2c1e8b47...  ✅ INTACTO
Archivo Alterado  →  SHA-256  →  f7c2a1b9e4d83...  🚨 ALERTA
```

> 💡 Esta es la misma lógica usada por herramientas enterprise como **Tripwire**, **OSSEC** y **Wazuh**.

---

## 🎯 Casos de uso reales

| Escenario | Descripción |
|-----------|-------------|
| 🦠 **Detección de malware** | Identifica si un ejecutable del sistema fue reemplazado |
| 🔑 **Auditoría de accesos** | Detecta modificaciones no autorizadas en archivos de configuración |
| 📋 **Compliance** | Cumplimiento de estándares como PCI-DSS, HIPAA, ISO 27001 |
| 🔍 **Forense digital** | Verifica si archivos fueron alterados tras un incidente |

---

## ⚙️ ¿Cómo funciona?

```
┌─────────────────────────────────────────────────────────┐
│                    FLUJO DE OPERACIÓN                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  OPCIÓN 1 — Crear Línea Base                            │
│  ─────────────────────────                              │
│  📁 Directorio  →  🔢 SHA-256  →  💾 JSON (baseline)   │
│                                                          │
│  OPCIÓN 2 — Verificar Integridad                        │
│  ────────────────────────────                           │
│  📁 Directorio  →  🔢 SHA-256  →  🔄 Comparar JSON     │
│                                                          │
│       ✅ Hash igual    →  Archivo INTACTO               │
│       🚨 Hash distinto →  Archivo MODIFICADO            │
│       🆕 No en JSON    →  Archivo NUEVO (inyectado)     │
│       ❌ No en disco   →  Archivo ELIMINADO             │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| `Python 3.8+` | Lenguaje principal |
| `hashlib` | Cálculo de hashes SHA-256 / MD5 |
| `os` | Navegación del sistema de archivos |
| `json` | Almacenamiento de la línea base |

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/kaleth4/file-integrity-monitor.git
cd file-integrity-monitor
```

### 2. Verificar requisitos

```bash
python --version  # Python 3.8+ requerido
# No se necesitan dependencias externas — solo librería estándar
```

### 3. Ejecutar la herramienta

```bash
python fim.py
```

---

## 💻 Demo de uso

```bash
======================================================
  Herramienta de Monitoreo de Integridad de Archivos
======================================================
1. Crear línea base de hashes (Estado seguro)
2. Verificar integridad de los archivos (Detectar cambios)
Selecciona una opción (1 o 2): 2

--- Iniciando Verificación de Integridad ---
[OK]     Archivo intacto:              ./archivos_seguros/config.txt
[OK]     Archivo intacto:              ./archivos_seguros/users.db
[ALERTA] Archivo MODIFICADO detectado: ./archivos_seguros/system.conf
[ALERTA] Archivo NUEVO detectado:      ./archivos_seguros/backdoor.exe
[ALERTA] Archivo ELIMINADO detectado:  ./archivos_seguros/audit.log
```

---

## 📂 Estructura del proyecto

```
file-integrity-monitor/
│
├── 📄 fim.py                      # Script principal
├── 📄 linea_base_hashes.json      # Base de hashes generada (auto)
├── 📁 archivos_seguros/           # Directorio a proteger (pruebas)
│   ├── config.txt
│   └── users.db
└── 📄 README.md
```

---

## 🔬 Código principal

```python
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
```

---

## 🔐 Conceptos de seguridad aplicados

| Concepto | Implementación |
|----------|---------------|
| **Criptografía** | Hash SHA-256 como firma digital de archivos |
| **Integridad de datos** | Pilar CIA — detección de alteraciones |
| **Auditoría** | Registro de estado confiable (baseline) |
| **Threat Detection** | Alertas por nuevos, modificados y eliminados |
| **Forense digital** | Evidencia de manipulación de archivos |

---

## 🔮 Mejoras futuras

- [ ] 📧 Notificaciones por email al detectar cambios
- [ ] 📊 Reporte en HTML/PDF con timestamp
- [ ] ⏱️ Modo demonio — escaneo automático cada N minutos
- [ ] 🗃️ Soporte para múltiples directorios simultáneos
- [ ] 🔑 Algoritmos adicionales: MD5, SHA-512, BLAKE2

---

## 👤 Autor

**Kaleth Corcho**  
Ingeniería de Sistemas · WolvesTI · Bogotá, Colombia

[![LinkedIn](https://img.shields.io/badge/LinkedIn-kaleth--corcho-0077B5?style=flat&logo=linkedin)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-kaleth4-181717?style=flat&logo=github)](https://github.com/kaleth4)

---

<div align="center">

**⭐ Si este proyecto te fue útil, dale una estrella**

*Proyecto de portafolio en ciberseguridad · 2026 · WolvesTI*

</div>
