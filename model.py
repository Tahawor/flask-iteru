import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

# Set page config
st.set_page_config(page_title="Object Detection App", page_icon="📸")

# Get model path from environment variable or default to local file
MODEL_PATH = os.getenv("MODEL_PATH", "train.pt")

# Initialize session state for model
if 'model' not in st.session_state:
    try:
        st.session_state.model = YOLO(MODEL_PATH)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.stop()

st.title("📸 YOLOv8 Object Detection")
st.write("Upload an image to detect objects")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        # Load and display the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert to numpy array
        image_np = np.array(image)

        # Run inference
        with st.spinner("Detecting objects..."):
            results = st.session_state.model(image_np)
            
        # Display results
        annotated = results[0].plot()
        st.image(annotated, caption="Detected Objects", use_column_width=True)
        
        # Display detection information
        st.write("### Detection Results")
        for r in results:
            for box in r.boxes:
                conf = box.conf[0].item()
                cls = box.cls[0].item()
                class_name = results[0].names[int(cls)]
                st.write(f"- {class_name}: {conf:.2%} confidence")
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
