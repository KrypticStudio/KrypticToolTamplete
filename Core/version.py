### Kryptic Studio ###

# Local Libraries

# Libraries

# Standard Libraries
import urllib.request
import curses
import webbrowser
import sys
import time

# Function Deffinitions

def progressbar(it, prefix="", size=60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()



def CheckVersion():
    for i in progressbar(range(10), "Checking for update: ", 40):
        time.sleep(0.05) #Calulcation Speed
    versionTxtF = open("Version/version.txt", "r")

    versionLink = "https://raw.githubusercontent.com/KrypticStudio/KrypticToolTamplete/master/Version/version.txt" #LINK TO RAW FILE ON LINE

    uptodatev = urllib.request.urlopen(versionLink)
    liveversion = None
    version = None
    for line in uptodatev: # files are iterable
        liveversion = line[9:]

    liveversion = liveversion.decode()
    for line in versionTxtF:
        version = line[9:]

    if version == liveversion:
        print("Kryptic Tools Tamplete is up to date!\n")
    elif version != liveversion:
        if version[5:] > liveversion[5:]:
            print("Sorry! Kryptic Tools Tamplete Tools has been tampered with. \nCan Not Open!")
            webbrowser.open("http://www.kryptic-studio.com")
        else:
            print("***UPDATE {} AVAILABLE*** \n - Some features may not work as intended until you update to the newest version.\n - Visit repository to update!\n".format(liveversion))
            webbrowser.open("http://www.kryptic-studio.com")

CheckVersion()