# -*- coding: utf-8 -*-

"""

███████╗ ██████╗ ██╗     ██████╗ ██╗███████╗██████╗
██╔════╝██╔═══██╗██║     ██╔══██╗██║██╔════╝██╔══██╗
███████╗██║   ██║██║     ██║  ██║██║█████╗  ██████╔╝
╚════██║██║   ██║██║     ██║  ██║██║██╔══╝  ██╔══██╗
███████║╚██████╔╝███████╗██████╔╝██║███████╗██║  ██║
╚══════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝


Soldier is an Apache2 licensed library designed for executing system
processes with ease. It is written on top of subprocess and has a much
user-friendly and pythonic interface.

"""

__title__ = 'soldier'
__version__ = '0.1'
__author__ = 'Yash Mehrotra'
__license__ = 'Apache 2.0'

from .soldier import run
from .exceptions import (
    InvalidCommandError,
    ProcessDoesNotExistError,
    ProcessTimeoutError
)

__all__ = ['run', 'InvalidCommandError',
           'ProcessDoesNotExistError', 'ProcessTimeoutError']
