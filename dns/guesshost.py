import sys
import socket

if len(sys.argv) !=3:
    print sys.argv[0]+" <dict_file> <domain>"
    sys.exit(0)

able_map={}

def do_dns_lookup(name):
    try:
        try:
            ip = socket.gethostbyname(name)
            print name+": "+ip
            able_map[name] =ip 
        except socket.gaierror,e:
            print name+": "+str(e)
    except KeyboardInterrupt:
        print able_map.keys()
        while True:
            pycmd=raw_input("find>>")
            try:
                print able_map[pycmd]
            except KeyError:
                print "It is an error key"
        sys.exit(0)
try:
    fh = open(sys.argv[1],"r")

    for word in fh.readlines():
        do_dns_lookup(word.strip()+"."+sys.argv[2])
    
    fh.close()
except IOError:
    print "Can't read dictionary "+sys.argv[1]