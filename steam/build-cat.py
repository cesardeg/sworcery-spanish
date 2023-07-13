#!/usr/bin/env python3
import struct
import sys
import os

# Constants for magic numbers, offsets, and byte sizes
ENDREC_SIGNATURE = 0x06054B50
HEADER_SIGNATURE = 0x02014B50
HEADER_PTHLNG_OFFSET = 28
HEADER_ABOUTE_OFFSET = 30
HEADER_RESADR_OFFSET = 46
BYTES_INT_OFFSET = 12  # Offset for skipping bytes when seeking with BYTES_INT
FILE_SEARCH_LIMIT = 100
BYTES_INT = 4
BYTES_SHORT = 2

def main(res_dir="."):
    resnum = 0
    resadr = 0
    pthlng = 0
    aboute = 0

    try:
        dat_file_path = os.path.join(res_dir, "sworcery.dat")
        cat_file_path = os.path.join(res_dir, "sworcery.dat.cat")

        with open(dat_file_path, "rb") as fpr, open(cat_file_path, "wb") as fpw:
            offset = find_central_header(fpr)
            resadr = offset
            while True:
                respath = ""

                fpr.seek(resadr)  # Seek to the resource address
                ch = struct.unpack("I", fpr.read(BYTES_INT))[0]
                if ch == HEADER_SIGNATURE:
                    fpr.seek(resadr + HEADER_PTHLNG_OFFSET, 0)  # Seek to read pthlng
                    pthlng = struct.unpack("H", fpr.read(BYTES_SHORT))[0]
                    fpr.seek(resadr + HEADER_ABOUTE_OFFSET, 0)  # Seek to read aboute
                    aboute = struct.unpack("H", fpr.read(BYTES_SHORT))[0]
                    fpr.seek(resadr + HEADER_RESADR_OFFSET, 0)  # Seek to the beginning of respath
                    respath = fpr.read(pthlng).decode("utf-8").lower()

                    fpw.write(struct.pack("I", pthlng))
                    fpw.write(respath.encode("utf-8"))
                    fpw.write(struct.pack("I", resadr))
                    fpw.write(struct.pack("I", resnum))
                else:
                    break

                resnum += 1
                resadr += HEADER_RESADR_OFFSET + pthlng + aboute

    except IOError as e:
        print(f"Error: Failed to open or read the file. {e}")
        sys.exit(1)
    except struct.error:
        print("Error: The sworcery.dat file is corrupt or has an invalid format.")
        sys.exit(1)

def find_central_header(fp):
    found = False
    fstadr = 0
    file_size = fp.seek(0, 2)  # Get the size of the file

    for i in range(file_size - BYTES_INT, file_size - FILE_SEARCH_LIMIT, -1):
        fp.seek(i)  # Seek from the end of the file
        ch = struct.unpack("I", fp.read(BYTES_INT))[0]
        if ch == ENDREC_SIGNATURE:
            fp.seek(BYTES_INT_OFFSET, 1)  # Seek BYTES_INT_OFFSET bytes ahead from the current position
            fstadr = struct.unpack("I", fp.read(BYTES_INT))[0]
            found = True
            break

    if not found:
        print("Error: ENDREC_SIGNATURE not found in the file.")
        sys.exit(1)

    return fstadr


if __name__ == "__main__":
    res_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    main(res_dir)
