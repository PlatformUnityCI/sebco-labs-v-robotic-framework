# OpenCV, Canny, ArUco y OCR

import cv2
import numpy as np
import pytesseract

class VisionEngine:
    """
    Motor de procesamiento de imágenes para automatización no determinística.
    Incluye filtros para variaciones de iluminación y corrección de perspectiva.
    """

    def __init__(self):
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        self.aruco_params = cv2.aruco.DetectorParameters()

    def preprocess_for_light(self, frame):
        """
        Aplica CLAHE para normalizar la iluminación y reducir flakiness.
        """
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        return cv2.cvtColor(cv2.merge((cl,a,b)), cv2.COLOR_LAB2BGR)

    def get_canny_edges(self, frame):
        """
        Detección de bordes para fallbacks cuando el color se satura por brillo.
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)

    def find_element_by_template(self, screen, template_path, threshold=0.8):
        """
        Busca un elemento visual (template) dentro de la captura actual.
        Retorna coordenadas (x, y) relativas al centro del elemento.
        """
        template = cv2.imread(template_path)
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        
        if max_val >= threshold:
            h, w = template.shape[:2]
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            return (center_x, center_y, max_val)
        return None