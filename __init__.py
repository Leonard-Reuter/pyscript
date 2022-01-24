"""
pyscript
~~~~~~~~

Pyscript is a tiny library for using python as a scripting language in place of bash.

Most functions are imported from standard modules and renamed or adapted for convenience.

:copyright: 2021-2022 Reuter
:license: MIT
"""
from .pyscript import cd, cp, dirs, files, grep, mkdir, isdir, isfile, ls, mv, pwd, rm, run, sed

__all__ = [
    'cd',
    'cp',
    'dirs',
    'files',
    'grep',
    'mkdir',
    'isdir',
    'isfile',
    'ls',
    'mv',
    'pwd',
    'rm',
    'run',
    'sed'
]
