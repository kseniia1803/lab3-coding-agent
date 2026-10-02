'''
This program prints stdin to the screen.
'''
import sys

# Use a larger buffer for I/O efficiency, but fixed memory usage
CHUNK_SIZE = 64 * 1024  # 64 KB

def cat(file):
    while True:
        data = file.read(CHUNK_SIZE)
        if not data:
            break
        sys.stdout.buffer.write(data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
