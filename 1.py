import netmiko
from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.43.210',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin',

}

net_connect =ConnectHandler(**iosv_l2)

output =net_connect.send_command('show arp')
print(output)

