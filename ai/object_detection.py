import cv2
import torch

model = torch.hub.load("ultralytics/yolov5", "yolov5s")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    results = model(frame)

    annotated = results.render()[0]
    cv2.imshow("YOLO Object Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
