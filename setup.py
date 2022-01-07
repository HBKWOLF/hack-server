import sys
from cx_Freeze import setup,Executable
#ahmed.s.mohammed 
include_files = ['autorun.inf']
base = None
#ahmed.s.mohammed 
if sys.platform=='win32':
    base = 'win32GUI'
setup(name="connector",version = "1.0",description = "It connects to main server script",
options ={'build_exe':{'include_files':include_files}},executables = [Executable("client.py",base = base)])