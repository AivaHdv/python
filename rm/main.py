import os
import shutil

garbage = '/home/ivan/garbage/'

changer = raw_input("Your change is : ")
if changer == "rm":
        print ("What file i'll should delete :")
        rm_path = raw_input()
        if rm_path is None:
            print ("Couldn't find this directory/file.Try again")
        else:
            now = os.getcwd()
            os.chdir(rm_path)
            f = open('path.txt', 'w')
            recovery_path = os.path.dirname(rm_path)
            f.write(recovery_path)
            shutil.move(rm_path, garbage)
            os.chdir(now)

if changer == "clear":
        shutil.rmtree(garbage, ignore_errors=False, onerror=None)
        os.mkdir(garbage)






