# Project Title

Simple Python(3) script to recursively run a given grep command in the current directory and all sub-directories. Grep command is read in from grep.txt in current directory. Recommend putting -s and -H in command line, to not show "no matching files" errors (-s) and to always include the filename with each match (-H) - in testing found that if don't include -H, sometimes the filenames don't display.
Appears to work under Linux and Windows. (Tested under Ubuntu 18.04 and Windows 7.)

## Getting Started

Copy script to convenient location on your system, go to directory that you want to search underneath, put desired grep command line in grep.txt in that directory, then use python to run the script.
eg:
python3 grepr.py

### Prerequisites

Python (tested with 3.6.)
Command line version of grep. I've tested GNU grep 3.1 under Ubuntu, grep 1.0 for NT 32-bit under Windows.



## Authors

* **Greg Walker** - *Initial work* - (https://github.com/gregw18)


## License

MIT


