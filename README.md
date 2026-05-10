# Vision-Robotic QA Framework (PoC)

Este framework ha sido diseñado para la automatización de pruebas en dispositivos físicos 
donde la detección de elementos se realiza exclusivamente mediante **Computer Vision**.

### Arquitectura Técnica
*   **Core Vision:** Utiliza OpenCV para mitigar variaciones de iluminación (filtros CLAHE) 
    y detectar bordes (Canny) cuando la saturación de color es alta.
*   **Coordinate Translation:** Un sistema de desacoplamiento que permite que la lógica 
    de test envíe comandos a un robot sin conocer la implementación del hardware.
*   **Gherkin/BDD:** Implementación vía `pytest-bdd` para asegurar que los casos de 
    negocio (como los de **Ualá**) sean legibles para perfiles no técnicos.

### Estrategia ante No-Determinismo
El sistema utiliza marcadores **ArUco** para delimitar el área de trabajo, permitiendo 
que el framework sea agnóstico al dispositivo (Samsung A13, LG, etc.) mediante 
transformaciones de homografía.

🚀 Cómo usarlo:
Instalá todo: pip install -r requirements.txt

Generá la doc: mkdocs serve (esto abrirá una web con tus docstrings).

Corré el test: pytest tests/test_uala_flows.py -s