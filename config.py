#!/usr/local/bin/python3.7

from datetime import datetime as dt
import os


IMAGE_DUMP_PATH = '/home/vinc/Dropbox/Praxis-Photos/'
PROJECT_PATH = '/home/vinc/code/tierarzt/'
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
