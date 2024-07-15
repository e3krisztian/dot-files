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

def _slash_command(f):
    class SlashCommand:
        def __truediv__(self, data):
            return f(data)
        def __repr__(self):
            return f.__doc__
    SlashCommand.__name__ = f.__name__
    SlashCommand.__doc__ = f.__doc__
    return SlashCommand()


@_slash_command
def p(path):
    """p/"path" = Path("path")"""
    return Path(str(path))


@_slash_command
def l(iterable):
    """l/iterable = list(iterable)"""
    return list(iterable)


@_slash_command
def h(object):
    """h/object = help(object)"""
    help(object)


@_slash_command
def x(object):
    """x/object = pprint(object)"""
    width = int(os.environ.get("COLUMNS", 80))
    pprint(object, width=width, compact=True)


@_slash_command
def xl(iterable):
    """xl/iterable = pprint(list(iterable))"""
    pprint(list(iterable))


@_slash_command
def X(object):
    """X/object = print(object)"""
    print(object)


@_slash_command
def h(object):
    """h/object = help(object)"""
    help(object)


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
    _WARN = ""
    _RESET = ""


_SAD_FACE = f"{_WARN}\N{Slightly Frowning Face}{_RESET}"


@_slash_command
def s(object):
    """s/object = print the Python source for object"""
    try:
        source = inspect.getsource(object)
    except Exception:
        print(f"Haiya {_SAD_FACE}! Could not get source of {_EMPH}{object}{_RESET} for you - so sad!")
        return

    # print(_highlight(source))
    run(["/usr/bin/less", "-RF"], input=_highlight(source).encode())


# WIP: interactive console with goodies after loading a module
# # PYTHONINSPECT & PYTHONSTARTUP does not work together :(
# import code
# filename="demo.py"
# __file__ = filename
# c = code.InteractiveConsole(locals=locals(), filename=filename)
# c.runsource(Path(filename).read_text(), filename=filename, symbol="exec")
# c.interact()
