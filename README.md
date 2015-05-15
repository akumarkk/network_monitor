# network_monitor

Network monitoring and diagnostic tool :
 A tool that will continuously monitor the connectivity status and connection quality of each network. Log all information to /var/log/netmon/log. In addition, all active network issues (outages, severe performance degradation) are kept current at /var/log/netmon/issues.
 
 Quality of the network interface/connection can be best measured by:
  1. Uptime - The amount of time interface is up 
  2. Network Transmission rate - Number of bytes transmitted and received per unit time
  
A network with higher uptime and transmission rate is consider to be better than that with lower uptime and transmission rate.
