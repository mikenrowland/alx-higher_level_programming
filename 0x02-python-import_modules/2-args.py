#!/usr/bin/python3
def print_number_of_args(argv):
    args_count = len(argv) - 1
    if args_count == 0:
        print("{:d} argument.".format(args_count))
        return
    else:
        if args_count == 1:
            print("{:d} argument:".format(args_count))
        else:
            print("{:d} arguments:".format(args_count))
        i = 1
        while i <= args_count:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    print_number_of_args(sys.argv)
