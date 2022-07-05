
import subprocess

import glob

files = glob.glob('./test_*.py')

for file in files:
    subprocess.call('python %s' % file)
