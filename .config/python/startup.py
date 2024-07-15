import enum
import inspect
import itertools
import json
import math
import os
import re
import stat
import statistics
import subprocess
import sys

from pathlib import Path
from pprint import pprint, pp
from subprocess import run

import rlcompleter
import readline
# readline.parse_and_bind("tab: complete")
readline.read_init_file()

# FIXME: readline history file
# SEE: https://docs.python.org/3/library/readline.html
# if Path(".python_history").exists():
#     readline.read_history_file(".python_history")
# else:
#     readline.write_history_file(".python_history")

class _PathString:
    def __truediv__(self, other):
        return Path(str(other))

P = p = _PathString()
del _PathString


class _PPrint:
    def __truediv__(self, other):
        pprint(other)

x = _PPrint()
del _PPrint


class _Print:
    def __truediv__(self, other):
        print(other)

X = _Print()
del _Print


class _Help:
    def __truediv__(self, other):
        help(other)

h = _Help()
del _Help


def _highlight(code):
    try:
        import pygments
        import pygments.lexers
        import pygments.formatters
    except ImportError:
        return code

    lexer = pygments.lexers.get_lexer_by_name("Python")
    formatter = pygments.formatters.get_formatter_by_name("console")
    return pygments.highlight(code, lexer, formatter)


try:
    import colorama
    _EMPH = colorama.Style.BRIGHT
    _WARN = colorama.Fore.YELLOW + colorama.Style.BRIGHT
    _RESET= colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL
except ImportError:
    _EMPH = ""
    _RED = ""
    _RESET = ""

class _Source:
    def __truediv__(self, other):
        try:
            source = inspect.getsource(other)
        except Exception:
            print(f"Haiya {_WARN}\N{Slightly Frowning Face}{_RESET}! Could not get source for {_EMPH}{other}{_RESET} for you - so sad!")
            return

        # print(_highlight(source))
        run(["/usr/bin/less", "-RF"], input=_highlight(source).encode())

s = _Source()
del _Source

# PYTHONINSPECT & PYTHONSTARTUP:
# https://gist.github.com/gwparikh/797559acf7d0164cfd32


import code
filename="demo.py"
__file__ = filename
c = code.InteractiveConsole(locals=locals(), filename=filename)
c.runsource(Path(filename).read_text(), filename=filename, symbol="exec")
c.interact()
