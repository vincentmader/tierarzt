#!/usr/local/bin/python3.7

from datetime import datetime as dt
import os

# get linux distro
import platform
using_distro = False
try:
    import distro
    using_distro = True
except ImportError:
    pass
if using_distro:
    linux_distro = distro.linux_distribution()[0]
else:
    linux_distro = platform.linux_distribution()[0]

# set path variables
if linux_distro == 'Ubuntu':  # assume Ubuntu distribution runs on server
    PROJECT_PATH = '/home/vinc/tierarzt/'
    IMAGE_DUMP_PATH = '/home/vinc/Dropbox/Praxis-Photos/'
elif linux_distro == 'Arch Linux':  # assume this is my main PC
    PROJECT_PATH = '/home/vinc/code/tierarzt/'
    IMAGE_DUMP_PATH = None  # dropbox has not yet been setup, TODO
else:  # assume this case executes only on my macOS
    PROJECT_PATH = '/Users/meister/Library/Mobile Documents/' + \
        'com~apple~CloudDocs/Documents/code/tierarzt'  # TODO: correct path?
    IMAGE_DUMP_PATH = '/Users/meister/Public/Dropbox/Praxis-Photos/'

LOG_FILE_PATH = os.path.join(PROJECT_PATH, 'log.txt')

# where to start gallery?
FIRST_QUARTER = '12Q3'
# notdienst
NOTDIENST_DATES = [
    (dt(2019, 7, 5), dt(2019, 7, 7)),
    (dt(2019, 7, 30), dt(2019, 7, 30)),
    (dt(2019, 8, 16), dt(2019, 8, 18)),
    (dt(2019, 9, 16), dt(2019, 9, 16)),
    (dt(2019, 9, 27), dt(2019, 9, 29)),
    (dt(2019, 11, 12), dt(2019, 11, 12)),
    (dt(2019, 11, 22), dt(2019, 11, 24)),
    (dt(2019, 12, 27), dt(2019, 12, 29)),
    (dt(2021, 1, 8), dt(2021, 1, 10)),
    (dt(2021, 2, 2), dt(2021, 2, 2)),
    (dt(2021, 3, 12), dt(2021, 3, 14)),
    (dt(2021, 4, 20), dt(2021, 4, 20)),
    (dt(2021, 4, 30), dt(2021, 5, 2)),
    (dt(2021, 6, 25), dt(2021, 6, 27)),
    (dt(2021, 7, 7), dt(2021, 7, 7)),
    (dt(2021, 8, 13), dt(2021, 8, 15)),
    (dt(2021, 10, 8), dt(2021, 10, 10)),
    (dt(2021, 11, 19), dt(2021, 11, 21)),
    (dt(2021, 12, 7), dt(2021, 12, 7)),
]
