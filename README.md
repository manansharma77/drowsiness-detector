# drowsiness-detector
Drowsiness Detection System is a computer vision project that monitors a user’s eyes in real time using a webcam. The system detects signs of drowsiness and triggers a voice and sound alert when the eyes remain closed for a specified duration, helping improve safety and prevent accidents.

😴 Drowsiness Detection System

📌 Overview

The Drowsiness Detection System is a real-time computer vision application developed using Python and OpenCV. It monitors a user’s eyes through a webcam to detect signs of drowsiness. If the user’s eyes remain closed for a specified number of consecutive frames, the system displays a warning message and triggers both a voice notification and an alarm sound.

The project also collects the user’s Name and Registration Number through a simple graphical interface and displays this information on the live camera feed.

⸻

✨ Features

* 🎥 Real-time webcam monitoring
* 👤 Face detection using Haar Cascade Classifier
* 👀 Eye detection using Haar Cascade Classifier
* ⚠️ Drowsiness detection based on continuous eye closure
* 🔊 Voice alert (“Wake up”)
* 🔔 Alarm sound notification
* 📝 Displays user name and registration number on the video feed
* ⌨️ Press ESC to exit the application

⸻

🛠️ Technologies Used

* Python 3
* OpenCV
* Turtle
* OS Module

⸻

📂 Project Structure

Drowsiness-Detection-System/
│── finalproject.py
│── README.md

⸻

⚙️ How It Works

1. The program asks the user to enter their Name and Registration Number.
2. The webcam starts capturing live video.
3. Each frame is converted to grayscale.
4. Haar Cascade classifiers detect the user’s face and eyes.
5. If the eyes are detected, the system displays Awake.
6. If the eyes remain undetected for more than 20 consecutive frames, the system:
    * Displays SLEEPING ALERT!
    * Plays an alarm sound.
    * Announces “Wake up” using the system voice.
7. The application continues monitoring until the ESC key is pressed.

⸻

🚀 Installation

1. Clone the repository

git clone https://github.com/your-username/Drowsiness-Detection-System.git

2. Navigate to the project folder

cd Drowsiness-Detection-System

3. Install the required packages

pip install opencv-python

(The os and turtle modules are included with Python.)

4. Run the project

python finalproject.py

⸻

📸 Output

The application displays:

* Live webcam feed
* Face detection rectangle
* Eye detection rectangles
* Awake/Sleeping status
* User Name
* Registration Number

⸻

🔮 Future Improvements

* Replace Haar Cascade with CNN-based eye detection
* Integrate MediaPipe Face Mesh for improved accuracy
* Add blink detection using Eye Aspect Ratio (EAR)
* Improve performance under low-light conditions
* Support multiple users and attendance logging
* Save drowsiness events with timestamps

⸻

📚 Learning Outcomes

Through this project, I learned:

* Computer Vision fundamentals
* Real-time webcam processing
* Face and eye detection using OpenCV
* Working with Haar Cascade classifiers
* Image preprocessing using grayscale conversion
* Real-time decision making using frame counters
* Displaying text and graphics on video frames
* Building an end-to-end Python application

⸻

👨‍💻 Author

Manan Sharma

B.Tech Computer Science Engineering

Python | OpenCV | Machine Learning Enthusiast

⸻

📄 License

This project is intended for educational and learning purposes.
