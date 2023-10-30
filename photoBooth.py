import sys
from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
import cv2
from multiprocessing import Process
sys.path.append("/home/jhdinh/Desktop/gphoto/helpers")
from liveView import *
from countDown import *
from displayPushToStart import *
from collage import *

shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "PiPhotos"
folderName = shot_date + picID
saveLocation = "/home/jhdinh/Desktop/gphoto/images/" + folderName
captureAndDownload = ["--filename", saveLocation + '/' + shot_time, "--capture-image-and-download"]

# kill gphoto2 process
# reconnects camera to be run from script
def killgphoto2Process():
	p = subprocess.Popen(['ps', '-A'],stdout=subprocess.PIPE)
	out, err = p.communicate()
	
	# search for process ID and kill it
	for line in out.splitlines():
		if b'gvfsd-gphoto2' in line:
			pid = int(line.split(None, 1)[0])
			os.kill(pid, signal.SIGKILL)

def createSaveFolder():
	try:
		os.mkdir(saveLocation)
	except:
		print("Failed to create new directory")

killgphoto2Process()
createSaveFolder()
while True:
	# TODO: Still need to put int push to start window
	# Then need to have window disappear and start photobooth
	# Also need to display screen in between photos
	input("Press anything to start photobooth")
	for i in range(3):
		p = Process(target=liveView)
		shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		captureAndDownload = ["--filename", saveLocation + '/' + shot_time, "--capture-image-and-download"]
		p.start()
		time.sleep(2)
		for j in range(3,0,-1):
			countDown(j)
		p.terminate()
		gp(captureAndDownload)
	collage(saveLocation)
	
