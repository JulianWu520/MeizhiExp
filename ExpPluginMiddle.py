import os
import subprocess
def PMAExp(target):
    target = "http://" + target
    os.chdir("Plugin/Exp/phpmyadminExp/")
    scan_plugin = "python phpmyadminExp.py %s" % target
    # PMAExp_thread = subprocess.Popen(scan_plugin, bufsize=0, executable=None, stdin=None, stdout=subprocess.PIPE, stderr=None,\
    #     preexec_fn=None, close_fds=False, shell=True, cwd=None, env=None, universal_newlines=False,\
    #     startupinfo=None, creationflags=0)
    os.system(scan_plugin)
    os.chdir("../../../")

