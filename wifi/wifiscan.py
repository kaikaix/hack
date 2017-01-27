from scapy.all import *

wifi = {}

def scan(packet):
    elt = packet.getlayer(Dot11Elt)
    dot = packet.getlayer(Dot11)

    if elt != None and dot != None:
        bssid = dot.addr1
        essid = elt.info
        if not wifi.has_key(bssid):
            wifi[bssid]=essid
            if essid == "":
                essid = "Hidden"
            print essid+": "+bssid

sniff(prn=scan)        