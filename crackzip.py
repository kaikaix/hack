import zipfile
import sys

while True:
		path = raw_input("input the compressed file path:")

		try:
				zFile=zipfile.ZipFile(path)
				break
		except IOError as err:
				print err
				continue

while True:
		path = raw_input("input the dict path:")
		try:
				passFile = open(path,"r")
				break
		except IOError as err:
				print err
				continue

path = raw_input("input the decompressing path:")
save_path = path
				

for line in passFile.readlines():
		password = line.strip('\n')
		try:
				zFile.extractall(path=save_path,pwd=password)
				print "password is %s" % password
				sys.exit(0)
		except RuntimeError:
				pass


