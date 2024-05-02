import cv2

# Path to the saved video file
video_path = '/home/gsurats1/video1.avi'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get the frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Create a window to display the video
cv2.namedWindow('Slow Motion Video', cv2.WINDOW_NORMAL)

# Read and display each frame
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Display the frame
    cv2.imshow('Slow Motion Video', frame)

    # Adjust the delay to slow down the video (increase the value for slower playback)
    delay = int(1000 / fps * 4)  # milliseconds
    cv2.waitKey(delay)

    # Check for 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
