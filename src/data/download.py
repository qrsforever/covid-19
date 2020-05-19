#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import requests


# hosts: 199.232.68.133 raw.githubusercontent.com

CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../cache') # noqa
URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series' # noqa
FILES = [
    'time_series_covid19_recovered_global.csv',
    'time_series_covid19_deaths_global.csv',
    'time_series_covid19_confirmed_global.csv'
]


def fetch_data():
    print(CACHE_DIR)
    dst_dir = f'{CACHE_DIR}/datasets'
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for item in FILES:
        print('get {}'.format(item))
        content = requests.get(f'{URL}/{item}')
        with open(f'{dst_dir}/{item}', 'wt') as fw:
            fw.write(content.text)


if __name__ == "__main__":
    fetch_data()
