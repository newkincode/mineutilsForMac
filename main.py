import tkinter
import minecraft_launcher_lib
from pmlauncher import pml, mlogin, mlaunchoption
from pycraft import authentication
import subprocess
import sys
import os
import pprint

p = os.getcwd() + "/game"
pml.initialize(p)


session = mlogin.session()
session.username = "tester123"
session.uuid = "uuid"
session.access_token = "access_token"

windows = tkinter.Tk()



windows.mainloop()

pprint.pprint(minecraft_launcher_lib.utils.get_version_list()[0])