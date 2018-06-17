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
	p=srl(IP(dst=destip)/UDP(sport=RandShort(), dport=i), timeout=10)
	if(str(type(p)== "<type 'Nonetype'>")):
		filterport.append(i)
		continue
	if(p.haslayer(UDP)):
		openport.append(i)
	elif(p.haslayer(ICMP)):# This is the hexadecimal equivalent of rst,ack we get, when port is closed
		ic=p.getlayer(ICMP)
		if(int(ic.type == 3) and int(ic.code == 3)):
			closeport.append(i)

print "Open ports in the given range are: ", openport
print "Closed ports in the given range are: ", closeport
print "Filtered ports in the given range are: ", filterport

