# YOLOv8 Streamlit Object Detection App

This is a Streamlit app for object detection using YOLOv8, ready for deployment on Railway.

## Files
- `model.py`: Main Streamlit app
- `requirements.txt`: Python dependencies
- `Procfile`: For Railway deployment
- `train.pt`: Your YOLOv8 model weights (add this to your repo or upload via Railway dashboard)

## Deployment on Railway

1. **Push your code to GitHub** (including `model.py`, `requirements.txt`, `Procfile`, and `train.pt` if small enough).
2. **Create a new project on [Railway](https://railway.app/)** and link your GitHub repo.
3. Railway will auto-detect the `Procfile` and install dependencies from `requirements.txt`.
4. If your `train.pt` is too large for GitHub, upload it directly in the Railway dashboard after the first deploy.
5. Access your app via the public Railway URL.

## Environment Variables
- You can set `MODEL_PATH` as an environment variable on Railway if your model file is named differently or stored elsewhere.

## Example Usage
- Upload an image and the app will display detected objects with bounding boxes and class names. 