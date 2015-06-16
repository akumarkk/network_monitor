import argparse
import sys

parser = argparse.ArgumentParser(
    prog="l2ald-stats",
    description='Test Utility to install/delete Bridge domains and mac-routes')

# Optional arguments with argument list to them
parser.add_argument("-n", "--bridge-domain", type=int,   dest="n_bd",     default=10,  metavar="NUMBER",  help = "Number of Bridge Domains")
parser.add_argument("-m", "--umac-routes",   type=int,   dest="n_mac",    default=100, metavar="NUMBER",  help = "Number of Unicast mac-routes")
parser.add_argument("-f", "--log-file",      type=argparse.FileType('w'), default=sys.stdout, metavar="FILE", help = "Log file name")

# To create optional argument (like --bd-add), where it just signifies ADD/DEL 
#   action = "store_true/false"
#   It does not take 
#         - type & metavar
parser.add_argument("--bd-add",              dest="is_bd_add",    action="store_true",  help = "Add/Delete Bridge Domains")
parser.add_argument("--umac-add",            dest="is_umac_add",  action="store_true",  help="Add/Delete Unicast mac-routes")                     


#Required argument (Without any "-" or "--")
# These positional arguments do not take "dest" attribute in add_argument
parser.add_argument("ip-addr",     type=str,   metavar="x.x.x.x",      help = "IP address of QFX Gateway")
parser.add_argument("ovsdbd-port", type=int,   metavar="OVSDBD-PORT",  help = "Port number of ovsdbd")

par = parser.parse_args()

print par.n_bd
print "BD Add value = ", par.is_bd_add
print par.is_umac_add
