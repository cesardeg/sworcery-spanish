#!/usr/bin/env python3

import struct
import sys
import os

def errmsg(num):
    err = [
        "",
        "Failed to open file.",
        "Error while reading.",
        "Error while writing.",
        "sworcery.dat file is corrupted.",
        "ENDREC was not found. Please check the disk, file, and permissions.",
        "",
        "Failed to recognize archive structure. The archive may be corrupted.",
        "sworcery.dat is not present in the program folder or does not have sufficient permissions.",
        "sworcery.dat.cat is locked by another program or does not have sufficient permissions."
    ]
    print(err[num])


def CENTRECadr(fp):
    fstadr = 0
    for i in range(-4, -100, -1):
        fp.seek(i, 2)  # Seek from the end of the file
        ch = struct.unpack("I", fp.read(4))[0]
        if ch == 0x06054B50:
            fp.seek(12, 1)  # Seek 12 bytes ahead from the current position
            fstadr = struct.unpack("I", fp.read(4))[0]
            break
    return fstadr


def main(folder="."):
    resnum = 0
    resadr = 0
    offset = 0
    pthlng = 5
    aboute = 0

    try:
        fpr = open(os.path.join(folder, "sworcery.dat"), "rb")
    except IOError:
        errmsg(1)
        errmsg(8)
        exit(1)

    cat_file_path = os.path.join(folder, "sworcery.dat.cat")
    if os.path.exists(cat_file_path):
        os.remove(cat_file_path)

    try:
        fpw = open(cat_file_path, "wb")
    except IOError:
        errmsg(1)
        errmsg(9)
        exit(1)

    offset = CENTRECadr(fpr)
    resadr = offset
    stop = True

    while stop:
        respath = "nul"

        fpr.seek(resadr)  # Seek to the resource address
        ch = struct.unpack("I", fpr.read(4))[0]
        if ch == 0x02014B50:
            fpr.seek(resadr + 28)  # Seek to pthlng
            pthlng = struct.unpack("H", fpr.read(2))[0]
            fpr.seek(resadr + 30)  # Seek to aboute
            aboute = struct.unpack("H", fpr.read(2))[0]
            fpr.seek(resadr + 46)  # Seek to the beginning of respath
            respath = fpr.read(pthlng).decode("utf-8")
            respath = respath.lower()

            fpw.write(struct.pack("I", pthlng))
            fpw.write(respath.encode("utf-8"))
            fpw.write(struct.pack("I", resadr))
            fpw.write(struct.pack("I", resnum))

            """
            print(respath)
            print("pthlng: ", pthlng)
            print("aboute: ", aboute)
            print("resnum: ", resnum)
            print("resadr: ", resadr)
            print("header: ", ch)
            """

        else:
            stop = False

        resnum += 1
        resadr += 46 + pthlng + aboute

    fpr.close()
    fpw.close()


if __name__ == "__main__":
    folder_path = sys.argv[1] if len(sys.argv) > 1 else "."
    main(folder_path)
