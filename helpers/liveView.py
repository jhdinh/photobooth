import cv2
import sys

# live view runs for ~ 7 seconds right now
# higher Timer = longer
# subtracting less from timer = longer
# not sure exactly what the ratio is, but cv2.waitKey holds execution for x milliseconds
def live_view():
	
	cv2.namedWindow('LiveView', cv2.WINDOW_NORMAL)
	cv2.setWindowProperty('LiveView', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	

	cap = cv2.VideoCapture(0, cv2.CAP_V4L)

	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
	
	timer = 3000

	#while timer > 0:
	while True:
		ret, frame = cap.read()
		#timer -= 35
		frame = cv2.resize(frame, (1920, 1080))
		cv2.imshow('LiveView', frame)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
