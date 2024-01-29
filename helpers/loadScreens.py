import cv2

def load_screens():
	print("loading the screens")
	path1 = r'/home/jhdinh/Desktop/gphoto/assets/OneMorePic.JPG'
	path2 = r'/home/jhdinh/Desktop/gphoto/assets/TwoMorePics.JPG'
	path3 = r'/home/jhdinh/Desktop/gphoto/assets/PushToStart.JPG'
	path4 = r'/home/jhdinh/Desktop/gphoto/assets/SmileScreen.JPG'
	path5 = r'/home/jhdinh/Desktop/gphoto/assets/PrintingScreen.JPG'

	image1 = cv2.imread(path1)
	image2 = cv2.imread(path2)
	pushToStart = cv2.imread(path3)
	smile = cv2.imread(path4)
	printing = cv2.imread(path5)

	cv2.namedWindow('oneMorePic', cv2.WINDOW_NORMAL)
	cv2.setWindowProperty('oneMorePic', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

	cv2.namedWindow('twoMorePics', cv2.WINDOW_NORMAL)
	cv2.setWindowProperty('twoMorePics', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	
	cv2.namedWindow('smileWindow', cv2.WINDOW_NORMAL)
	cv2.setWindowProperty('smileWindow', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	
	cv2.namedWindow('pushToStartWindow', cv2.WINDOW_NORMAL)
	cv2.setWindowProperty('pushToStartWindow', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	
	cv2.namedWindow('printingScreen', cv2.WINDOW_NORMAL)
	cv2.setWindowProperty('printingScreen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

	image1 = cv2.resize(image1, (1920, 1080))
	image2 = cv2.resize(image2, (1920, 1080))
	pushToStartImage = cv2.resize(pushToStart, (1920, 1080))
	smileImage = cv2.resize(smile, (1920, 1080))
	printScreen = cv2.resize(printing, (1920, 1080))


	cv2.imshow("oneMorePic", image1)
	cv2.imshow("twoMorePics", image2)
	cv2.imshow("pushToStartWindow", pushToStartImage)
	cv2.imshow("smileWindow", smileImage)
	cv2.imshow("printingScreen", printScreen)
	


	while(1):
		k = cv2.waitKey(33)
		if k==27:    # Esc key to stop
			break
		elif k ==97:
			print("pressed a")
			print(k)


if __name__ == "__main__":
	load_screens()
