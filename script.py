# Imgur photos downloader
# https://i.imgur.com/S1jmapR.png
import requests, string, random
import os
from PIL import Image
from threading import Thread

os.chdir("validi")


def check_img(filename):
	try:
		im = Image.open(filename)
		im.verify()
		im.close()
		im = Image.open(filename)
		im.transpose(Image.FLIP_LEFT_RIGHT)
		im.close()
		print(filename, ' work... saving')
		return True
	except:
		print(filename, ' corrupted... skipping.')
		return False


def thr_func():
	while True:
		iug = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
		url = f"https://i.imgur.com/{iug}.jpg"
		limg = open(f"{iug}.jpg", "wb")
		cnt = requests.get(url).content
		limg.write(cnt)
		if check_img(iug + ".jpg"):
			limg.close()
			wimg = open(f"{iug}.jpg", "wb")
			wimg.write(cnt)
			wimg.close()
		else:
			limg.close()
			os.system(f"del {iug}.jpg")


threads = []
for i in range(32):
	thread = Thread(target=thr_func)
	threads.append(thread)
	thread.start()
