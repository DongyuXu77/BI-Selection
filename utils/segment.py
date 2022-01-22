from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot
kernel = 0.06*np.ones((5,5))
def test():
	image = cv2.imread('./test.png')
	pyplot.imshow(image)
	#pyplot.show()
	img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	mask_kernel = cv2.filter2D(image, -1, kernel)
	hsv = cv2.cvtColor(mask_kernel, cv2.COLOR_BGR2Lab)
	low_hsv = np.array([180, 0, 0], dtype=np.uint8)
	high_hsv = np.array([225, 225, 225], dtype=np.uint8)

	mask = cv2.inRange(hsv, low_hsv, high_hsv)
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	ret, threshl = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	pyplot.imshow(image[:, :, 1], "gray")
	pyplot.show()
def test_1():
	image = Image.open('./test.png')
	image_1 = image.convert('L')
	image_1 = np.array(image_1)
	
	Threshold = 254
	for l_1 in range(len(image_1)):
		for l_2 in range(len(image_1[0])):
			image_1[l_1][l_2] = 255 if image_1[l_1][l_2]>Threshold else 0
	pyplot.imshow(image_1)
	pyplot.show()
if __name__=="__main__":
	test_1()
