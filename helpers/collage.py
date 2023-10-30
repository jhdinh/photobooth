from PIL import Image
import os

def collage(saveFolder):

	files = os.listdir(saveFolder)
	files = [f for f in files if os.path.isfile(saveFolder+'/'+f)]
	files.sort()
	lastThreePhotos = files[-3:]

	template = Image.open('assets/photobooth-layout.png')

	# 825 x 525 px
	pic1 = Image.open(saveFolder + '/' + lastThreePhotos[0]).resize((825, 535))
	pic2 = Image.open(saveFolder + '/' + lastThreePhotos[1]).resize((825, 535))
	pic3 = Image.open(saveFolder + '/' + lastThreePhotos[2]).resize((825, 535))


	template.paste(pic1, (920, 50, 1745, 585))
	template.paste(pic2, (50, 625, 875, 1160))
	template.paste(pic3, (920, 625, 1745, 1160))

	template.save('collages/' + lastThreePhotos[2] + '.png')
