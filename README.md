# Emotion Detection in Admissions Interviews

A real-time **facial emotion recognition system** developed as an academic project at **ESPRIT**.

The project uses **Computer Vision and Deep Learning** to detect and classify facial expressions during admission interviews. The objective is to provide an additional AI-based indicator that can support the analysis of candidate interactions during the admission process.

> **Academic Project — ESPRIT**

## About the Project

The system analyzes facial expressions captured through a webcam and identifies the detected emotional state in real time.

The solution is based on the **FER2013 dataset** and uses **TensorFlow/Keras** for deep learning and **OpenCV** for real-time image and facial processing.

The recognized emotions include:

- Angry
- Happy
- Sad
- Surprise
- Neutral
- Fear
- Disgust

## Main Features

- Real-time facial expression detection
- Webcam-based emotion recognition
- Face detection using Computer Vision
- Deep Learning-based emotion classification
- Recognition of multiple emotional states
- Real-time prediction and visualization
- FER2013 dataset integration
- Interactive visual feedback

## Technology Stack

### Computer Vision

- OpenCV
- Real-time webcam processing
- Face detection

### Deep Learning

- TensorFlow
- Keras
- Convolutional Neural Network (CNN)

### Dataset

- FER2013

### Programming Language

- Python

## System Workflow

```text
              ┌─────────────────────┐
              │       Webcam        │
              │    Video Stream     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    Face Detection   │
              │      OpenCV         │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Image Preprocessing │
              │   Resize / Normalize│
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   CNN Model         │
              │ TensorFlow / Keras  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Emotion Prediction  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Real-Time Display   │
              │ Emotion + Confidence│
              └─────────────────────┘

```

---

## Demo




https://github.com/user-attachments/assets/2f0dc30f-6c04-4bfb-b87e-a782617c427d




```
