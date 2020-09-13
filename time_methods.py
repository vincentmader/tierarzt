#!/usr/local/bin/python3.7

from datetime import datetime as dt
import json

from config import FIRST_QUARTER, PROJECT_PATH


def get_all_quarters(start=None, end=None):
    if start:
        start_year_num = int(start.split('Q')[0])
        start_quarter_num = int(start.split('Q')[1])
    else:
        start_year_num = int(FIRST_QUARTER.split('Q')[0])
        start_quarter_num = int(FIRST_QUARTER.split('Q')[1])

    if end:
        end_year_num = int(end.split('Q')[0])
        end_quarter_num = int(end.split('Q')[1])
    else:
        end_year_num = dt.now().year - 2000
        end_quarter_num = int(get_current_quarter().split('Q')[1])

    quarters = []
    while start_year_num <= end_year_num:
        quarter = '{}Q{}'.format(start_year_num, start_quarter_num)
        quarters.append(quarter)

        if start_quarter_num == 4:
            start_year_num += 1
            start_quarter_num = 0

        start_quarter_num += 1
        if start_year_num == end_year_num and start_quarter_num > end_quarter_num:
            break

    return quarters


def get_current_quarter():
    return get_quarter_from_date(dt.now().strftime('%Y-%m-%d'))


def get_quarter_from_date(date):
    year_num = date.split('-')[0][2:]
    quarter_num = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4, 12: 4}[int(date.split('-')[1])]
    return '{}Q{}'.format(year_num, quarter_num)


def get_quarters_that_need_update():
    with open('{}/last_update.json'.format(PROJECT_PATH)) as fp:
        last_update = json.load(fp)[0]

    if get_quarter_from_date(last_update) != get_current_quarter():
        return get_all_quarters(start='12Q3')

    return get_all_quarters(start=get_quarter_from_date(last_update))

