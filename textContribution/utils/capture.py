import time
from PIL import Image
import pyscreenshot

def screenshot(path='./test.png', ratio=2.0):
	time.sleep(5)
	image = pyscreenshot.grab()
	height, width = image.size
	print(image.size)
	image = image.resize((int(height/ratio), int( width/ratio)), Image.ANTIALIAS)
	image.save(path)
	print(image.size)
if __name__=="__main__":
	screenshot()
