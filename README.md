**pyscript - a tiny package for using python as a scripting language in place of bash**

Some functions only work on Unix-like systems. Best to use with `from pyscript import *`

functions:

* `with cd('dir'):` moves into directory 'dir' and leaves back to the current directory after the with block
* `cp('a', 'b')` copies 'a' to 'b'
* `dirs()` returns a list of directories in the current directory
* `files()` returns a list of files in the current directory
* `grep('text', 'f')` returns a list of all lines in 'f', which include 'text'
* `mkdir('dir')` creates the directory 'dir'
* `isdir('dir')` returns a boolean, checks, whether 'dir' is a directory
* `isfile('f')` returns a boolean, checks, whether 'f' is a file
* `ls()` returns a list of files and directories in the current directory
* `mv('a', 'b')` moves 'a' to 'b'
* `pwd()` returns the current path
* `rm('file')` removes 'file', or directories with `rm('-r dir')`
* `run('input')` runs the given input in the current shell
* `sed('f', 'text1', 'text2')` replaces 'text1' with 'text2' in file 'f' globally
 
