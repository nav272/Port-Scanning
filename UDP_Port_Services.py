from scapy.all import*
destip="10.10.111.1" 
packet=srl(IP(dst=destip)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="Router")))
print packet[DNS].summary