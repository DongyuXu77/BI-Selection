import pyscreenshot
import time

def screenshot(path='./test.png'):
	time.sleep(10)
	image = pyscreenshot.grab()
	image.save(path)

if __name__=="__main__":
	screenshot()
