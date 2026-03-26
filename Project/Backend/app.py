from flask import Flask, Response, jsonify
import cv2
from detector import detect_objects

app = Flask(__name__)

# 🔹 Non-Functional: Compatibility (camera access across devices)
camera = cv2.VideoCapture(0)

@app.route('/video')
def video_feed():
    # 🔹 Functional: Real-time video streaming
    def generate():
        while True:
            success, frame = camera.read()

            # 🔹 Non-Functional: Reliability (error handling)
            if not success:
                break

            # 🔹 Functional: Object Detection
            detections, response_time = detect_objects(frame)

            # 🔹 Functional: AR Visualization (drawing boxes)
            for obj in detections:
                (x1, y1, x2, y2) = obj["box"]
                label = obj["label"]

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # 🔹 Non-Functional: Performance Monitoring (response time)
            cv2.putText(frame, f"Time: {response_time:.2f}s",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # 🔹 Non-Functional: Performance (efficient encoding)
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # 🔹 Functional: Streaming frames to frontend
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/data')
def data():
    # 🔹 Functional: API endpoint for object data
    success, frame = camera.read()

    # 🔹 Non-Functional: Reliability (error handling)
    if not success:
        return jsonify({"error": "camera failed"})

    # 🔹 Functional: Object Detection API
    detections, response_time = detect_objects(frame)

    # 🔹 Functional: Return structured JSON data
    return jsonify({
        "detections": detections,
        "response_time": response_time
    })


if __name__ == "__main__":
    # 🔹 Non-Functional: Debug mode for development (maintainability)
    app.run(debug=True)
