# -*- coding: utf-8 -*-

import subprocess
import re


def parse_output(pattern, args):
    try:
        out_str = subprocess.check_output(args)
        if isinstance(out_str, bytes):
            out_str = out_str.decode()
    except Exception:
        out_str = ''

    match = re.search(pattern, out_str)
    return match.group(1) if match else None


def ip_address():
    return parse_output(r'(\S*)', ['hostname', '-I'])
