import telnetlib

#connect device using telnet
tn = telnetlib.Telnet("192.168.56.112")

#login into router 
tn.read_until(b"Username: ")
tn.write(b"cisco\n")
tn.read_until(b"Password: ")
tn.write(b"cisco\n")

#enter privilege mode
tn.write(b"enable\n")
tn.read_until(b"Password: ")
tn.write(b"cisco\n")

#write configuration
tn.write(b"conf t\n")
tn.write(b"int lo10\n")
tn.write(b"ip address 10.10.10.3 255.255.255.0 \n")
tn.write(b"do write\n")
tn.write(b"end\n")

#print configuration
tn.write(b"show ip interface brief\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

#close remote
tn.close()