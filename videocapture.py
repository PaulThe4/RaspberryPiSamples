import cv2
import os
from datetime import datetime

from picamera2 import Picamera2
piCam = Picamera2()
piCam.preview_configuration.main.size=(1280,720)
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.controls.FrameRate=30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()


dest = '/home/gsurats1/Desktop'
os.chdir(dest)
interval = 20
start_time = datetime.now()
X = cv2.VideoWriter_fourcc(*'XVID')
#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#fps = cap.get(cv2.CAP_PROP_FPS)
i = 1
#output = cv2.VideoWriter('Video.avi',X,30.0,(1280,720))
while True:
	frame = piCam.capture_array()
	
	cv2.imshow('Live',frame)
	current_time = datetime.now()
	time_passed = (current_time - start_time).total_seconds()
	if time_passed >= interval:
		timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
		file_name = 'video_{}.avi'.format(timestamp)
		output = cv2.VideoWriter(file_name,X,30.0,(1280,720))
		#output = cv2.VideoWriter(file_name,X)
		for j in range(500):
			output.write(frame)
		output.release()
		start_time = current_time
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
#cap.release()
output.release()
cv2.destroyAllWindows()
