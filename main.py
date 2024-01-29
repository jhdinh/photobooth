from time import sleep
from datetime import datetime
from multiprocessing import Process
from sh import gphoto2 as gp
import pygame, sys
sys.path.append("/home/jhdinh/Desktop/gphoto/helpers")
from collage import collage, collageDouble
from loadScreens import load_screens
from countDown import count_down
from displayPushToStart import display_push_to_start
from liveView import live_view
from sendToPrinter import send_to_printer
import pywinctl as gw
import cv2
import signal, os, subprocess
import time

shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "PiPhotos"
folderName = shot_date + picID
saveLocation = "/home/jhdinh/Desktop/gphoto/images/" + folderName
captureAndDownload = ["--filename", saveLocation + '/' + shot_time, "--capture-image-and-download"]
#BG = pygame.image.load("assets/PushToStart.png")
#SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def reInit():
    pygame.init()
    SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Menu")
    return SCREEN

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def startPhotobooth():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((0,0,0))

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, (255,255,255))
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color=(255,255,255), hovering_color=(19,148,79))

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

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
    
#12/26/23
# screen transitions work so far, need to get countdown to display during live view
# also need transition screens to display 2 more pictures, 1 more picture, etc
if __name__ == "__main__":
    init_flag = 0
    killgphoto2Process()
    createSaveFolder()
    load_screens()
    time.sleep(3)
    win2 = gw.getWindowsWithTitle('oneMorePic')[0]
    win1 = gw.getWindowsWithTitle('twoMorePics')[0]
    win3 = gw.getWindowsWithTitle('pushToStartWindow')[0]
    win4 = gw.getWindowsWithTitle('smileWindow')[0]
    win5 = gw.getWindowsWithTitle('printingScreen')[0]
    while(True):
        k = cv2.waitKey(33)
        if init_flag == 0:
            win3.raiseWindow()
            init_flag = 1
        if k==27:    # Esc key to stop
            break
        elif k==-1:
            continue
        else:
            for i in range(3):
                shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                captureAndDownload = ["--filename", saveLocation + '/' + shot_time, "--capture-image-and-download"]
                p = Process(target=count_down)
                #p.start()
                live_view()
                
                win4.raiseWindow()
                time.sleep(1)
                
                #for j in range(3,0,-1):
                #   count_down(j)
                #p.terminate()
                gp(captureAndDownload)
                if i == 0:
                    win1.raiseWindow()
                    time.sleep(1)
                elif i == 1:
                    win2.raiseWindow()
                    time.sleep(1)
                else:
                    win5.raiseWindow()
                    #change "collageDouble" to "collage" for wedding template
                    collage_filepath = collageDouble(saveLocation)
                    send_to_printer(collage_filepath)
            time.sleep(20)
            win3.raiseWindow()
                #p.terminate()
                
    #SCREEN = reInit()
    '''
    while True:
        SCREEN.blit(BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # TODO: need to find a way to terminate live view after pictures are taken
                # Commented process lines are for testing purposes
                #p = Process(target=live_view)
                #p.start()
                #time.sleep(2)
                pygame.display.quit()
                # TODO: Need to add image in between pictures being taken
                for i in range(3):
                    shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    captureAndDownload = ["--filename", saveLocation + '/' + shot_time, "--capture-image-and-download"]
                    p = Process(target=live_view)
                    p.start()
                    time.sleep(2)
                    for j in range(3,0,-1):
                        count_down(j)
                    p.terminate()
                    gp(captureAndDownload)
                #p.terminate()
                
                #currently on friendsmas template; change "collageDouble" to "collage" for wedding template
                collage_filepath = collageDouble(saveLocation)
                send_to_printer(collage_filepath)
                #TODO: put in screen that says image is printing
                SCREEN = reInit()
        pygame.display.update()
        '''
