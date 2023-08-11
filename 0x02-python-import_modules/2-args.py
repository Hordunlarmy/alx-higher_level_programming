#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv
if (len(argv) == 1):
    print(f"{len(argv) - 1} arguments.")
elif (len(argv) > 1):
    if (len(argv) == 2):
        print(f"{len(argv) - 1} argument:")
        print(f"{len(argv) - 1}: {argv[1]}")
    else:
        print(f"{len(argv) - 1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
