import os

dev = 'cdc-wdm0'
iface = 'wwan0'

os.popen('mbim-network /dev/%s start' % dev)
res = os.popen('mbimcli -d /dev/%s -p --query-ip-configuration' % dev).read().splitlines()

nameservers = []

for line in res:
    if 'IPv6' in line:
        break
    elif 'IP ' in line:
        ip_addr = line.split(':')[1].strip()[1:-1]
    elif 'Gateway' in line:
        gw_addr = line.split(':')[1].strip()[1:-1]
    elif 'DNS' in line:
        nameservers.append(line.split(':')[1].strip()[1:-1])
    elif 'MTU' in line:
        mtu = line.split(':')[1].strip()[1:-1]

print('ip_addr= %s' % ip_addr)
print('gw_addr= %s' % gw_addr)
print('nameservers= %s' % nameservers)
print('mtu= %s' % mtu)

os.popen('ifconfig %s up %s mtu %s' % (iface, ip_addr, mtu))
os.popen('route add default gw %s %s' % (gw_addr, iface))

with open('/etc/resolv.conf', 'w') as f:
    content = ['nameserver '+ns+'\n' for ns in nameservers]
    f.writelines(content)