import cv2

# Set desired frame rate and total number of frames
frame_rate = 30  # 30 frames per second
total_frames = 900

# Set video dimensions (width, height)
frame_width = 640
frame_height = 480

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('captured_video.avi', fourcc, frame_rate, (frame_width, frame_height))

# Initialize video capture
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # Change 0 to the video file path if you want to capture from a file

# Check if the camera/video file is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera or video file.")
    exit()

# Variables to keep track of frames captured
frame_count = 0

# Loop to capture frames
while frame_count < total_frames:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Error: Could not read frame.")
        break

    # Write the frame to the video file
    out.write(frame)

    # Display the frame (optional)
    cv2.imshow('Frame', frame)

    # Increment frame count
    frame_count += 1

    # Wait for a short duration to achieve the desired frame rate
    cv2.waitKey(int(1000 / frame_rate))

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object, VideoWriter object, and close any open windows
cap.release()
out.release()
cv2.destroyAllWindows()