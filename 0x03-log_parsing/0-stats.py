#!/usr/bin/python3
"""
0-stats.py
This module contains a script that reads stdin
line by line and computes metrics:
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
"""

import sys
import re


if __name__ == '__main__':
    total_file_size = 0
    status_codes = {}
    possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    pattern = r'(\S+) - \[(.*?)\] "(.*?)" (\S+) (\S+)'
    counter = 0

    try:
        for line in sys.stdin:
            match = re.match(pattern, line)
            if match:
                ip_address, date, request, status_code, file_size = \
                    match.groups()
                try:
                    int_status_code = int(status_code)
                except Exception:
                    counter += 1
                    continue
                if int_status_code not in possible_codes:
                    continue
                if int_status_code in status_codes.keys():
                    status_codes[int_status_code] += 1
                else:
                    status_codes[int_status_code] = 1
                total_file_size += int(file_size)
                counter += 1
                if counter != 0 and counter % 10 == 0:
                    print("File size: {:d}".format(total_file_size))
                    sc_keys = sorted(status_codes.keys())
                    for key in sc_keys:
                        print("{:d}: {:d}".format(key, status_codes[key]))
            else:
                continue
    except KeyboardInterrupt:
        print("File size:", total_file_size)
        sc_keys = sorted(status_codes.keys())
        for key in sc_keys:
            print("{:d}: {:d}".format(key, status_codes[key]))

    print("File size:", total_file_size)
    sc_keys = sorted(status_codes.keys())
    for key in sc_keys:
        print("{:d}: {:d}".format(key, status_codes[key]))
