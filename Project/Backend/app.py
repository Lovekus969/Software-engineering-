from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load pre-trained COCO-SSD model (TensorFlow Hub)
model = tf.saved_model.load("ssd_mobilenet_v2_fpnlite_320x320/saved_model")

# COCO class labels
COCO_CLASSES = {
    1: "person", 2: "bicycle", 3: "car", 4: "motorcycle",
    5: "airplane", 6: "bus", 7: "train", 8: "truck",
    9: "boat", 10: "traffic light", 11: "fire hydrant",
    # ... you can extend this if needed
}

def detect_object(image_array):
    """
    Detect object from image using TensorFlow COCO-SSD.
    Returns object name, distance, direction.
    """
    # Convert to tensor
    input_tensor = tf.convert_to_tensor(image_array)
    input_tensor = input_tensor[tf.newaxis, ...]  # add batch dim
    detections = model(input_tensor)

    # Extract first detection with confidence > 0.5
    scores = detections['detection_scores'][0].numpy()
    classes = detections['detection_classes'][0].numpy().astype(int)
    boxes = detections['detection_boxes'][0].numpy()  # y_min, x_min, y_max, x_max

    for i in range(len(scores)):
        if scores[i] > 0.5:
            obj_class = COCO_CLASSES.get(classes[i], "Unknown")
            box = boxes[i]
            # Calculate direction: left, center, right
            x_center = (box[1] + box[3]) / 2
            if x_center < 0.33:
                direction = "Left"
            elif x_center < 0.66:
                direction = "Center"
            else:
                direction = "Right"
            # Dummy distance (later replace with real depth calculation)
            distance = f"{round((1 - scores[i]) * 5 + 1, 2)} meters"
            return {"object": obj_class, "distance": distance, "direction": direction}

    return {"object": "None", "distance": "-", "direction": "-"}


@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    img_data = data['image'].split(",")[1]  # remove 'data:image/png;base64,'
    img_bytes = base64.b64decode(img_data)
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    img_array = np.array(img)

    result = detect_object(img_array)
    return jsonify(result)


if __name__ == '__main__':
    print("Starting backend at http://127.0.0.1:5000")
    app.run(debug=True)
