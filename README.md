# maldi2masst

Take MALDI data from timsTOF converted using [TIMSCONVERT](https://github.com/gtluu/timsconvert) and get a peak list from a single spectrum written to a text file to use with [GNPS MASST](https://masst.ucsd.edu/). Expects an mzML file with only one spectrum. Built for Windows 10.

## Installation

### Setting Up Your Local Environment

If you prefer to run TIMSCONVERT locally via Nextflow or the CLI, you can set up an environment to do so. Please note
that TIMSCONVERT should be run under Linux or Windows. macOS is not supported.

#### Install Anaconda on Linux

1. Download and install Anaconda for [Linux](https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh). 
Follow the prompts to complete installation. Anaconda3-2021.11 for Linux is used as an example here.
```
wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
bash /path/to/Anaconda3-2021.11-Linux-x86_64.sh
```
2. Add ```anaconda3/bin``` to PATH.
```
export PATH=$PATH:/path/to/anaconda3/bin
```

#### Install Anaconda on Windows.

1. Download and install Anaconda for [Windows](https://repo.anaconda.com/archive/Anaconda3-2021.11-Windows-x86_64.exe). 
Follow the prompts to complete installation.
2. Run ```Anaconda Prompt (R-MINI~1)``` as Administrator.

#### Set Up ```conda env```

3. Create a conda instance.
```
conda create -n maldi2masst python=3.7
```
4. Activate conda environment.
```
conda activate maldi2masst
```

#### Install maldi2masst

5. Download maldi2masst by cloning the Github repo.
```
git clone https://www.github.com/gtluu/maldi2masst
```
6. Install dependencies.
```
# maldi2masst dependencies
pip install -r /path/to/maldi2masst/requirements.txt
```

## Command Line Interface Usage

The CLI version of maldi2masst supports conversion of all experimental data types specified above.

Use ```maldi2masst.py``` to run maldi2masst. The input directory and experiment type. Unless specified, all other 
default parameters for all other values will be used.
```
python /path/to/maldi2masst/maldi2masst.py -i /path/to/data -o /path/to/output/directory
or
python3 /path/to/maldi2masst/maldi2masst.py -i /path/to/data -o /path/to/output/directory
```
