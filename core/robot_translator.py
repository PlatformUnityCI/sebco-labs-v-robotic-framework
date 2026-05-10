# Mocks de movimiento y coordenadas

class RobotTranslator:
    """
    Capa de abstracción de hardware (HAL).
    Traduce coordenadas de píxeles a comandos para el actuador físico.
    """

    def move_to(self, x, y):
        """
        Simula el movimiento del brazo robótico a una coordenada específica.
        """
        print(f"[ROBOT] Moviendo actuador físico a posición: X={x}, Y={y}")
        return True

    def tap(self):
        """
        Simula la acción física de presionar la pantalla.
        """
        print("[ROBOT] Ejecutando TAP físico en pantalla.")
        return True