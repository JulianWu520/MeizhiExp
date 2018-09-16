from Scan import WebScan,PortScan
from Exp import WebExp,PortExp
from Display import function_option,function_auto,show_bar,history,show_exp,show_task
import multiprocessing
from TaskController import taskController
from Color import *
import time

def Scan(target):
    if WebScan(target) != "successful":
        print red("    [!] Error happened on web scan!")
    else:
        print green("\n    [*] %s Web Scan Finished" % target)
    if PortScan(target) != "successful":
        print red("    [!] Error happened on port scan!")
    else:
        print green("\n    [*] %s Port Scan Finished" % target)
def search_feature(log_file,feature_file,index):
    feature_list = open(feature_file,"r")
    find_feature = ''
    scan_list = open(log_file).readlines()
    for feature in feature_list.readlines():
        feature = feature.rstrip('\n')
        func = feature.split(" ")
        for log_result in scan_list:
            if func[index] in log_result:
                find_feature = func[index+1]
                break
    return find_feature


def Exploit(ip):
    
    web_scan_path_log = "DB/Scan/%s/web.txt" % ip
    web_feature = "web_feature.txt"
    
    port_scan_path_log = "DB/Scan/%s/port.txt" % ip
    port_feature = "port_feature.txt"
    

    time.sleep(5)
    find_web_feature = search_feature(web_scan_path_log,web_feature,0)
    find_port_feature = search_feature(port_scan_path_log,port_feature,1)
        
    if find_web_feature != '':
        WebExp(ip,find_web_feature)
    if find_port_feature != '':
        PortExp(ip,find_port_feature)

def AutoExp(ip):
    Scan(ip)
    Exploit(ip)

def CustomExp(target_msg):
    ip,exp_name,exp_type = target_msg
    if ip != '':
        if exp_type == "web":
            WebExp(ip,exp_name)
        if exp_type == "port":
            PortExp(ip,exp_name)
    

def mainController():
    task_list = []
    scan_task_list = []
    exp_task_list = []
    show_bar()
    while True:
        
        option = function_option()
        if option == "A":
            target = function_auto()
            if target != '':
                p = multiprocessing.Process(target=AutoExp,args=(target,))
                p.start()
                task_list.append([target,p])
        
        elif option == "B":
            ip = function_auto()
            scan_process = multiprocessing.Process(target=Scan,args=(ip,))
            scan_process.start()
            scan_task_list.append([ip,scan_process])
        
        elif option == "C":
            ip,exp_name,exp_type = show_exp()
            target_msg = (ip,exp_name,exp_type)
            exp_process = multiprocessing.Process(target=CustomExp,args=(target_msg,))
            exp_process.start()
            exp_task_list.append([ip,exp_process])
        
        elif option == "D":
            show_task(task_list,scan_task_list,exp_task_list)
        elif option == "E":
            history()
        
        elif option == "F":
            exit(0)
        
        else:
            pass
        #Scan(target)
        





