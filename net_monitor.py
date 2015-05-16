import netifaces
import time
import os
from itertools import imap
import string

#NETMON_DIR = "/var/log/netmon/"
#MAX_TIME_TO_RUN = 10
#ifc_info = {}
#total_count = 0

# This is the data structure to hold the interface info.
# INTERFACE     :   # OF TIMES UP  
ifc_info = {}

# Variable to hold # of times interface status is verified
total_count = 0

# Run this wizard for 10 minutes
MAX_TIME_TO_RUN = 10

NETMON_DIR = "/var/log/netmon/"


def get_ifc_uptime():
    global total_count

    total_count = total_count + 1

    for ifc in netifaces.interfaces():
        if ifc in ifc_info:
            ifc_info[ifc] = ifc_info[ifc] + 1
        else:
            ifc_info[ifc] = 1


def ifc_statistics():
    global total_count

    get_ifc_uptime()

    max_key = max(imap(len, ifc_info))
    with open("/var/log/netmon/log", "w") as file:
        #line = "INTERFACE \t\t\tUPTIME      \n"
        line =  string.ljust("INTERFACE", max_key+4, " ") + string.ljust("UPTIME", max_key+4, " ") + "\n"
        file.write(line)
        
        for ifc in ifc_info:
            line = string.ljust(ifc, max_key+4, " ") + str( float(ifc_info[ifc]) / total_count) + "\n"
            file.write(line)




def run_monitor():
    global MAX_TIME_TO_RUN
    
    if not os.path.exists(NETMON_DIR):
        os.makedirs(NETMON_DIR)

    while MAX_TIME_TO_RUN != 0:
        ifc_statistics()
        time.sleep(60)
        MAX_TIME_TO_RUN = MAX_TIME_TO_RUN - 1

if __name__ == '__main__':
    #netmon_init()
    print "Monitoring network quality ..."
    run_monitor()
