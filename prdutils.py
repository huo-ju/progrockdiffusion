import os
from os import path
#from os.path import exists

# Simple create paths taken with modifications from Datamosh's Batch VQGAN+CLIP notebook
def createPath(filepath):
    if path.exists(filepath) == False:
        os.makedirs(filepath)
        print(f'Made {filepath}')
    else:
        pass


