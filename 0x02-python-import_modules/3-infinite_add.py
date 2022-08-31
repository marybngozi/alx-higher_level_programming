#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    sm = 0
    for i in range(1, len(argv)):
        sm += int(argv[i])
    print(sm)
