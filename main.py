from time import sleep
from datetime import datetime
from multiprocessing import Process
from sh import gphoto2 as gp


from collage import collage
from countDown import count_down
from displayPushToStart import display_push_to_start
from liveView import live_view
from sendToPrinter import send_to_printer


import cv2
import pygame, sys
import signal, os, subprocess
import time

sys.path.append("/home/jhdinh/Desktop/gphoto/helpers")
shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "PiPhotos"
folderName = shot_date + picID
saveLocation = "/home/jhdinh/Desktop/gphoto/images/" + folderName
captureAndDownload = ["--filename", saveLocation + '/' + shot_time, "--capture-image-and-download"]
BG = pygame.image.load("assets/PushToStart.png")
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
    

def main_menu():
    killgphoto2Process()
    createSaveFolder()
    SCREEN = reInit()
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
                collage_filepath = collage(saveLocation)
                send_to_printer(collage_filepath)
                #TODO: put in screen that says image is printing
                SCREEN = reInit()
        pygame.display.update()

main_menu()
