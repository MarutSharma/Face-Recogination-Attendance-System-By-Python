# Face Recognition Attendance System

A Python-based attendance system that uses real-time face recognition to automate and record attendance. This project leverages OpenCV, face recognition libraries, and Tkinter for GUI interaction.

## 📌 Features

- Real-time face detection and recognition using webcam
- Mark attendance and record it with timestamp in a CSV file
- GUI interface built using Tkinter
- Admin options to:
  - Register new faces
  - View attendance logs
  - Train dataset for recognition

## 🧰 Tech Stack

- **Language**: Python  
- **Libraries**:
  - OpenCV
  - face_recognition
  - NumPy
  - Pandas
  - Tkinter
  - PIL

## 📷 How It Works

1. **Face Registration**: Capture images of new faces and store them in a dataset folder.
2. **Model Training**: Encode and save face data for recognition.
3. **Recognition & Attendance**: Run live camera stream to detect and match faces; mark attendance in `Attendance.csv`.

## 🚀 Getting Started

### Prerequisites

Install the required libraries using pip:

```bash
pip install opencv-python
pip install face_recognition
pip install numpy
pip install pandas
pip install pillow

1. Clone the repository:

git clone https://github.com/MarutSharma/Face-Recogination-Attendance-System-By-Python
cd Face-Recogination-Attendance-System-By-Python

📁 # Folder Structure :

Face-Recogination-Attendance-System-By-Python/
├── dataset/               # Stored face images
├── attendance/            # Attendance CSV files
├── training_data/         # Encoded face data
├── main.py                # Main GUI application
├── face_recognition.py    # Face encoding and matching logic
└── README.md              # Project documentation

🎯 # Future Enhancements 

Email alerts for unknown faces

Attendance dashboard

Face detection accuracy improvements

👨‍💻 Author
Marut Sharma
GitHub: MarutSharma
