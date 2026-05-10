# 🤖 Sebco Labs - Robotic Automation Framework
**Project Context & Architecture for AI Assistance**

## 1. Objetivo del Proyecto
Migración y automatización de casos de prueba para la App Ualá utilizando **Visión Artificial No Determinística**. El sistema busca reemplazar la interacción manual y los selectores tradicionales (XPath/ID) por una ejecución física basada en reconocimiento visual y coordenadas normalizadas.

## 2. Infraestructura de Hardware (Setup Físico)
* **Estación de Trabajo:** macOS M1 (Host de procesamiento y ejecución de scripts).
* **Device Under Test (DUT):** Samsung SM-A15 (Ejecuta la App Ualá).
* **Sensor Visual (Cámara):** Samsung SM-A13 (Actúa como "ojos" del sistema).
* **Puente de Video:** Iriun Webcam (Conecta el A13 con macOS vía Wi-Fi/USB).
* **Sistema de Referencia:** Marcadores ArUco (IDs 0, 1, 2, 3) pegados físicamente en las esquinas del SM-A15.

## 3. Stack Tecnológico
* **Lenguaje:** Python 3.9+
* **Librerías Core:** * `OpenCV`: Detección de ArUco, Homografía, Template Matching.
    * `NumPy`: Manejo de matrices para corrección de perspectiva.
* **Framework de Testing:** `Pytest-BDD` (Gherkin).
* **Componentes Internos:**
    * `VisionEngine.py`: Motor principal. Procesa el feed, aplica filtros CLAHE para mitigar reflejos y normaliza clics mediante la matriz de homografía.
    * `capture_assets.py`: Herramienta para recortar y guardar templates visuales (assets).

## 4. Flujo de Trabajo (Workflow)
1.  **Calibración:** El `VisionEngine` detecta los 4 marcadores ArUco para enderezar la imagen del DUT.
2.  **Mapeo:** Se capturan los elementos de la UI (botones, campos) como imágenes `.png` en la carpeta `/assets`.
3.  **Ejecución:** Los Step Definitions de Gherkin llaman al motor para buscar un asset y devolver la coordenada exacta de acción.

## 5. Limitaciones y Desafíos Técnicos
* **Latencia:** Posible delay en el feed de Iriun (optimizar mediante conexión USB si es necesario).
* **Iluminación:** Sensibilidad a reflejos en la pantalla del SM-A15 (uso crítico de CLAHE).
* **DPI/Resolución:** Los assets deben capturarse en la misma resolución de pantalla en la que se ejecutarán los tests.

## 6. Instrucciones para la IA
* Priorizar código robusto que maneje excepciones de visión (ej. ArUco no encontrado).
* Generar Step Definitions que utilicen coordenadas relativas calculadas por la matriz de homografía.
* Mantener un enfoque modular en la creación de nuevos flujos de prueba.

## 7. Perfil Técnico del Operador
* **Rol:** Senior QA Automation Analyst.
* **Especialidad:** Automatización de productos digitales complejos y flujos transaccionales.
* **Dominio de Negocio:** Fintech (Pagos QR, Microservicios bancarios, Open Banking).
* **Stack Tecnológico:**
    * **Frameworks:** Selenium, Appium, Pytest-BDD.
    * **Herramientas:** Postman (API Testing), GitHub Actions, Jenkins.
    * **Core:** Python para desarrollo de herramientas de soporte (R&D).

## 8. Sebco Labs - Objetivos de Automatización
* **Foco:** Creación de frameworks de soporte que integren hardware y software.
* **Metodología:** Desarrollo dirigido por especificaciones (Spec Driven Development) enfocado en la migración de flujos manuales a automatización por visión computarizada.