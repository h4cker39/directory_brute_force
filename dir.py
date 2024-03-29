import requests
import argparse
import sys

def checkFuzz(args):
	fuzz = "FUZZ"
	if fuzz not in args:
		print("You must supply the FUZZ option inside the URL")
		sys.exit()

def list_of_strings(arg):
    return arg.split(',')

ap = argparse.ArgumentParser()
ap.add_argument("-sc","--status_code", required=True,help="Status Code Ignored", type=list_of_strings)
ap.add_argument("-f", "--file", required=True, help="File to for Directory Bruteforce")
ap.add_argument("-c","--color", required=False, help="Color to use")
ap.add_argument("-url", "--url", required=True, help="File to for Directory Bruteforce", type=str)
args = ap.parse_args()
args2 = vars(ap.parse_args())
print(args.status_code)
filename = open(args2['file'], 'r')
print(args.url)

Lines = filename.readlines()
count = 0

for line in Lines:
	count += 1
	checkFuzz(args.url)
	x = requests.get(args.url.replace("FUZZ",line.strip()))
	if str(x.status_code) in args.status_code:
			continue
	print(args.url.replace("FUZZ",line.strip()) + " -- Code : " + str(x.status_code))


	


