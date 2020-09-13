#!/usr/local/bin/python3.7

from datetime import datetime as dt
import os


IMAGE_DUMP_PATH = '/Users/meister/Public/Dropbox/Praxis-Photos/'
CLOUD_PATH = '/Users/meister/Library/Mobile Documents/com~apple~CloudDocs/'
PROJECT_PATH = os.path.join(CLOUD_PATH, 'Documents/code/tierarzt') + '/'
LOG_FILE_PATH = os.path.join(PROJECT_PATH, 'log.txt')

FIRST_QUARTER = '12Q3'

NOTDIENST_DATES = [
    (dt(2019, 7, 5), dt(2019, 7, 7)),
    (dt(2019, 7, 30), dt(2019, 7, 30)),
    (dt(2019, 8, 16), dt(2019, 8, 18)),
    (dt(2019, 9, 16), dt(2019, 9, 16)),
    (dt(2019, 9, 27), dt(2019, 9, 29)),
    (dt(2019, 11, 12), dt(2019, 11, 12)),
    (dt(2019, 11, 22), dt(2019, 11, 24)),
    (dt(2019, 12, 27), dt(2019, 12, 29)),
]
