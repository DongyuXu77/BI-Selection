import os
import numpy as np
from PIL import Image
from matplotlib import pyplot

def grayImage(path):
	image = Image.open(path)
	image_gray = image.convert('L')
	image_gray = np.array(image_gray)
	Threshold = 255
	for l_1 in range(len(image_gray)):
		count = 0
		for l_2 in range(len(image_gray[1])):
			if image_gray[l_1][l_2]>=Threshold:
				image_gray[l_1][l_2] = 255
				count = count+1
			else:
				image_gray[l_1][l_2] = 0
		if count/len(image_gray[1])<0.3:
			for l_2 in range(len(image_gray[1])):
				image_gray[l_1][l_2] = 0
	if (os.path.exists('./saved_picture')) is False:
		os.makedirs('./saved_picture')
	image_gray = Image.fromarray(image_gray)
	image_gray.save('./saved_picture/'+os.path.basename(path))
if __name__=="__main__":
	grayImage('./test.png')
