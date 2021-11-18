import sys
import socket


try: 
	#takes file as input
	filename = sys.argv[1]
	
	#Reads the entire file
	with open(filename, 'r') as ipfile:
		ip_addresses = ipfile.read()
		ipfile.close()
	
	#Splits ip_address string to a list
	ip_list = ip_addresses.splitlines()
	
	#Iterates through list, converts values to binary format
	binary_list = []
	for ip in ip_list:
		bin_value = socket.inet_aton(ip)
		binary_list.append(bin_value)

	#Sorts binary values
	binary_list.sort()
	
	#Iterates through list, converts values from binary to string IPv4. 
	sorted_list = []
	for binary in binary_list:
		ipaddr = socket.inet_ntoa(binary)
		sorted_list.append(ipaddr)
	
	#Iterates through list and print output. 
	for ipaddr in sorted_list:
		print(ipaddr)
except: 
	print('Please input file name when starting script, example: python3 ip-sort.py FILENAME.txt')
