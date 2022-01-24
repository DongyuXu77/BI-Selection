import pyscreenshot
from PIL import Image

def screenshot(path='./test.png', ratio=2.0):
	image = pyscreenshot.grab()
	height, width = image.size
	image = image.resize((int(height/ratio), int( width/ratio)), Image.ANTIALIAS)
	image.save(path)
if __name__=="__main__":
	screenshot()
