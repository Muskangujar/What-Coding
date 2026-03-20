# Index Finger Tracking using OpenCV and MediaPipe

## Overview
This project demonstrates how to track the tip of the index finger using a webcam. 
It uses OpenCV for capturing video frames and MediaPipe for detecting hand landmarks.

The program detects a hand in real time and draws a circle on the tip of the index finger.

## Requirements

Python 3.8 or later

Libraries:
- opencv-python
- mediapipe

Install dependencies with:

pip install opencv-python mediapipe

## Project Files

hand_landmarker.task  
The trained MediaPipe model used to detect hand landmarks.

main.py  
Python script that runs the hand tracking program.

README.md  
Documentation explaining the project.

## How the Program Works

1. The webcam captures video frames.
2. Each frame is converted from BGR to RGB format.
3. The frame is passed to the MediaPipe hand landmark detector.
4. MediaPipe returns 21 landmark points for the detected hand.
5. Landmark number 8 corresponds to the tip of the index finger.
6. The coordinates are converted to pixel values.
7. A circle is drawn on the detected fingertip.
8. The processed frame is displayed in a window.

## Running the Program

Place the model file in the same directory as the Python script.

Run the program with:

python main.py

Press the 'q' key to exit the application.

## Hand Landmark Reference

MediaPipe detects 21 landmarks for each hand.

Important fingertip landmarks:

4  - Thumb tip  
8  - Index finger tip  
12 - Middle finger tip  
16 - Ring finger tip  
20 - Pinky finger tip  

## Possible Improvements

- Control the mouse cursor using finger movement
- Create a virtual drawing application
- Detect gestures such as pinch or swipe
- Track multiple hands

# Updated Version: Gesture Controlled Air OS

This project has been upgraded from basic index finger tracking to a full gesture-based control system.

New features include:
- Mouse control using index finger
- Click using pinch gesture
- Smooth cursor movement
- Real-time gesture recognition

---

## Previous Version
The original implementation tracked only the index finger and displayed its position.

This version builds on top of that foundation

## Author

This project was created as a learninggit status exercise for understanding computer vision and hand tracking using MediaPipe and OpenCV.
