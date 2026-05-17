# DOCUMENTACIÓN TÉCNICA: CONFIGURACIÓN DEL ENTORNO PYTHON EN macOS

**Proyecto:** `sebco-labs-v-robotic-framework`

> [!NOTE]
> Esta guía fue validada únicamente sobre <span style="color:#B0005A;">macOS (ARM64 e Intel)</span>. Algunos comandos o rutas pueden requerir ajustes en Linux o Windows.

---

# 1. Objetivo

Este documento define un flujo reproducible para administrar dependencias Python utilizando:

- `pip-tools`
- hashes SHA-256
- entornos virtuales aislados

El objetivo es:

- evitar diferencias de versiones entre entornos,
- mejorar la reproducibilidad,
- reducir problemas derivados de dependencias inconsistentes,
- mantener el entorno limpio y controlado.

---

# 2. Información del entorno

- **Sistema Operativo:** macOS
- **Python:** 3.14
- **Gestión de dependencias:** `pip-tools`
- **Entorno virtual:** `.venv`

---

# 3. ¿Por qué usar hashes?

Instalar paquetes directamente con `pip install` puede generar diferencias entre máquinas o pipelines debido a cambios en versiones secundarias o dependencias transitivas.

El uso de hashes permite:

- validar la integridad de los paquetes descargados,
- garantizar instalaciones reproducibles,
- detectar modificaciones inesperadas en dependencias.

---

# 4. Configuración del entorno

## Paso 1: eliminar el entorno virtual existente

Desde la raíz del proyecto:

```bash
rm -rf .venv
```

Esto elimina únicamente el entorno virtual local.
No afecta:

- código fuente,
- archivos `.feature`,
- repositorio Git,
- documentación del proyecto.

---

## Paso 2: crear y activar el entorno virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno
source .venv/bin/activate

# Actualizar pip
python -m pip install --upgrade pip
```

---

## Paso 3: instalar pip-tools

```bash
pip install pip-tools
```

`pip-tools` permite:

- resolver dependencias transitivas,
- generar archivos bloqueados (`requirements.txt`),
- administrar hashes automáticamente.

---

# 5. Definición de dependencias

Crear `requirements.in` en la raíz del proyecto:

```text
# --- Visión y automatización ---
opencv-python
numpy
pillow
pytesseract

# --- Testing BDD ---
pytest
pytest-bdd

# --- Documentación ---
mkdocs-material
mkdocstrings[python]
```

Este archivo debe contener únicamente dependencias principales.

---

# 6. Generación de requirements.txt

Ejecutar:

```bash
pip-compile --generate-hashes requirements.in
```

El comando:

- resuelve dependencias secundarias,
- fija versiones exactas,
- agrega hashes SHA-256.

Ejemplo:

```text
numpy==2.4.5 \
    --hash=sha256:... \
    --hash=sha256:...
```

---

# 7. Instalación reproducible

Instalar dependencias utilizando hashes:

```bash
pip install --require-hashes -r requirements.txt
```

Esto fuerza a que cada paquete coincida exactamente con los hashes definidos.

---

# 8. Workflow recomendado

El flujo de mantenimiento recomendado es:

```text
requirements.in
        │
        ▼
pip-compile
        │
        ▼
requirements.txt
        │
        ▼
pip-sync
```

---

# 9. Uso de pip-sync

Para sincronizar el entorno virtual:

```bash
pip-sync requirements.txt
```

A diferencia de `pip install`, `pip-sync`:

- instala dependencias faltantes,
- actualiza versiones necesarias,
- elimina paquetes que ya no existen en `requirements.txt`.

Esto ayuda a evitar dependencias obsoletas o inconsistentes dentro del entorno virtual.

---

# 10. Recomendaciones

- No editar manualmente `requirements.txt`.
- Modificar únicamente `requirements.in`.
- Regenerar `requirements.txt` después de cada cambio.
- Versionar ambos archivos en Git.
- Mantener el entorno virtual fuera del repositorio (`.gitignore`).

---

# 11. Herramientas utilizadas

## pip-tools

Se utiliza para:

- compilar dependencias reproducibles,
- resolver dependencias transitivas,
- generar hashes SHA-256,
- mantener sincronizado el entorno.

Fue elegido porque simplifica el manejo de dependencias sin incorporar la complejidad de herramientas más pesadas como Poetry o Pipenv.

---

## pytest

Framework principal de testing.

Se utiliza para:

- ejecutar pruebas automatizadas,
- organizar suites de testing,
- integrar fixtures y validaciones.

Fue elegido por su simplicidad, ecosistema y compatibilidad con automatización.

---

## pytest-bdd

Extensión BDD sobre `pytest`.

Permite:

- escribir escenarios en formato Gherkin,
- separar comportamiento de implementación,
- facilitar lectura funcional de pruebas.

---

## opencv-python

Biblioteca de visión por computadora.

Se utiliza para:

- procesamiento de imágenes,
- captura y análisis visual,
- automatización basada en reconocimiento visual.

---

## pytesseract

Wrapper de Tesseract OCR para Python.

Permite extraer texto desde imágenes o capturas.

---

## pillow

Biblioteca de manipulación de imágenes.

Se utiliza como complemento liviano para transformaciones simples y procesamiento auxiliar.

---

## mkdocs-material

Framework de documentación estática.

Permite:

- generar documentación navegable,
- publicar documentación técnica,
- mantener documentación versionable dentro del repositorio.

---

## mkdocstrings

Extensión para documentación automática de código Python.

Permite generar documentación directamente desde docstrings.

---

# 12. Mejora futura

Actualmente puede utilizarse `flake8` para validaciones estáticas.

Como mejora futura podría evaluarse una migración a `ruff` para:

- mejorar performance,
- unificar linting y formateo,
- simplificar configuración y mantenimiento.

La migración queda planteada como una posible evolución del entorno, no como una necesidad inmediata.

