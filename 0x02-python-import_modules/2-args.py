#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    slen = len(argv) - 1
    print("{} argument{}{}"
          .format(slen, '' if slen == 1 else 's', ':' if slen >= 1 else '.'))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
