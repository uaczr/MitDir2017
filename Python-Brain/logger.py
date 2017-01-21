##@package logger
#@author Christoph Hellmann
#@date 21.01.2017
#@brief Logging functionalities

from colorama import Fore
import time

def debug(mesg):
    print("[" + str(time.time()) + "]" + Fore.BLUE + "DEBUG:\t" + mesg + Fore.RESET)

def warn(mesg):
    print("[" + str(time.time()) + "]" + Fore.YELLOW + "WARN:\t" + mesg  + Fore.RESET)

def error(mesg):
    print("[" + str(time.time()) + "]" + Fore.RED + "ERROR:\t" + mesg + Fore.RESET)