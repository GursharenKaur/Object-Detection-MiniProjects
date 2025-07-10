# Moving Object Detection

A simple Python script that detects motion using a webcam feed by comparing video frames in real-time. Useful for basic surveillance, monitoring, or learning computer vision concepts.

## 📌 Features
- Real-time video feed using OpenCV.
- Detects and highlights moving objects with bounding boxes.
- Displays detection status (`"Normal"` or `"Moving Object Detected"`) on screen.

## Install dependencies:
```bash
pip install opencv-python
pip install opencv-contrib-python
pip install imutils
```

## 📷 How It Works
- Captures video from webcam.

- Converts frames to grayscale and applies Gaussian blur.

- Compares the current frame to the first frame to detect changes.

- Draws bounding boxes around detected motion.
