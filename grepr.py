# Program to recursively grep - i.e. run given grep command on current directory and all subdirectories.
# Grep command read in from grep.txt.
# Works as is, but works best if put -s and -H on command line, to not show "no matching files" errors,
# and to always include the filename with each match - rather inexplicably filenames are missing sometimes
# if don't add -H.
# TODO: suppress directory names where no matches were found.

import os

def grep_dir(base_dir):
    # Get list of all subdirectories, including current.
    dirnames = [name for name in os.listdir()
                if os.path.isdir(os.path.join(base_dir, name))]

    # For each, run the grep command.
    start_dir = os.getcwd()
    for dirname in dirnames:
        print('\n' + os.path.join(start_dir, dirname))
        os.chdir(os.path.join(start_dir, dirname))
        os.system(grep_cmd)
        grep_dir(os.path.join(start_dir, dirname))


# __main__
# Read in grep command
grep_file = "grep.txt"
if os.path.exists(grep_file):
    with open(grep_file, 'rt') as f:
        grep_cmd = f.read()
    print("cmd: " + grep_cmd)

    # Start with the initial directory.
    start_dir = os.getcwd()
    print(start_dir)
    os.system(grep_cmd)
    grep_dir(start_dir)

else:
    print( "This program requires the desired grep command be in the file " + grep_file)

