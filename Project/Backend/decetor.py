import cv2
import numpy as np
import time

# 🔹 Functional: Predefined object classes
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

# 🔹 Non-Functional: Accuracy depends on model quality
net = cv2.dnn.readNetFromCaffe(
    "model/deploy.prototxt",
    "model/mobilenet_iter_73000.caffemodel"
)

def detect_objects(frame):
    # 🔹 Non-Functional: Performance measurement
    start_time = time.time()

    (h, w) = frame.shape[:2]

    # 🔹 Functional: Preprocessing image for model
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)

    net.setInput(blob)

    # 🔹 Functional: Run AI model
    detections = net.forward()

    results = []

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # 🔹 Non-Functional: Accuracy control (threshold)
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # 🔹 Functional: Store detection result
            results.append({
                "label": label,
                "confidence": float(confidence),
                "box": [int(startX), int(startY), int(endX), int(endY)]
            })

    # 🔹 Non-Functional: Response time calculation
    response_time = time.time() - start_time

    return results, response_time
