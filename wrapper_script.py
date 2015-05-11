import os
import subprocess
import sys

os.environ['LD_LIBRARY_PATH'] = "/usr/local/cuda-7.0/lib64/"
subprocess.Popen(['python test_gpu.py'],env=os.environ)
