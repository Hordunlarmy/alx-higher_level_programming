#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv
add = 0

if (len(argv) == 1):
    print("0")
elif (len(argv) > 1):
    for i in range(1, len(argv)):
        add += int(argv[i])
    print(add)
