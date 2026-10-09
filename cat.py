#!/usr/bin/env python3
"""
Stream stdin or files to stdout in constant memory.
"""
import sys

CHUNK_SIZE = 64 * 1024


def cat(file, out):
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        out.write(chunk)

if __name__ == "__main__":
    out = sys.stdout.buffer
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f, out)
    else:
        cat(sys.stdin.buffer, out)
