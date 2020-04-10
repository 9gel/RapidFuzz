# SPDX-License-Identifier: MIT
# Copyright © 2020 Max Bachmann

from rapidfuzz._utils import *
import re

def default_process(sentence: str):
    alnum_re = re.compile(r"(?ui)\W")
    return alnum_re.sub(" ", sentence).strip().lower()