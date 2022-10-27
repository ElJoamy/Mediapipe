import cv2
import numpy as np
import mediapipe as mp
  
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# configuracion de la camara
mp_face_mesh = mp.solutions.face_mesh
face_mesh =  mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
  
img = cv2.imread('filters/face.jpg', cv2.IMREAD_UNCHANGED)
image = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
# Para mejorar el rendimiento, podemos cambiar el tamaño de la imagen de entrada
image.flags.writeable = False
results =  face_mesh.process(image)


# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break
