# 🛑 Drowsiness Detection System

A simple real-time drowsiness detection system using **OpenCV** and **Haar Cascades** to monitor eye closure and detect sleepiness or fatigue based on Eye Aspect Ratio (EAR).

## 📌 Features

- Real-time face and eye detection using webcam
- EAR (Eye Aspect Ratio) based drowsiness detection
- Displays status: **AWAKE**, **SLEEPY**, or **DROWSY**
- Simple and lightweight, no deep learning required
- Works even when wearing glasses (uses `eye_tree_eyeglasses` cascade)

## 🧠 How It Works

The system calculates the Eye Aspect Ratio (EAR) using the height and width of detected eyes. If eyes are not detected for a continuous number of frames, it classifies the state as:
- **SLEEPY** (brief eye closure)
- **DROWSY** (sustained eye closure)

If no face is detected, it shows **NO FACE**.

## 🔧 Tech Stack

- Python
- OpenCV
- Haar Cascade Classifiers

## 📁 Files

- `main.py`: Main script for drowsiness detection
- `README.md`: Project description
- `haarcascade_frontalface_default.xml`: Face detection model (OpenCV built-in)
- `haarcascade_eye_tree_eyeglasses.xml`: Eye detection model (for glasses support)

## ▶️ How to Run

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/Drowsiness-Detection-System.git
    cd Drowsiness-Detection-System
    ```

2. Install the required packages:

    ```bash
    pip install opencv-python
    ```

3. Run the code:

    ```bash
    python main.py
    ```

4. Press `q` to exit the webcam window.

## ⚠️ Dependencies

- Python 3.x
- OpenCV (`cv2`)
- Webcam

> Make sure your webcam is working before running the project.
