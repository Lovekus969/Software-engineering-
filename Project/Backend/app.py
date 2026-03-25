from flask import Flask, Response
import cv2
from detector import detect_objects
import json

app = Flask(__name__)

camera = cv2.VideoCapture(0)

@app.route('/video')
def video_feed():
    def generate():
        while True:
            success, frame = camera.read()
            if not success:
                break

            detections, response_time = detect_objects(frame)

            # Draw boxes
            for obj in detections:
                (x1, y1, x2, y2) = obj["box"]
                label = obj["label"]

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Show response time
            cv2.putText(frame, f"Time: {response_time:.2f}s",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data')
def data():
    success, frame = camera.read()
    if not success:
        return {"error": "camera failed"}

    detections, response_time = detect_objects(frame)

    return {
        "detections": detections,
        "response_time": response_time
    }

if __name__ == "__main__":
    app.run(debug=True)
