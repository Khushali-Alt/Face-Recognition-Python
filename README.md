# Real-Time Face Detection System

A Python-based real-time face detection application using OpenCV and Haar Cascade classifiers. This project captures video from your webcam and detects faces in real-time, drawing green rectangles around detected faces.


## Features

- Real-time face detection using webcam
- Haar Cascade classifier for accurate detection
- Live video feed with face bounding boxes
- Cross-platform support (Windows, macOS, Linux)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- A working webcam

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/face-recognition.git
cd face-recognition
```

### Step 2: Create a Virtual Environment

Creating a virtual environment is recommended to keep dependencies isolated.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command prompt, indicating the virtual environment is active.

### Step 3: Install Dependencies

```bash
pip install opencv-python
```

Or install from requirements file:
```bash
pip install -r requirements.txt
```

## Project Structure

```
face-recognition/
│
├── face_detection.py       # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
└── venv/                  # Virtual environment (not tracked)
```

## Usage

### Running the Application

1. **Activate your virtual environment** (if not already active):
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Run the script**:
   ```bash
   python face_detection.py
   ```

3. **Using the application**:
   - A window will open showing your webcam feed
   - Detected faces will have green rectangles around them
   - Press **'a'** key to exit the application

### Troubleshooting

**Camera not opening?**
- Close other applications using the webcam (Zoom, Teams, Skype)
- Try running with administrator privileges
- Check if your camera is enabled in Windows Settings → Privacy → Camera

**No window appearing?**
- Press `Alt + Tab` to check if the window is behind other windows
- Try different camera indices in the code (change `0` to `1` or `2`)

**"Camera opened: False" error?**
- Ensure your webcam is properly connected
- Grant camera permissions to Python
- Restart your computer

**Program hangs or freezes?**
- Press `Ctrl + C` in the terminal to stop
- Make sure you're using `cv2.CAP_DSHOW` on Windows

## Configuration

You can adjust detection parameters in the code:

```python
faces = face_cap.detectMultiScale(
    col,
    scaleFactor=1.1,      # Adjust between 1.05-1.3 (lower = more sensitive)
    minNeighbors=5,       # Adjust between 3-10 (higher = stricter)
    minSize=(30, 30)      # Minimum face size in pixels
)
```

## How It Works

1. **Camera Initialization**: Opens the default webcam using OpenCV
2. **Frame Capture**: Continuously captures frames from the video feed
3. **Grayscale Conversion**: Converts each frame to grayscale for faster processing
4. **Face Detection**: Uses Haar Cascade classifier to detect faces
5. **Drawing Rectangles**: Draws green bounding boxes around detected faces
6. **Display**: Shows the processed frame in a window

## Code Example

```python
import cv2

# Load face cascade classifier
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open webcam
video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, video_data = video_cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cap.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("Face Detection", video_data)
    
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()
cv2.destroyAllWindows()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Author

**Khushali Tiwari**

## Acknowledgments

- OpenCV library for computer vision capabilities
- Haar Cascade classifiers for face detection

---

If you found this project helpful, please give it a star!
