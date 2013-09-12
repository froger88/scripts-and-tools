#!/usr/bin/python2.7
import sys
import json

def print_help():
    print """
./rewriter.py --help: show this screen and exit
./rewriter.py: run and waits untill eof
./rewriter.py --json-header: like above, but read and do not save into result file, the first line

EXAMPLE USAGE:
Usage (1): cat file_in | rewriter.py 
Usage (2): cat file_in | rewriter.py --json-header
Usage (3): cat file_in | docker run DOCKER_ID -i /usr/bin/executioner | rewriter.py --json-header
Usage (4): cat file_in | rewriter.py --out dir/file.out

We can use (1), when we want to cat binary file into other file using stdout
We can use (2), when we want to add additional json header (one line, ending with \\n)
\tThis line will be ignored and not write into file, but we can pass few variables like:
\tfilename - out file name, dir - output directory
\tUsage (3) is just example of throwing file_in into docker, and getting binary result with rewriter
\t(result contain header line)    
\tUsage (4) is example of save to seleted dir/filename given by parameter

Supported json options: 
-> filename: output filename
"""

def read_options():
    options = sys.stdin.readline()
    options = json.loads(options)
    return options

def read_file(filename):
    f = open(filename, "wb")
    try:
        while True:
            x = sys.stdin.read()
            if not x:
                    return
            f.write(x)
    except:
        exit(-1)

    f.close()

def main():
    try:
        options = read_options()
    except Exception, e:
        print e
        exit(-1)

    try:
        filename = read_file(options)
    except Exception, e:
        print e
        exit(-1)


def main(argv):

    if len(argv) > 1:
        if argv[1] == "--json-header" or argv[1] == '-j':
            try:
                filename = read_options()['filename']
            except Exception, e:
                filename = "file.out"

        elif argv[1] == "--help" or argv[1] == '-h':
            print_help()

        else:
            filename = argv[1]

        read_file(filename)

if __name__ == '__main__':
    main(sys.argv)
