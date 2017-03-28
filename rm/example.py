import os
import shutil


garbage = '/home/ivan/garbage/'

rm_path = raw_input()
os.chdir(rm_path)
f = open('path.txt', 'w')
recovery_path = os.path.dirname(rm_path)
f.write(recovery_path)
shutil.move(rm_path, garbage)