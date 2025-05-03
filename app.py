from flask import Flask, request, jsonify, send_file
from ultralytics import YOLO
from PIL import Image
import io
import os

app = Flask(__name__)

# Load model once
model = YOLO("train.pt")  # Make sure this file is in the project root

@app.route('/')
def index():
    return jsonify({"message": "YOLO Flask API is live!"})

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image_path = "input.jpg"
    file.save(image_path)

    results = model(image_path)
    result = results[0]

    # Get labels
    labels = [model.names[int(cls)] for cls in result.boxes.cls]

    # Plot image with bounding boxes
    plotted_image = result.plot()
    image_pil = Image.fromarray(plotted_image)
    image_io = io.BytesIO()
    image_pil.save(image_io, format='JPEG')
    image_io.seek(0)

    # Send both image and label response
    response = {
        "labels": labels
    }

    # Use multipart response to send JSON and image (or simplify)
    # For simplicity, just return labels + send image separately
    return send_file(image_io, mimetype='image/jpeg')

@app.route('/labels', methods=['POST'])
def get_labels():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image_path = "input.jpg"
    file.save(image_path)

    results = model(image_path)
    result = results[0]
    labels = [model.names[int(cls)] for cls in result.boxes.cls]

    return jsonify({"labels": labels})
