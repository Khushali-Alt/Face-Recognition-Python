







# pip install opencv-python

import cv2
import time

# ========== PART 1: Simple Video Capture ==========
print("Camera initialize ho raha hai...")

# Camera enabling with backend specification
video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Windows ke liye CAP_DSHOW use karo

# Camera ko initialize hone ka time do
time.sleep(2)

# Check if camera opened successfully
if not video_cap.isOpened():
    print("Error: Camera nahi khul raha hai")
    print("\nSolutions:")
    print("1. Check karein ki camera kisi aur app mein toh nahi chal raha")
    print("2. Windows Settings > Privacy > Camera - Python ko allow karein")
    print("3. Device Manager mein camera check karein")
    exit()

# Camera settings optimize karna
video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
video_cap.set(cv2.CAP_PROP_FPS, 30)

print("Camera successfully open ho gaya!")
print("Video chalane ke liye koi bhi key press karein. 'a' press karke band karein.")

frame_count = 0
while True:
    ret, video_data = video_cap.read()

    # Check if frame read successfully
    if not ret:
        print(f"Error: Frame {frame_count} nahi read ho raha")
        print("Camera reconnect karne ki koshish kar rahe hain...")
        video_cap.release()
        time.sleep(1)
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        time.sleep(2)
        continue

    frame_count += 1
    cv2.imshow("video_live", video_data)

    # 'a' key press karne par break
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()
cv2.destroyAllWindows()


# ========== PART 2: Face Detection ==========
print("\nFace detection start ho raha hai...")

# Haar Cascade file load karna
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Check if cascade loaded successfully
if face_cap.empty():
    print("Error: Haar Cascade file load nahi hui")
    exit()

# Camera phir se enable karna
video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(2)

# Camera settings
video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
video_cap.set(cv2.CAP_PROP_FPS, 30)

if not video_cap.isOpened():
    print("Error: Camera nahi khul raha hai")
    exit()

print("Face detection chal raha hai. 'a' press karke band karein.")

frame_count = 0
error_count = 0

while True:
    ret, video_data = video_cap.read()

    if not ret:
        error_count += 1
        print(f"Warning: Frame skip ho gaya ({error_count})")
        if error_count > 10:
            print("Bahut zyada errors aa rahe hain, band kar rahe hain...")
            break
        continue

    error_count = 0  # Reset error count on successful read
    frame_count += 1

    # Image ko grayscale mein convert karna
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    # Faces detect karna
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Detected faces par rectangle draw karna
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(video_data, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Faces count display karna
    cv2.putText(video_data, f"Faces: {len(faces)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Face Detection", video_data)

    # 'a' key press karne par break
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()
cv2.destroyAllWindows()

print("Face detection band ho gaya!")
print(f"Total frames processed: {frame_count}")
