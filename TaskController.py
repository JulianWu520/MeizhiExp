from Color import *
def taskController(process_list):
    for index,process in enumerate(process_list):
        if "stop" not in str(process[1]):
            print green("    [*] [%s]process(%s) is running" % (str(index),process[0]))
        else:
            print green("    [*] [%s]process(%s) is finshed" % (str(index),process[0]))
    
    process_id = exp_task_detail()
    if process_id != '':
        try:
            process_name = process_list[int(process_id)][0]
            shell_list = open("DB/Shell/" + process_name + ".txt","r")
            for shell in shell_list.readlines():
                if process_name in shell:
                    print green("    [*] WebShell:%s" % shell)
        except:
            pass
    else:
        pass

def exp_task_detail():
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