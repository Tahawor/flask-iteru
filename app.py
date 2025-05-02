from flask import Flask, request, jsonify, send_file
from ultralytics import YOLO
import os
from PIL import Image
import io

app = Flask(__name__)

# Load the model (update the path if needed)
model = YOLO("train.pt")

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save uploaded image temporarily
    image_path = "uploaded_image.jpg"
    file.save(image_path)

    # Run YOLO prediction
    results = model(image_path)

    # Plot detections on the image
    result_image = results[0].plot()

    # Convert to a bytes stream for sending via HTTP
    image_pil = Image.fromarray(result_image)
    image_io = io.BytesIO()
    image_pil.save(image_io, 'JPEG')
    image_io.seek(0)

    # Send the image back to the client
    return send_file(image_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
