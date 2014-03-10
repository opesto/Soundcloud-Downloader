# Soundcloud-Downloader

A tool which can be used to download music files from SoundCloud.com even if the download button is not available

A fork of [013's Soundcloud-Downloader](https://github.com/013/Soundcloud-Downloader).  
Additions:
- automatic iTunes library addition
- a small GUI

### Requirements
easygui (for the GUI)
http://easygui.sourceforge.net/download/version_0.96/index.html

ID3-PY (for name tagging)
http://id3-py.sourceforge.net/

Requests (for downloading SoundCloud pages)
pip install requests
--note: for Windows, use [win-pip](https://sites.google.com/site/pydatalog/python/pip-for-windows). **Follow the installation instructions**.

### Usage
Open a terminal/command prompt in the directory which contains your Music directory (the one with the iTunes directory inside of it). Then run  
```
git clone https://github.com/RossHamish/Soundcloud-Downloader
```
Your directory structure should look like this:  
```
.  
+-- Music  
|   +-- iTunes  
|       +-- iTunes Media  
|           +-- Automatically Add to iTunes  
|   +-- Soundcloud-Downloader  
|       +-- soundcloud-downloader.py  
|       +-- soundcloud-downloader-GUI.py  
```
Now:
```
cd Soundcloud-Downloader
soundcloud-downloader-GUI.py
```

Navigate to a SoundCloud song or playlist, copy the URL, paste it in the text box and hit OK. You should see the result of the operation in your command prompt, and iTunes will add the file to your library on next run (or immediately if it is currently running).

### Legal
This software is intended as proof of concept. This source is to be used for educational purposes under the laws in your area. 
This software is provided AS-IS without any warranty of any kind, implied or otherwise.
