import subprocess
import os
import sys
def NmapScan(ip):
    check_nmap_exist = "which nmap"
    check_namp = subprocess.Popen(check_nmap_exist,shell=True,stdout=subprocess.PIPE)
    check_result = check_namp.stdout.read()
    if check_result != '':
        
        #nmap_result = subprocess.Popen(nmap_cmd,shell=True,stdout=subprocess.PIPE)
        #os.system()
        if not os.path.exists('../../../DB/Scan/' + ip):
            os.makedirs('../../../DB/Scan/' + ip)
        file_path = "../../../DB/Scan/%s/port.txt" % ip
        nmap_cmd = "nmap %s > %s" % (ip,file_path)
        os.system(nmap_cmd)
        
        scan_result = open(file_path,"r").readlines()


        file_handle = open(file_path,"w")
        for line in scan_result:
            if "open" in line:
                file_handle.write(line)
        
if __name__ == '__main__':
    ip = sys.argv[1]
    NmapScan(ip)