import cv2
import os
from datetime import datetime, timedelta

dest = '/home/gsurats1/Desktop'
os.chdir(dest)
video_duration = 60  # Duration of the video in seconds
cap2 = cv2.VideoCapture(2)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap2.set(3, 640)
cap2.set(4, 480)
X = cv2.VideoWriter_fourcc(*'MJPG')
fps = 30

# Create directories to store frames
frames_dir1 = 'frames1'
frames_dir2 = 'frames2'
os.makedirs(frames_dir1, exist_ok=True)
os.makedirs(frames_dir2, exist_ok=True)

# Capture frames for the specified duration
start_time = datetime.now()
frame_count = 0

while True:
    ret1, frame1 = cap.read()
    ret2, frame2 = cap2.read()

    cv2.imshow('Live1', frame1)
    cv2.imshow('Live2', frame2)

    current_time = datetime.now()
    time_passed = (current_time - start_time).total_seconds()

    # Save frames only if still within the video duration
    if time_passed <= video_duration:
        timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        file_name1 = os.path.join(frames_dir1, 'frame1_{}.jpg'.format(timestamp))
        file_name2 = os.path.join(frames_dir2, 'frame2_{}.jpg'.format(timestamp))
        cv2.imwrite(file_name1, frame1)
        cv2.imwrite(file_name2, frame2)
        frame_count += 1
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap2.release()
cv2.destroyAllWindows()

# Combine saved images to form the video
image_files1 = sorted(os.listdir(frames_dir1))
image_files2 = sorted(os.listdir(frames_dir2))

output_video1 = cv2.VideoWriter('video1.avi', X, fps, (640, 480))
output_video2 = cv2.VideoWriter('video2.avi', X, fps, (640, 480))

# Write frames to video
for image_file1, image_file2 in zip(image_files1, image_files2):
    frame1 = cv2.imread(os.path.join(frames_dir1, image_file1))
    frame2 = cv2.imread(os.path.join(frames_dir2, image_file2))
    output_video1.write(frame1)
    output_video2.write(frame2)

output_video1.release()
output_video2.release()

# Cleanup: Delete temporary frame files
for file in os.listdir(frames_dir1):
    os.remove(os.path.join(frames_dir1, file))
for file in os.listdir(frames_dir2):
    os.remove(os.path.join(frames_dir2, file))
os.rmdir(frames_dir1)
os.rmdir(frames_dir2)

print("Total frames captured:", frame_count)
