


import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # En Windows CAP_DSHOW ayuda

if not cap.isOpened():
    raise SystemExit("No se pudo abrir la cámara (prueba con 1, 2...).")

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)  # ← des-espeja (flip horizontal)

    cv2.imshow("Cam", frame)
    if cv2.waitKey(1) == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
