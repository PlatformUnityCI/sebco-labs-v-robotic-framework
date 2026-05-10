import cv2
import os

# Configuración
ASSETS_PATH = "assets/"
if not os.path.exists(ASSETS_PATH):
    os.makedirs(ASSETS_PATH)

def capture_elements():
    # 0 suele ser la cámara integrada, 1 o 2 el celular conectado por cable
    cap = cv2.VideoCapture(0) 
    
    print("INSTRUCCIONES:")
    print("1. Seleccioná con el mouse el área del botón/elemento.")
    print("2. Presioná ENTER o ESPACIO para confirmar el recorte.")
    print("3. Escribí el nombre del elemento en la consola.")
    print("4. Presioná 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Captura de Assets - Framework Artesanal", frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        # Iniciar selección con el mouse
        if key == ord('s') or key == 32: # 's' o Espacio
            # Abre una ventana para recortar (ROI - Region of Interest)
            roi = cv2.selectROI("Seleccioná el elemento", frame, fromCenter=False)
            
            if roi != (0, 0, 0, 0):
                x, y, w, h = roi
                crop = frame[y:y+h, x:x+w]
                
                cv2.imshow("Recorte", crop)
                name = input("Nombre del elemento (ej: btn_login): ")
                
                if name:
                    file_path = os.path.join(ASSETS_PATH, f"{name}.png")
                    cv2.imwrite(file_path, crop)
                    print(f"✅ Guardado: {file_path}")
                
                cv2.destroyWindow("Recorte")
                cv2.destroyWindow("Seleccioná el elemento")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_elements()