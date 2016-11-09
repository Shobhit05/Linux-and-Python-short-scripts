import subprocess
a=int(input("selcet one of the options \n 1:to shut down the computer \n 2:to restart your computer \n 3:to make a directory \n 4:to change the password for unix\n else anykey to start a video"))
if(a==1):
    print(subprocess.call(["sudo","init","0"]))
elif(a==2):
    print(subprocess.call(["sudo","init","6"]))

elif(a==3):
    print(subprocess.call(["mkdir","shobhit"]))
elif(a==4):
    print(subprocess.call(["passwd","shobhit"]))
else:
    print(subprocess.call(["vlc","/home/shobhit/shobhit/video/sanamre"]))
