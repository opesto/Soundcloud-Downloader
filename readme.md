# SoundCloud downloader

Installation instructions:  
[windows](#windows)
[mac](#mac)

## Windows

Follow these steps exactly.

#### Setup

1. Install python
    * Go to https://www.python.org/downloads/release/python-278/
    * Download the `.msi` (Microsoft installer) file labelled `Windows x86 MSI Installer (2.7.8)`
    * Run the `python-2.7.8.msi` file
    * A window will pop up to help you through the installation
    * Keep clicking `Next` - the defaults are all fine.

0. Restart your computer
    * If you skip this step, other things may fail for no apparent reason. I'd recommend doing this.

0. Install pip
    * Go to http://www.pip-installer.org/en/latest/installing.html
    * Where it says `To install or upgrade pip, securely download get-pip.py`, right-click on `get-pip.py` and click "Save Link As".
    * Save it in `C:\Python27\`

0. Install git
    * Go to http://git-scm.com/download/win
    * Download the `.exe` installer file
    * Run the `.exe` installer file
    * A window will pop up to help you through the installation
    * Keep clicking `Next` - the defaults are all fine.

0. Open up a `git bash` command prompt
    * Hit the windows key on your keyboard **or** click the start button
    * type `git bash`, and hit Enter

0. Type `cd C:\Python27` and hit Enter

0. Type `python get-pip.py` and hit Enter

0. Type `cd Scripts` and hit Enter

0. Type `pip install mutagen` and hit Enter

0. Type `pip install requests` and hit Enter

0. Type `cd ..` and hit Enter

0. Type `git clone https://github.com/rosshamish/soundcloud-downloader` and hit Enter

0. Type `cd soundcloud-downloader` and hit Enter

0. Make a new folder on your desktop called `Soundcloud-Downloads`. Find its exact "path" by right-clicking on it and selecting `Properties`. Keep this path around, you'll need it in the next step. It should look something like "C:\Users\<yourname>\Desktop\Soundcloud-Downloads"

0. Open a file explorer
    
    Click `Computer` in the left sidebar.

    Click `C:`

    Click `Python27`

    Click `soundcloud-downloader`

    Edit the python code file `soundcloud-downloader.py` by right-clicking and selecting `Edit`

    In the code, replace this line `destination_folder = '/Users/<your-name>/Music/Soundcloud'`

    With this line `destination_folder = r'C:\Users\<yourname>\Desktop\Soundcloud-Downloads'`

    (This should be the same path as in the previous step)

Congrats! You're done all the hard stuff.

#### Regular workflow

1. Open a `git bash` command prompt
    * Hit the windows key on your keyboard **or** click the start menu
    * Type `git bash`
    * Hit Enter

0. In git bash, type `cd C:\Python27\soundcloud-downloader`, and hit Enter

0. In git bash, type `python soundcloud-downloader.py <URL-of-a-song>`, and hit Enter

0. The downloaded song should be in `C:\Users\<yourname>\Desktop\Soundcloud-Downloads`

Cool.

## Mac

Follow these steps exactly.

#### Setup

1. [Install](http://git-scm.com/download/mac) git

3. Open Terminal
    * How-to: Open Finder. Click on `Applications`, then `Utilities`. 
    * Important: when in the Terminal, type every line which starts with `$`

            $ like this

        Type the "`like this`" part **exactly**, and hit Enter on your keyboard after each line. For each command, expected output is shown

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

To learn more, or to get help, contact [ross](https://github.com/rosshamish/) or [olive](https://github.com/opesto)

[Learn more about git]

[Learn more about python]

[Firefox]: https://www.mozilla.org/en-US/firefox/new/
[Chrome]: http://www.google.ca/chrome/

[Learn more about python]: http://docs.activestate.com/activepython/2.7/easytut/index.html
[Learn more about git]: http://cswsolutions.com/featured-post/git-for-non-developers/
