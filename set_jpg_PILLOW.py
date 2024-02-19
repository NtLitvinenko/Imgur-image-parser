from PIL import Image
import glob
import random
import os

ilist = []
for filename in glob.glob('validi/*.jpg'): #assuming gif
    try:
        im = Image.open(filename)
        ilist.append(im)
    except: print("Image format error..."); continue


cw = 0
for img in ilist:
    imgf = img.format.lower()
    if imgf != "jpeg":
        cw += 1
        print(f"File correct... Saving...")
        img.save(f"WI-{cw}")
    else:
        print("File incorrect... Saving...")
        fn = f"NWF-{random.randint(cw, cw+1000)}"
        img.save(fn)
        os.system(f"del {fn}")
