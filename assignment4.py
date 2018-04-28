
import nmap

def port_scanner(ports):
    nm = nmap.PortScanner()
    nm.scan(ports, '21-1000')
    for host_names in nm.all_hosts():
        ports = nm[host_names].get('tcp')
        benevis(ports)

    return ports


def benevis(contents):
    f = open('javab', 'w')
    pasokh = str(contents)
    f.write(pasokh)

    pass


def main():
    hosts = [
        'fileniko.com'
        'appniko.com'
        'tvniko.com'
        'iaun.ac.ir'
        'hadipoor.ir'
        'google.com',
    ]

    for host_name in hosts:
        port_scanner(host_name)

main()
