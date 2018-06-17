from scapy.all import*
destip="10.10.111.1" #A valid destination IP address

# We will define the port range we want to scan.

a=0
b=100
ports=range(a,b)

# Creating empty lists for open ports, closed ports and filtered ports
openport=[]
closeport=[]
filterport=[]

for i in ports:
	p=srl(IP(dst=destip)/TCP(sport=RandShort(), dport=i, flags="S"), timeout=10)
	if(str(type(p)== "<type 'Nonetype'>")):
	
	if(p.haslayer(TCP)):
		tlayer = p.getlayer(TCP).flags
		print tlayer
		if(tlayer == 0x12): #This is the hexadecimal equivalent of syn,ack we get, when port is open
			openport.append(i)
		elif(tlayer == 0x14):# This is the hexadecimal equivalent of rst,ack we get, when port is closed
			closeport.append(i)

print "Open ports in the given range are: ", openport
print "Closed ports in the given range are: ", closeport
print "Filtered ports in the given range are: ", filterport

