import subprocess
import os
import re


# def bannerscan(target):
#     scan_plugin_path = "Plugin/Scan/"
#     plugin_name = "bannerscan/"
#     exec_file = scan_plugin_path + plugin_name + 'bannerscan.py'
#     cmd = "python %s -i %s -s %s" % (exec_file,target,"save.txt")
#     getcmd = subprocess.Popen(cmd, bufsize=0, executable=None, stdin=None, stdout=subprocess.PIPE, stderr=None,\
#     preexec_fn=None, close_fds=False, shell=True, cwd=None, env=None, universal_newlines=False,\
#     startupinfo=None, creationflags=0)
#     while True:
#         print getcmd.stdout.readline()


# bannerscan('http://192.168.10.173')


def DirBruteScan(ip):
    
    try:
        os.chdir('Plugin/Scan/DirBrute/')
        path = '../../../DB/Scan/%s' % ip
        if not os.path.exists(path):
            os.makedirs(path)
        scan_plugin = "python dirbrute.py %s -e php -t 1 > %s/web.txt" % (ip,path)
        os.system(scan_plugin)

        scan_log_txt = "../../../DB/Scan/" + ip + '/web.txt'
        scan_log = open(scan_log_txt,"r").read()

        scan_result = re.findall("http://[a-zA-Z0-9\.]+/(.*) ",scan_log)
        

        handle = open(scan_log_txt,"w")
        for line in scan_result:
            handle.write(line+'\n')
        handle.close()
        os.chdir('../../../')
        
        return True
    except:
        return False
def NmapScan(ip):
    path = "Plugin/Scan/NmapScan/"
    os.chdir(path)
    scan_plugin = "python NmapScan.py %s" % ip
    os.system(scan_plugin)
    os.chdir('../../../')
    return "successful"


#DirBruteScan("192.168.10.173")