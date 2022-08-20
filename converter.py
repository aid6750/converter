#!/usr/bin/python3
import glob
import argparse
import os
try :
	from PIL import Image
except:
	os.system("pip3 install Pillow")
	from PIL import Image

def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("files",nargs='+')
	parser.add_argument("-type",default='png')
	parser.add_argument("-rm",default=False)
	return parser

def convert(file,args):
	im = Image.open(file)
	rgb_im = im.convert('RGB')
	rgb_im.save(file.replace(file.split(".")[1], args.type), quality=95)
	if (args.rm):
		os.remove(file)

if __name__ == '__main__':
	parser = create_parser()
	args = parser.parse_args()
	for file in args.files:
		if '*' in file:
			for file in glob.glob(file):
				convert(file,args)
		else:
			convert(file,args)

