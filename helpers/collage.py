from PIL import Image

import os

def collage(saveFolder):
	files = os.listdir(saveFolder)
	files = [f for f in files if os.path.isfile(saveFolder+'/'+f)]
	files.sort()
	lastThreePhotos = files[-3:]

	template = Image.open('/home/jhdinh/Desktop/gphoto/assets/photobooth-layout.png')

	"""
	template size is 1800 x 1200 px
	printer prints slightly crooked and leaves a larger margin on the left side (75px) compared to right side (60px)
	top and bottom have 0px margin
	"""
	template_w = 1800
	template_h = 1200

	# margins specific to the Brother MFC-J6530DW with 4"x6" input
	x_margin_l = 0
	x_margin_m = 30
	x_margin_r = 15
	y_margin = 30

	# image size is 855 x 555 px
	photo_w = int((template_w - x_margin_l - x_margin_m - x_margin_r)/2)
	photo_h = int((template_h - y_margin * 3)/2)

	# coordinates corredpond to the upper left corner of the photo
	# x and y coordinates of pic1
	p1_x = x_margin_l + photo_w + x_margin_m
	p1_y = y_margin

	# x and y coordinates of pic2
	p2_x = x_margin_l
	p2_y = 2 * y_margin + photo_h

	# x and y coordinates of pic3
	p3_x = x_margin_l + photo_w + x_margin_m
	p3_y = 2 * y_margin + photo_h

	pic1 = Image.open(saveFolder + '/' + lastThreePhotos[0]).resize((photo_w, photo_h))
	pic2 = Image.open(saveFolder + '/' + lastThreePhotos[1]).resize((photo_w, photo_h))
	pic3 = Image.open(saveFolder + '/' + lastThreePhotos[2]).resize((photo_w, photo_h))

	template.paste(pic1, (p1_x, p1_y, p1_x + photo_w, p1_y + photo_h))
	template.paste(pic2, (p2_x, p2_y, p2_x + photo_w, p2_y + photo_h))
	template.paste(pic3, (p3_x, p3_y, p3_x + photo_w, p3_y + photo_h))
	
	collage_filepath = ('/home/jhdinh/Desktop/gphoto/collages/' + lastThreePhotos[2] + '.png')
	template.save(collage_filepath)
	
	return collage_filepath

def collageDouble(saveFolder):
	files = os.listdir(saveFolder)
	files = [f for f in files if os.path.isfile(saveFolder+'/'+f)]
	files.sort()
	lastThreePhotos = files[-3:]

	template = Image.open('/home/jhdinh/Desktop/gphoto/assets/fatcousins.png')

	"""
	the template size is 1200 x 1800 px
	printer prints slightly crooked and leaves a larger margin on the right side (30px) compared to left side (24px)
	top and bottom have 0px margin
	this is for non FullBleed printing
	"""
	template_w = 1200
	template_h = 1800

	#calculate margins
	x_margin_l = 6
	x_margin_m = 30
	y_margin_t = 155
	y_margin_m = 30
	y_margin_b = 535


	# image size is 855 x 555 px
	photo_w = int((template_w - x_margin_l - x_margin_m * 2)/2)
	photo_h = int((template_h - y_margin_t - y_margin_m * 2 - y_margin_b)/3)

	# x and y coordinates of pic1
	p1_x = x_margin_l
	p1_y = y_margin_t

	# x and y coordinates of pic2
	p2_x = x_margin_l
	p2_y = y_margin_t + photo_h + y_margin_m

	# x and y coordinates of pic3
	p3_x = x_margin_l
	p3_y = y_margin_t + 2 * photo_h + 2 * y_margin_m

	scoot_to_right = photo_w + 2 * x_margin_m
	p1_x2 = p1_x + scoot_to_right
	p2_x2 = p2_x + scoot_to_right
	p3_x2 = p3_x + scoot_to_right

	pic1 = Image.open(saveFolder + '/' + lastThreePhotos[0]).resize((photo_w, photo_h))
	pic2 = Image.open(saveFolder + '/' + lastThreePhotos[1]).resize((photo_w, photo_h))
	pic3 = Image.open(saveFolder + '/' + lastThreePhotos[2]).resize((photo_w, photo_h))

	template.paste(pic1, (p1_x, p1_y, p1_x + photo_w, p1_y + photo_h))
	template.paste(pic2, (p2_x, p2_y, p2_x + photo_w, p2_y + photo_h))
	template.paste(pic3, (p3_x, p3_y, p3_x + photo_w, p3_y + photo_h))
	template.paste(pic1, (p1_x2, p1_y, p1_x2 + photo_w, p1_y + photo_h))
	template.paste(pic2, (p2_x2, p2_y, p2_x2 + photo_w, p2_y + photo_h))
	template.paste(pic3, (p3_x2, p3_y, p3_x2 + photo_w, p3_y + photo_h))

	collage_filepath = ('/home/jhdinh/Desktop/gphoto/collages/' + lastThreePhotos[2] + '.png')
	template.save(collage_filepath)
	
	return collage_filepath

if __name__ == "__main__":
	collage("test/")
