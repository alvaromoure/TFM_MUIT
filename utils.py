import os
import nibabel
import numpy as np

def get_num_files(path):
    return len(os.listdir(path))

def read_nii(path, rotate=False):
    ct_scan = nibabel.load(path)
    array = ct_scan.get_fdata()
    if rotate:
        array = np.rot90(np.array(array))
    return array