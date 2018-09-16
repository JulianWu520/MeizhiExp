import os
from TaskController import taskController
from termcolor import colored
from Color import red,yellow,cyan,green

def show_bar():
    show_pic = \
    """
     __  __      _     _     _ _____            
    |  \/  | ___(_)___| |__ (_) ____|_  ___ __  
    | |\/| |/ _ \ |_  / '_ \| |  _| \ \/ / '_ \ 
    | |  | |  __/ |/ /| | | | | |___ >  <| |_) |
    |_|  |_|\___|_/___|_| |_|_|_____/_/\_\ .__/ 
                                        |_|    
    """
    print red(show_pic)



def function_option():
    function_display =  \
    """
    [A] AutoScan and AutoExploit
    [B] Scan
    [C] Exploit
    [D] Check the Task
    [E] Show History
    [F] Exit
    """
    print yellow(function_display)
    option = raw_input(cyan('    [+] Type "A"-"F" to select option: '))
    return option

def function_auto():
    target = raw_input(cyan("    [+] Set Your target: "))
    return target



def show_process(process_list):
    for index,process in enumerate(process_list):
        if "stop" not in str(process[1]):
            msg = "    [*] [%s]process(%s) is running" % (str(index),process[0])
            print green(msg)
        else:
            msg = "    [*] [%s]process(%s) is finshed" % (str(index),process[0])
            print green(msg)
        
def task_detail():
    option_detail = \
    """
    [*] Type "A"-"B" to select the option.
    [A] Process Detail.
    [B] Exit\
    """
    print yellow(option_detail)

    option = raw_input(cyan("    [*] Optional Select:"))
    if option == 'A':
        process_id = raw_input(cyan("    [*] Set Process ID:"))
        return process_id
    else:
        return ''

def show_task(auto_task,scan_task,exp_task):
    string = \
    """
    [A] Auto Exploit Task    
    [B] Scan Task
    [C] Exploit Task
    """
    print yellow(string)
    option_type = raw_input(cyan("    [*] Select the type:"))
    if option_type == "A":
        taskController(auto_task)
    elif option_type == "C":
        taskController(exp_task)
    elif option_type == "B":
        show_process(scan_task)
    else:
        pass
        
        




def history():
    file_list = os.listdir("DB/Shell/")
    for index,file_name in enumerate(file_list):
        file_name = file_name.replace(".txt","")
        msg = "    [*] [%s] %s" % (str(index),file_name)
        print green(msg)
    history_id = raw_input(cyan("    [+] Check the hisory id:"))
    if history_id != '':
        file_name = file_list[int(history_id)]
        file_name = "DB/Shell/%s" % file_name
        shell = open(file_name,"r").read()
        msg = "    [*] %s" % shell
        print green(msg)

def show_exp():
    web_feature = open("web_feature.txt","r")
    port_feature = open("port_feature.txt","r")

    web_exp = []
    port_exp = []

    web_exp_name = []
    port_exp_name = []

    for web in web_feature.readlines():
        web = web.split(' ')
        web_exp.append(web[0] + " => " + web[1])
        web_exp_name.append(web[1])
    
    for port in port_feature.readlines():
        port = port.split(' ')
        port_exp.append(port[1] + " => " + port[2])
        port_exp_name.append(port[2])
    print green("\n    [*] Web Exp")
    for index,exp in enumerate(web_exp):
        msg = "    [%s] %s" % (str(index),exp.replace('\n',''))
        print green(msg)
    #num = index
    print yellow("\n    [*] Port Exp")
    for index,exp in enumerate(port_exp):
        msg = "    [%s] %s" % (str(index),exp.replace('\n',''))
        print green(msg)
    
    exp_type = raw_input(cyan("    [+] Select Exploit Type (type 'web' or 'port'):"))
    if exp_type == "web":
        web_num = raw_input(cyan("    [*] Select Exploit Numer:"))
        exp_name = web_exp_name[int(web_num)]
    elif exp_type == "port":
        port_num = raw_input(cyan("    [*] Select Exploit Numer:"))
        exp_name = port_exp_name[int(port_num)]
    else:
        exp_name = ''
    
    if exp_name != '':
        ip = raw_input(cyan("    [+] Set you target:"))
        return ip,exp_name,exp_type
    else:
        return "","",""
        
    

    