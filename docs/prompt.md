Te explicaste perfecto.
Lo que querés en realidad es un **prompt de lineamientos editoriales/técnicos** para generar documentación profesional, moderna y limpia, evitando el exceso de “épica enterprise”.

Te dejo uno bastante sólido y reutilizable para cualquier proyecto:

---

# Prompt — Estilo de documentación técnica profesional para proyectos de software

Generá documentación técnica en formato Markdown (`.md`) con un estilo profesional, limpio y mantenible.

## Objetivo del estilo

La documentación debe sentirse:

* técnica,
* clara,
* moderna,
* seria,
* fácil de escanear,
* orientada a onboarding y mantenimiento real.

Evitar tono:

* corporativo exagerado,
* marketinero,
* “tech manifesto”,
* grandilocuente,
* excesivamente dramático.

La prioridad es:

1. claridad,
2. precisión,
3. mantenibilidad,
4. legibilidad rápida.

---

# Reglas de redacción

## Tono

Usar un tono:

* técnico,
* directo,
* profesional,
* sobrio.

Evitar:

* adjetivos exagerados,
* épica innecesaria,
* frases absolutas,
* lenguaje inflado.

NO usar frases como:

* “blindaje absoluto”
* “sanitización quirúrgica”
* “garantía matemática”
* “infraestructura enterprise”
* “core operacional crítico”

Preferir:

* explicaciones concretas,
* precisión técnica,
* lenguaje neutral.

---

# Estructura del documento

Organizar el `.md` en secciones claras usando:

```md
# Título principal
## Sección
### Subsección
```

Mantener:

* separación visual,
* bloques cortos,
* listas simples,
* párrafos breves.

Cada sección debe tener:

* propósito claro,
* explicación breve,
* comandos o ejemplos concretos.

---

# Formato visual

Usar:

* bloques de código bien separados,
* listas con bullets,
* tablas solo si realmente ayudan,
* divisores `---` entre secciones importantes.

Evitar:

* paredes enormes de texto,
* párrafos demasiado largos,
* narrativa innecesaria.

---

# Código y comandos

Todos los comandos deben:

* ser reales,
* ejecutables,
* minimalistas,
* estar contextualizados.

Ejemplo correcto:

```bash
pip install pip-tools
```

Explicar brevemente:

* qué hace,
* por qué se usa.

No sobreexplicar cosas obvias.

---

# Explicaciones técnicas

Explicar:

* el “por qué” de una decisión,
* riesgos reales,
* beneficios concretos.

Evitar exageraciones técnicas.

Ejemplo:

* NO decir:
  “seguridad absoluta de supply chain”
* SÍ decir:
  “mejora reproducibilidad y validación de integridad”

---

# Dependencias y herramientas

Cuando describas librerías o herramientas:

* explicar función real,
* justificar brevemente por qué fueron elegidas,
* evitar marketing técnico.

Formato recomendado:

## pytest

Framework principal de testing.

Se utiliza para:

* ejecutar pruebas automatizadas,
* organizar suites de testing,
* integrar fixtures.

Fue elegido por:

* simplicidad,
* ecosistema,
* compatibilidad con automatización.

---

# Diseño visual sutil

Se permite usar HTML inline para resaltar elementos importantes.

Usar colores de forma moderada y elegante.

Ejemplo recomendado:

```md
<span style="color:#B0005A;"><strong>macOS (ARM64 e Intel)</strong></span>
```

Reglas:

* usar bordó/fucsia oscuro para warnings o compatibilidad,
* evitar colores saturados en exceso,
* no abusar de highlights visuales.

---

# Filosofía general

La documentación debe sentirse:

* escrita por un engineer senior,
* mantenida para un equipo real,
* útil dentro de un repositorio vivo.

Debe priorizar:

* claridad operativa,
* velocidad de lectura,
* mantenimiento futuro,
* onboarding técnico.

No escribir para impresionar.
Escribir para que otro engineer pueda trabajar rápido y entender el sistema sin fricción.
