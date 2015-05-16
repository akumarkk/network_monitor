import netifaces

# This is the data structure to hold the interface info.
# INTERFACE     :   # OF TIMES UP  
ifc_info = {}

# Variable to hold # of times interface status is verified
total_count = 0

def get_ifc_uptime():
    total_count = total_count + 1

    for ifc in netifaces.interfaces():
        if ifc in ifc_info:
            ifc_info[ifc] = ifc_info[ifc] + 1
        else:
            ifc_info[ifc] = 1


