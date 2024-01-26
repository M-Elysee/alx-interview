#!/usr/bin/python3
"""a Script that reads from standard input and computes metrics:
   on interruption or after 10 lines it prints the total file size
   and the count of read status codes where the input formart is:
   <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
   <file size>
"""


def statistics_display(size, status_codes):
    """Displays file size and status codes with their occurences"""

    print("File size: {}".format(size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                    '404': 0, '405': 0, '500': 0}

    try:
        i = 0
        for cmd_line in sys.stdin:
            args = cmd_line.split()
            if len(args) > 6:
                st_code = args[-2]
                fl_size = args[-1]
                size += int(fl_size)
                if st_code in status_codes:
                    i += 1
                    status_codes[st_code] += 1
                    if i % 10 == 0:
                        statistics_display(size, status_codes)

    except KeyboardInterrupt:
        statistics_display(size, status_codes)
        raise
    else:
        statistics_display(size, status_codes)
