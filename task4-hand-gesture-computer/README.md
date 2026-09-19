# Task 4: AI Hand Gesture Computer Control System

## Overview
An AI-powered computer vision application built using Python, OpenCV, MediaPipe, and PyAutoGUI that allows users to control basic computer actions (such as moving the mouse cursor, clicking, and scrolling) using hand gestures captured via a webcam.

## Features
- **Real-Time Hand Tracking:** Landmark estimation using MediaPipe Hands[span_3](start_span)[span_3](end_span).
- **Touchless Cursor Navigation:** Smooth mouse movement tracked via index finger positioning[span_4](start_span)[span_4](end_span).
- **Gesture-Based Clicking:** Triggered via close proximity of thumb and index fingers[span_5](start_span)[span_5](end_span).
- **Gesture-Based Scrolling:** Dynamic page scrolling controlled via thumb and middle finger gestures[span_6](start_span)[span_6](end_span).

## Technologies Used
- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python controller.py`
