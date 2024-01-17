from scapy.all import ARP, Ether, srp

target_ip = "192.168.86.112"

# create ARP packet, this broadcasts a request packet to all machines on the LAB, and asks if an pf the machines are using that particular IP address
# a broadcast packet contains te destination IP 
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether/arp

#srp() in scapy is use to send and receive packets at layer 2
result = srp(packet, timeout=3, verbose=0)[0]

clients = []

for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
print("IP" + " "*8+"MAC")
for client in clients:
    print("{:8} {}".format(client['ip'], client['mac']))