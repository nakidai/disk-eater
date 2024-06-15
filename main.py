#!/usr/bin/env python

"""
This code creates a file that takes up all the disk space

Be careful as some filesystems will break if no free space available

Most likely code will not work as planned if runned on FAT32 or simillar because
of limitation in max file size

Code created for educational purposes only and licensed under the GPLv3 license
(check LICENSE file or https://www.gnu.org/licenses/gpl-3.0.txt for details)

Author: Nakidai <plaza521 at inbox dot ru>
"""

from sys import argv


# Amount of bytes that script will write on the disk per one iteration if no
# argument specified, default is 1KiB
BYTES_PER_WRITE: int = 1024


def main() -> None:
    if len(argv) < 2:
        print(f"usage: {argv[0]} <filename> [BYTES_PER_WRITE]")
        exit(1)
    bpw: int = int(argv[2]) if len(argv) > 2 and argv[2].isnumeric() else BYTES_PER_WRITE
    with open(argv[1], "w") as f:
        try:
            while True:
                f.write('\0' * bpw)
                f.flush()
        except Exception as exc:
            print(f"Stopped because of {exc}")
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
