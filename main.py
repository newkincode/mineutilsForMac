import tkinter
import minecraft_launcher_lib
import subprocess
import sys
import pprint

windows = tkinter.Tk()



windows.mainloop()

pprint.pprint(minecraft_launcher_lib.utils.get_version_list()[0])