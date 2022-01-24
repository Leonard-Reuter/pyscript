from contextlib import contextmanager
import subprocess
from os import chdir, mkdir
from os import listdir as ls
from os import getcwd as pwd
from os.path import isdir, isfile
from shutil import copy2 as cp
from shutil import move as mv

# https://stackoverflow.com/a/24176022/11272733
@contextmanager
def cd(newdir):
    """Enters the directory newdir. 

    To be used as:
    with cd('dir'):
        ...
    
    This construct makes sure, that the directory is left after the
    block of the 'with' statement

    If 'dir' does not exist, it is made.
    """
    if not isdir(newdir):
        mkdir(newdir)
    prevdir = pwd()
    chdir(newdir)
    try:
        yield
    finally:
        chdir(prevdir)

def dirs():
    """Returns list of subdirectories in current directory."""
    return [obj for obj in ls() if isdir(obj)]

def files():
    """Returns list of subdirectories in current directory."""
    return [obj for obj in ls() if isfile(obj)]

def grep(filename, string):
    """Returns a list of all lines of a file which include the given
    string pattern."""
    lines = []
    with open(filename, 'r') as grepfile:
        for line in grepfile.readlines():
            if string in line:
                lines.append(line)
    return lines

def rm(string, recursive=False):
    """Calls rm, works with wildcards and arguments like -f."""
    if recursive:
        string = '-r ' + string
    run(f'rm {string}')

def run(line):
    """Executes the given string in the shell."""
    return subprocess.check_call(line, shell=True)

def sed(filename, str1, str2):
    """Calls sed to replace strings in files."""
    run(f'sed -i "s/{str1}/{str2}/g" {filename}')

