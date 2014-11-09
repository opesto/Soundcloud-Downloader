SoundCloud downloader for MACS

Follow these steps exactly:

1) Download Git  : http://git-scm.com/download/mac
2) Download Python : https://www.python.org/downloads/release/python-342/
3) Go to Finder, then go to Applications. Look for Utilities, open Terminal which is inside Utilities.
4) Once inside Terminal, you need to check to see if both python and git were downloaded.  Type : Git --version
git version 1.9.3 should be printed to the screen (or which ever version you have).
Then, check if Python was downloaded.  Type : Python --version
Python version 2.7.5 should be printed to the screen (or which ever version you have).
5) If both Python and Git’s versions were printed to the screen. Now, choose a destination for all your downloaded songs to go to.  I for example went to Music inside Finder, and made a folder called Soundcloud.
6) Now go back inside Terminal. Type: mkdir python-soundcloud-dl (nothing should happen)
7) Type: cd python-soundcloud-dl
8) Type: git clone https://github.com/sachinrudr/Soundcloud-Downloader
9) Type: cd Soundcloud-Downloader
10)  Type: sudo easy_install pip
11) Type: sudo pip install mutagen
12) Type: sudo pip install requests
13)  Type: emacs soundcloud-downloader.py (some programming code should pop up)
14)  Now you have to figure out the path with which you want to save your music to. I have my music downloaded to a folder called Soundcloud in Music, in Finder.
So my path is “/Users/<your name here>/Music/Soundcloud”. If you are still not sure what the path is, right click on the folder you are downloading your music to and click the “get info” option. A small window should pop up and right next to “where”, it should say the path of where the folder is. For me it would say /Users/Oliver/Music. Add /<name of folder> to the end of it, to make the path /Users/Olivier/Music/Soundcloud. This is the path you will use in the next step.
15)  In the code, in terminal (about 15 lines down)
replace this line:
DIRECTORY = raw_input("Where do you want to put the files?\ndefault is '/media/Data/Music/Untagged': ") or '/media/Data/Music/Untagged'

with this line:

DIRECTORY = “<name of the path from step 14)>”
So I would have replaced it with: 
DIRECTORY = "/Users/Olivier/Music/Soundcloud”
16) Now save and exit back to the terminal by typing control x, control c.
17) Congratulations you’re done all the hard stuff! Now find the url to the soundcloud song you want to download. You can even download all your likes on soundcloud. Just simply click on your likes page on soundcloud and use the url to that page. The url should look like this: https://soundcloud.com/name/likes 
18) To download a song or all your likes type : 
python soundcloud-downloader.py <the url from step 17 here>
so for example type, 
python soundcloud-downloader.py https://soundcloud.com/willowbeats/willow-beats-triple-j-mix-up-exclusive
19)  Every time you download something you have to be in the 
Soundcloud-Downloader directory. If you are reopening the terminal to download something new, re do steps 7 and 9. And then redo step 18 with the new url you want to download.
