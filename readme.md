SoundCloud downloader - mac instructions

Follow these steps exactly.

#### Setup

1. [Download](http://git-scm.com/download/mac) and [install](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git#Installing-on-Mac) git

2. [Download python](https://www.python.org/downloads/release/python-342/)

3. Open Terminal
    * How-to: Open Finder. Click on `Applications`, then `Utilities`. 
    * Important: when in the Terminal, type *exactly* what is shown

            $ like this

        and hit Enter on your keyboard after each line. For each command, expected output is shown

            like this
    
            (and comments look like this)

4. Verify that python and git were installed correctly.

        $ git --version
        git version #.#.#

        (Where # is some number)
        (Do not type the $)

        $ python --version
        python version 2.#.#

        (Where # is some number)
        (Do not type the $)

5. Open Finder. Pick a folder to keep downloaded songs in, or create a new one. A good option is `"/Users/<your-name>/Music/Soundcloud”`. Keep Finder open.

6. Open Terminal.

        $ mkdir python-soundcloud-dl
        $ cd python-soundcloud-dl
        $ git clone https://github.com/rosshamish/soundcloud-downloader
        Cloning into 'soundcloud-downloader'...
        remote: Counting objects: 130, done.
        remote: Compressing objects: 100% (87/87), done.
        remote: Total 130 (delta 43), reused 130 (delta 43)
        Receiving objects: 100% (130/130), 28.27 KiB | 0 bytes/s, done.
        Resolving deltas: 100% (43/43), done.
        Checking connectivity... done.

        (Or similar)

        $ cd soundcloud-downloader

        $ sudo easy_install pip
        [sudo] password for <your-name>: 

        (type your password, then hit Enter on the keyboard)
        (no letters will appear - that is normal)
    
        Searching for pip
        Best match: pip #.#.#
        Adding pip 1.5.4 to easy-install.pth file
            Installing pip script to /some/path
            Installing pip2.7 script to /some/path
            Installing pip2 script to /some/path
    
        Using /some/path/
        Processing dependencies for pip
        Finished processing dependencies for pip
    
        $ sudo pip install mutagen
    
        Downloading/unpacking mutagen
        Downloading mutagen-#.#.#.tar.gz (850kB): 850kB downloaded
        Running setup.py (path:/some/path/to/setup.py) egg_info for package mutagen
            
        Installing collected packages: mutagen
        Running setup.py install for mutagen
            changing mode of build/scripts-#.#/mid3cp from 664 to 775
            ...
    
        Successfully installed mutagen
        Cleaning up...
    
        $ sudo pip install requests
    
        Downloading/unpacking requests
            Downloading requests-#.#.#-py2.py3-none-any.whl (459kB): 459kB downloaded
        Installing collected packages: requests
        Successfully installed requests
        Cleaning up...

        $ open -t soundcloud-downloader.py

        (Code will open in a text editor window)

7. In the code, replace `<your-name>` on this line with the name of your computer

        destination_folder = '/Users/<your-name>/Music/Soundcloud'

        (This should be the same path as in step 5)

8. Save the file, and quit TextEdit.

Congratulations! You’re done all the hard stuff! 

From now on only the [regular workflow](#regular-workflow) steps are necessary.

#### Regular workflow

1. Open a web browser: Safari, [Firefox], or [Chrome]
    * Go to soundcloud
    * Go to the page of a song or set which you own the rights to
    * Copy the page's address
        * Right click on the text, and select "copy" **or** hold 'Cmd' and press 'C'
        * It should look like one of:
            * `https://soundcloud.com/<user>/<track-name>`
            * `https://soundcloud.com/<user>/sets/<set-name>`
            * `https://soundcloud.com/<user>/likes `

2. Open Terminal (refer to setup step #3 if you've forgotten how)
    * To get the page-address: right click, then click 'paste'

            $ cd
            $ cd python-soundcloud-downloader
            $ cd soundcloud-downloader
            $ python soundcloud-downloader.py <page-address>
            Destination: /Users/<your-name>/Music/Soundcloud/
        
            (type the name of a sub-folder to put these particular tracks in)
            (hit Enter on the keyboard)
        
            Downloading: <track-name>.mp3
             10.32 Mbps (3.21/3.20MB): 100.00%

3. Open Finder.
    1. Go to your downloading folder. If you have been following exactly, it is `/Users/<your-name>/Music/Soundcloud`
    * The folder you named in the previous step will be there
    * Inside the folder will be each track downloaded

Cool

-----

This script is for academic use only. If abuse is reported, this repository will be removed.

To learn more, or to get help, contact [ross](https://github.com/rosshamish/)

[Learn more about git]

[Learn more about python]

[Firefox]: https://www.mozilla.org/en-US/firefox/new/
[Chrome]: http://www.google.ca/chrome/

[Learn more about python]: http://docs.activestate.com/activepython/2.7/easytut/index.html
[Learn more about git]: http://cswsolutions.com/featured-post/git-for-non-developers/
