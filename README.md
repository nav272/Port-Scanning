# Port-Scanning
### TCP and UDP port scanning is a method of determining what applications a host is running  
-------------------------

TCP and UDP port scanning is a method of determining what applications a host is
running. I developed 2 Python programs using the SCAPY module to scan TCP and
UDP ports on the external router rtr in VLAB.

For TCP, I scaned all the ports from 0 to 100. I collected the responses and sort
them by their status of OPEN, CLOSED, FILTERED. i.e. OPEN:1, 2, 3, ...; CLOSED:8, 9,
...;FILTERED: 11, 12, ...

For UDP, I also scanned all the ports from 0 to 100 and collected the responses by their
status of CLOSED and OPEN.

### Account for dropped packets: 
If you send out a TCP/SYN packet and get no response you should send out another as the packet may have
been dropped. You can see the same logic implemented in my TCP_Port_Scan.py program.

For UDP, no response means either the port is OPEN or the packet was
dropped. You should send out additional UDP packets to verify. You can see the same logic implemented in my UDP_Port_Scan.py program.

For an open UDP port lookup the service name associated with the port number and send a
well-formed UDP packet for that service to the port to verify it is running a service and
what that service is. You can see the same logic implemented in my UDP_Port_Services.py program. 

Look up service names and transport protocol numbers from the
number registry in iana.org. http://www.iana.org/assignments/service-names-portnumbers/service-names-port-numbers.xhtml
