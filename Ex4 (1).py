import cv2

cap = cv2.VideoCapture(1)

while True:
    _, vid = cap.read()

    cv2.imshow("Camera", vid)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()