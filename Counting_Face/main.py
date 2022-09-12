import cv2
import numpy as np
import dlib

# Muda o caminho do vídeo
webcam = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while 1:
    # Capturar quadro a quadro
    ret, frame = webcam.read()
    # Inverter a matriz 2D
    frame = cv2.flip(frame, 1)
    # converter a imagem de um espaço de cores para outro
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    i = 0

    for face in faces: 
        start_point = face.left(), face.top() # Canto superior esquerdo do retângulo
        end_point = face.right(), face.bottom() # Canto inferior direito do retângulo
        color_rectangle = (124,252,0) # RGB
        color_text = (0, 26, 255) # RGB ordem inversa
        thickness = 1 # Espessura da linha
        i += 1
        cv2.rectangle(frame, start_point, end_point, color_rectangle, thickness) # Desenhar um retângulo
        cv2.putText(frame, f"       CABECAO {i}", (start_point[0]-5, start_point[1]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_text, 1)

    cv2.imshow("Camera", frame) # Exibindo a imagem

    if cv2.waitKey(5) == (27): # Para o programa (ESC)
        break

# Desliga a janela
webcam.release()
cv2.destroyAllWindows()