from __future__ import print_function
import os, time
import pyzbar.pyzbar as pyzbar
from PIL import Image
import numpy as np
import cv2
from more_itertools import locate
from PyPDF2 import PdfFileMerger


path_to_watch = "watch"
##"S:/Users/jduysen/scans"
converted_path = "converted"
merge_path = "merged"

before = dict ([(f, None) for f in os.listdir(path_to_watch)])
def decode(im):
    decodedObjects = pyzbar.decode(im)
    for obj in decodedObjects:
##        print(obj.data)
        if decodedObjects:
            files.append(1)
            barFile = str(obj.data.decode('utf-8'))
##            print("this is the current barfile"+barFile)
            bars.append(obj.data.decode('utf-8'))
##            print(bars)
            barcount = 1
            return barFile
        else:
            files.append(0)
        

while 1:
    time.sleep(10)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:    
##        print(added)
        cv2list = []
        sep = []
        files = []
        bars = []
        barcount = 1
        
        for filename in os.listdir(path_to_watch):
            image = cv2.imread(path_to_watch+'/'+filename)
            cv2list.append(image)
            if decode(image):
                barFile = decode(image)
            else:
                barFile = barFile
            os.rename(path_to_watch+'/'+filename, path_to_watch+'/'+barFile+str(barcount)+'.jpg')
            barcount += 1
##        print(files)
        count = 1
        for filename in os.listdir(path_to_watch):
            
            jpg = path_to_watch+'/'+filename
            im = Image.open(jpg)
            if im.mode == "RGBA":
                im = im.convert("RBG")

            new_filename = filename.replace('.jpg', '.pdf')

            if not os.path.exists(converted_path+'/'+new_filename):
                im.save(converted_path+'/'+new_filename, "PDF", resolution = 100.0)
                count += 1
            os.remove(path_to_watch+'/'+filename)
        merges = [i for i, x in enumerate(files) if x == 1]
        bars = list(dict.fromkeys(bars))
##        print(bars)
##        print(merges)
        for bar in bars:
            merger = PdfFileMerger()
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            for filename in os.listdir(converted_path):
##                filename = os.listdir(converted_path+'/'+filename)
                if filename.startswith(bar):
                    merger.append(converted_path+'/'+filename)
##                    print(filename)
##            print(bar)
            if not os.path.exists(merge_path+'/'+bar+'_'+timestamp+'.pdf'):
                merger.write(merge_path+'/'+bar+'_'+timestamp+'.pdf')
            
            merger.close()
        for filename in os.listdir(converted_path):
            os.remove(converted_path+'/'+filename)
            
    

    before = after
