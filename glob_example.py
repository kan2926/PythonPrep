import os, glob
import shutil

os.chdir("/Users/kanya/Documents/GitHub/prep/PythonPrep")
directory = "/Users/kanya/Documents/GitHub/prep/PythonPrep/log"
for file in glob.glob('*.log'):
    print(file)
    if not os.path.exists(directory):
        os.makedirs(directory)
    shutil.move(file,directory)
        
