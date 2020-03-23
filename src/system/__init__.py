'''For more usable import from that's packet.'''
from sys import platform
from .system import ISystem
from .winSystem import WinSystem
from .linSystem import LinSystem


if platform == "linux" or platform == "linux2":
    system = LinSystem()
elif platform == "win32":
    system = WinSystem()
else:
    raise ImportError()
