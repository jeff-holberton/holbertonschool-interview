#!/usr/bin/python3
"""stats module"""

import sys
import re
import time



def print_status(status_codes, file_size):
    print(f"File size: {file_size}")
    for key in sorted(status_codes):
        if status_codes[key] != 0:
            print(f"{key}: {status_codes[key]}")

def main():
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    file_size = 0
    lines_read = 0
    pattern = re.compile(r'^(\d{1,3}(?:\.\d{1,3}){3}) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

    try:
        for line in sys.stdin:
            if lines_read == 10:
                print_status(status_codes, file_size)
                lines_read = 0
            line_matches = pattern.fullmatch(line.rstrip('\n'))
            if line_matches:
                ip, date, status, size = line_matches.groups()
                if int(status) in status_codes:
                    status_codes[int(status)] += 1
                    file_size += int(size)
                    lines_read += 1
            else:
                print(f"SKIPPED: {line!r}", file=sys.stderr)
    except KeyboardInterrupt:
        print_status(status_codes, file_size)
        time.sleep(1)
        return
    print_status(status_codes, file_size)
    
    


if __name__ == "__main__":
    main()
