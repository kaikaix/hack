import sys
from pythonwifi.iwlibs import Wireless

frequency_channel = {
    2412000000:"1",
    2417000000:"2",
    2422000000:"3",
    2427000000:"4",
    2432000000:"5",
    2437000000:"6",
    2442000000:"7",
    2447000000:"8",
    2452000000:"9",
    2457000000:"10",
    2462000000:"11",
    2467000000:"13",
    2472000000:"14"
} 

if len(sys.argv) < 2:
    print sys.argv[0] + " <network card>" 
    sys.exit(0)

network_c=sys.argv[1]
wifi = Wireless(network_c)

for ap in wifi.scan():
    try:
        print "ESSID:" + ap.essid
        print "BSSID:" + ap.bssid
        print "channel:" + frequency_channel.get(ap.frequency.getFrequency())
        print ""
    except TypeError:
        print ""
        continue
