# Face Detection using OpenCV on Raspberry Pi

## Description
This project performs real-time face detection using OpenCV's Haar Cascade classifier on a Raspberry Pi.

## Objective
To detect and count human faces in a live video stream.

## Hardware Required
* Raspberry Pi 4
* USB Camera / Pi Camera

## Software Used
* Python 3
* OpenCV

## Installation
```bash
sudo apt update
sudo apt install python3-pip
pip3 install opencv-python
```

## Run the Project
```bash
python3 src/face_detection.py
```

## Required File
Make sure the following file is present in the root directory:
* haarcascade_frontalface_default.xml

## Working
* Captures video from camera
* Converts frame to grayscale
* Uses Haar Cascade classifier to detect faces
* Draws bounding boxes around faces
* Displays number of faces in real-time

## 🚀 Future Improvements

* Face recognition (identify person)
* Mask detection
* Attendance system
* Optimize using Edge AI



