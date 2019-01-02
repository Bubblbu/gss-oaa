#!/usr/bin/python
# # -*- coding: utf-8 -*-

import requests
import pandas as pd
from pathlib import Path
from argparse import ArgumentParser

"""
Verification

- duplicates
- mark entries that are valid, invalid, or need manual control
"""


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", help="Input file", metavar="FILE")
    args = parser.parse_args()

    root = Path("../")
    inputfile = root / args.filename

    df = pd.read_csv(inputfile)

    # Check if duplicate entries

    # 