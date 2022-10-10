import argparse
import os
import sys
#import subprocess
import numpy as np
from pyteomics import mzml as pyt


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='Input mzML file with single spectrum from timsTOF MALDI', required=True, type=str)
    parser.add_argument('-o', help='Output file location', required=True, type=str)
    return vars(parser.parse_args())


def format_arrays_for_masst(spectrum):
    if spectrum['m/z array'].size == spectrum['intensity array'].size:
        masst_string = ''
        for i in range(0, spectrum['m/z array'].size):
            median_int = np.median(spectrum['intensity array'])
            if spectrum['intensity array'][i] > median_int * 2:
                masst_string += str(spectrum['m/z array'][i]) + ' '
                masst_string += str(spectrum['intensity array'][i]) + '\n'
        return masst_string[:-1]


def main():
    args = get_args()
    mzml_data = list(pyt.read(args['i']))
    if len(mzml_data) == 1:
        peak_str = format_arrays_for_masst(mzml_data[0])
        #subprocess.call('echo "' + peak_str + '"|clip', shell=True)
        with open(os.path.join(args['o'], 'maldi_peak_list.txt'), 'w') as peak_file:
            peak_file.write(peak_str)
    else:
        print('More than one spectrum found. Abort.')
        sys.exit(1)


if __name__ == '__main__':
    main()
