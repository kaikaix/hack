import sys
import os
if os.name != 'nt':
	print "It only can run on windows"
	sys.exit(0)
import zipfile
from unrar import rarfile
from optparse import OptionParser

usage = 'Usage:%prog -d dict -c compressed file -o decompress path'
parser = OptionParser(usage)
parser.add_option('-d',dest = 'dict',help='input the dict path')
parser.add_option('-c',dest = 'compressed',help = 'input the compressed file path')
parser.add_option('-o',dest = 'decompress',help='input the decompressing path')
(options,args) = parser.parse_args()

if options.dict is None:
        parser.print_help()
        sys.exit(0)

dict_p = options.dict
com_p = options.compressed
output_p = options.decompress

try:
        if com_p.endswith(".zip"):
	            zFile=zipfile.ZipFile(com_p)
        elif com_p.endswith(".rar"):
	            zFile=rarfile.RarFile(com_p)
        else:
                print "can't open it."
                sys.exit(0)
except IOError as err:
	    print err
	    sys.exit(0)

try:
	    passFile = open(dict_p,"r")
except IOError as err:
	    print err
	    sys.exit(0)

def crackit():
        for line in passFile.readlines():
                password = line.strip('\n')
                print password
                try:
                        zFile.extractall(path=output_p,pwd=password)
                        print "password is %s" % password
                        zFile.close()
                        sys.exit(0)
                except:
                        continue
crackit()
