#!/usr/bin/python3
# filename: PythonVariety.py

port = 21
banner = "FreeFloat FTP Server"
print("[+] Checking for" + banner + " on port" + str(port))

port_list = [21, 22, 80, 110]
port_open = True

# string module ：upper(), lower(), replace(), find().
print(banner.upper())
print(banner.lower())
print(banner.replace('FreeFloat', 'Ability'))
print(banner.find('FTP'))

# List module
port_list.append(443)
port_list.append(25)

# List can insert repeating data
port_list.append(21)
port_list.sort()
print(port_list)

# index can return the first offset
position = port_list.index(21)
print(position)

# Dictionary
services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}
print("ftp port is " + str(services['ftp']))
print("ftp port is", services['ftp'])
type(services)
print(services)

