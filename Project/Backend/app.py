from flask import Flask, Response, jsonify
import cv2
from detector import detect_objects
import pyttsx3

app = Flask(__name__)

# 🔹 Non-Functional: Compatibility (camera access)
camera = cv2.VideoCapture(0)

# 🔹 Functional: Initialize Text-to-Speech engine (Accessibility)
engine = pyttsx3.init()

def speak(text):
    # 🔹 Functional: Audio Feedback
    engine.say(text)
    engine.runAndWait()

def detect_obstacle(detections):
    # 🔹 Functional: Obstacle detection logic
    danger_objects = ["car", "person", "bicycle", "motorbike"]

    for obj in detections:
        if obj["label"] in danger_objects:
            return True
    return False


@app.route('/video')
def video_feed():
    def generate():
        while True:
            success, frame = camera.read()

            # 🔹 Non-Functional: Reliability
            if not success:
                break

            # 🔹 Functional: Object Detection
            detections, response_time = detect_objects(frame)

            labels = []

            # 🔹 Functional: AR Visualization
            for obj in detections:
                (x1, y1, x2, y2) = obj["box"]
                label = obj["label"]
                labels.append(label)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # 🔹 Functional: Audio Feedback (speak detected objects)
            if labels:
                speak(", ".join(labels))

            # 🔹 Functional: Obstacle Alert
            if detect_obstacle(detections):
                speak("Warning, obstacle ahead")

            # 🔹 Non-Functional: Performance Monitoring
            cv2.putText(frame, f"Time: {response_time:.2f}s",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # 🔹 Functional: Streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/data')
def data():
    success, frame = camera.read()

    # 🔹 Non-Functional: Reliability
    if not success:
        return jsonify({"error": "camera failed"})

    detections, response_time = detect_objects(frame)

    return jsonify({
        "detections": detections,
        "response_time": response_time
    })


if __name__ == "__main__":
    # 🔹 Non-Functional: Maintainability (debug mode)
    app.run(debug=True)
