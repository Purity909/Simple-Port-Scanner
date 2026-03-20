import socket
import os
import struct
import ipaddress

HOST = socket.gethostbyname(socket.gethostname())

def decode_ip(raw_data):
    header = raw_data[:20]
    iph = struct.unpack('!BBHHHBBH4s4s', header)
    version = iph[0] >> 4
    ihl = (iph[0] & 0xF) * 4
    ttl = iph[5]
    protocol = iph[6]
    src = ipaddress.ip_address(iph[8])
    dst = ipaddress.ip_address(iph[9])
    print(f"Version: {version}, Header Length: {ihl}, TTL: {ttl}")
    print(f"Protocol: {protocol}, Source: {src}, Destination: {dst}")

def main():
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    raw_data, addr = sniffer.recvfrom(65565)
    decode_ip(raw_data)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    main()