import cv2
import numpy as np
from matplotlib import pyplot
def test():
	image = cv2.imread('./test.png')
	pyplot.imshow(image)
	pyplot.show()
	img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	ret, threshl = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	pyplot.imshow(threshl)
	pyplot.show()
	print('finish')
if __name__=="__main__":
	test()
