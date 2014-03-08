from easygui import *
import os

while 1:
    result = enterbox(msg='Paste soundcloud link here', title='Soundcloud Downloader', default='', strip=True, image=None, root=None)    
    os.system('soundcloud-downloader.py --id3tags "' + result + '"')
