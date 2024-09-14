# sudok-telecom
Set of helper scripts to use SBPC + LTE dongle as mobile hotspot

# install
```
sudo apt install net-tools hostapd dnsmasq

sudo cp lte_set_ip_helper.py /opt/lte_set_ip_helper.py
sudo cp mbim-network.conf /etc/mbim-network.conf
sudo cp hostapd.conf /etc/hostapd/hostapd.conf
sudo cp dnsmasq.conf /etc/dnsmasq.conf

# If you already have iptables rules - don't copy whole file
sudo cp iptables.rules /etc/iptables.rules

# If you already have rc.local - don't copy whole file
sudo cp rc.local /etc/rc.local
sudo chmod 755 /etc/rc.local

sudo echo 'net.ipv4.ip_forward = 1' >> /etc/sysctl.conf
```