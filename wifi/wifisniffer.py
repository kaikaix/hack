import os
import sys
from scapy.all import *

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print sys.argv[0] + " <network card>"
    sys.exit(0)

iface = sys.argv[1]

os.system("ifconfig "+iface+" down")
os.system("iwconfig "+iface+" mode monitor")
os.system("ifconfig "+iface+" up")

def dump_packet(pkt):
    if not pkt.haslayer(Dot11Beacon) and \
       not pkt.haslayer(Dot11ProbeReq) and \
       not pkt.haslayer(Dot11ProbeResp):
        print pkt.summary()

        if pkt.haslayer(Raw):
            print hexdump(pkt.load)
        print "\n"

while True:
    for channel in range(1,14):
        os.system("iwconfig "+iface+" channel "+str(channel))
        print "Sniffing on channel "+str(channel)

        sniff(iface=iface,prn=dump_packet,count=10,timeout=3,store=0)
