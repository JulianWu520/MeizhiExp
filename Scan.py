from ScanPluginMiddle import DirBruteScan,NmapScan


def WebScan(target):
    status_list = []
    
    status_list.append(DirBruteScan(target))

    for index,status in enumerate(status_list):
        if status == False:
            scan_status_id = index
            break
        else:
            scan_status_id = "successful"
    return scan_status_id

def PortScan(target):
    string = ""
    if NmapScan(target) != string:
        return "successful"
    else:
        return ""