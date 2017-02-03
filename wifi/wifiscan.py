from scapy.all import *

wifi = {}

def scan(packet):
    dot = packet.getlayer(Dot11)

    if dot != None:
        elt = dot.getlayer(Dot11Elt)

        if elt != None:
            
            if dot.type == 0 and dot.subtype == 8:
		     bssid = dot.addr3.upper()
		     essid = elt.info
		     if not wifi.has_key(bssid):
		         wifi[bssid]=essid
		         if essid == "":
		             essid = "Hidden"
		         print essid+": "+bssid

sniff(prn=scan)
