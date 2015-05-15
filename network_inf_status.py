#Install netifaces before running this program if you do not have
#netiface module
#
# 1. Download module from https://pypi.python.org/pypi/netifaces
# 2. tar xvzf netifaces-0.10.4.tar.gz
# 3. cd netifaces-0.10.4
# 4. python setup.py install
# 5. export PYTHON_EGG_CACHE=/home/ubuntu/Downloads/netifaces-0.10.4 

# export the above env variable in ~/.bashrc 

import netifaces

def get_active_interfaces(active_ifc):
    for ifc in netifaces.interfaces():
        active_ifc.append(ifc)

    return active_ifc

active_ifc = []
get_active_interfaces(active_ifc)

print "Active Interfaces : "
for ifc in active_ifc:
    print ifc

