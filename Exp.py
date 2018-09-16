#from ExpPluginMiddle import PMAExp
import ExpPluginMiddle


def WebExp(target,feature):
    
    exploit_func = getattr(ExpPluginMiddle,feature)


    return exploit_func(target)


def PortExp(ip,feature):
    pass