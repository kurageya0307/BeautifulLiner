
import os
import subprocess

import glob

os.chdir(r"C:\\Users\yasu-kodama\python\BeautifulLiner\test\model")
files = glob.glob('./test_*.py')

for file in files:
    subprocess.call('python %s' % file)

os.chdir(r"C:\\Users\yasu-kodama\python\BeautifulLiner\test\logic")
files = glob.glob('./test_*.py')

for file in files:
    subprocess.call('python %s' % file)
