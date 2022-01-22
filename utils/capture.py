import pyscreenshot

def screenshot(path='./test.png'):
	image = pyscreenshot.grab()
	image.save(path)

if __name__=="__main__":
	screenshot()
