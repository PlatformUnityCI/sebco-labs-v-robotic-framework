# Escenarios Gherkin

Feature: Login en App Ualá con Visión Artificial
  Como un QA Engineer
  Quiero validar el acceso a la Home de Ualá
  Usando detección visual y hardware robótico

  @smoke @uala
  Scenario: Login exitoso mediante reconocimiento de botones
    Given que la cámara del robot detecta la pantalla de Inicio
    When el sistema identifica el botón "btn_login_uala"
    And el brazo robótico presiona las coordenadas detectadas
    Then el sistema debe validar la presencia del logo "home_logo_uala"