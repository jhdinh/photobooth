from PIL import Image
import os

def collage(saveFolder):

	files = os.listdir(saveFolder)
	files = [f for f in files if os.path.isfile(saveFolder+'/'+f)]
	files.sort()
	lastThreePhotos = files[-3:]

	template = Image.open('assets/photobooth-layout.png')
	
	template_x = 1800
	template_y = 1200

	photo_w = 810
	photo_h = 520

	p1_start_x = 923
	p1_start_y = 60

	p2_start_x = 75
	p2_start_y = 619

	p3_start_x = 923
	p3_start_y = 619

	pic1 = Image.open(saveFolder + '/' + lastThreePhotos[0]).resize((photo_w, template_y))
	pic2 = Image.open(saveFolder + '/' + lastThreePhotos[1]).resize((photo_w, template_y))
	pic3 = Image.open(saveFolder + '/' + lastThreePhotos[2]).resize((photo_w, template_y))


	template.paste(pic1, (p1_start_x, p1_start_y, p1_start_x + photo_w, p1_start_y + photo_h))
	template.paste(pic2, (p2_start_x, p2_start_y, p2_start_x + photo_w, p2_start_y + photo_h))
	template.paste(pic3, (p3_start_x, p3_start_y, p3_start_x + photo_w, p3_start_y + photo_h))

	template.save('collages/' + lastThreePhotos[2] + '.png')
