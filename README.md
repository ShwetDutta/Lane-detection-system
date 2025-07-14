# 🛣️ Lane Detection Using OpenCV

This project is a beginner-friendly implementation of a real-time lane detection system using OpenCV and Python. It leverages fundamental image processing techniques to detect lane lines on roads from video input.

## 🚀 Project Goals

- Process video frames in real-time
- Apply grayscale conversion, Gaussian blur, and Canny edge detection
- Define a region of interest (ROI) for focusing on lane areas
- Use Hough Transform to detect straight lane lines
- Overlay the detected lane lines on the original video

---

## 📁 Folder Structure

Lane-Detection/
│
├── lane_video.mp4 # Sample input video
├── final project.py # Main Python script
├── README.md # Project documentation



---

## 🧠 Key Concepts Used

- **Grayscale Conversion** – reduces computation by removing color
- **Gaussian Blur** – smoothens the image to reduce noise
- **Canny Edge Detection** – detects sharp edges which may correspond to lane lines
- **Region of Interest Masking** – filters out irrelevant parts of the frame
- **Hough Line Transform** – identifies lines in the edge-detected image

---

## 🖥️ How to Run

1. **Install Requirements:**

   ```bash
   pip install opencv-python numpy

2. **Run the Script:**

   ```bash
   python lane_detection.py

Press q to quit the video window.

