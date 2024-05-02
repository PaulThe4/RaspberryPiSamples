import cv2
import os
import datetime

# Function to save video with timestamped filename
def save_video_with_timestamp(video_capture1, video_capture2, camera_number1, camera_number2):
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Define filename with camera number and timestamp
    filename1 = f"video{camera_number1}_{timestamp}.avi"
    filename2 = f"video{camera_number2}_{timestamp}.avi"
    # Define video writer object
    result1 = cv2.VideoWriter(filename1, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
    result2 = cv2.VideoWriter(filename2, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
    
    # Record video for 10 seconds
    start_time = datetime.datetime.now()
    while (datetime.datetime.now() - start_time).total_seconds() < 30:
        ret1, frame1 = video_capture1.read()
        ret2, frame2 = video_capture2.read()
        if ret1 and ret2:
			# Resize frame for display
            resized_frame1 = cv2.resize(frame1, (640, 480))
            resized_frame2 = cv2.resize(frame2, (640, 480))
            result1.write(frame1)
            result2.write(frame2)
            cv2.imshow(f"Camera {camera_number1}", resized_frame1)
            cv2.imshow(f"Camera {camera_number2}", resized_frame2)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else:
            break
    
    # Release resources
    result1.release()
    result2.release()
    cv2.destroyAllWindows()
    print(f"Camera {camera_number1}: Video saved as {filename1}")
    print(f"Camera {camera_number2}: Video saved as {filename2}")


# Create video capture objects for each camera
video1 = cv2.VideoCapture(0)
video2 = cv2.VideoCapture(2)

# Check if cameras are opened successfully
if not video1.isOpened() or not video2.isOpened():
    print("Error: One or both cameras couldn't be opened.")
    exit()

# Set resolutions for video capture objects
frame_width1 = int(video1.get(3))
frame_height1 = int(video1.get(4))
frame_width2 = int(video2.get(3))
frame_height2 = int(video2.get(4))

size = (frame_width1, frame_height1)  # Assuming both cameras have the same resolution

# Save videos from both cameras
save_video_with_timestamp(video1, video2, 1, 2)
#save_video_with_timestamp(video2, 2)

# Release video capture objects
video1.release()
video2.release()
