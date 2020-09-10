"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = "10.1.1.200"
print("value of ip is: ",ip)
print("value of str(ip) is: ",str(ip))
print("type of ip is: ",type(ip))


# TODO: Write a conditional to print out if `iosversion` is less than or greater than 14
i = random.randint(12, 17)
if i < 14:
    print("i is " + str(i) + " which is < 14.")
elif i > 14:
    print("i is " + str(i) + " which is > 14.")
else:
    print('i is {}'.format(i))

# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1) [0]
device = list(device.values())[0]
print("The serial # of the device is " + str(device))


# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask

'''
TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''

# Lots of ways to break this, needs input validation, error checking
while True:
    ipaddr = input("Enter IP in CIDR notation w.x.y.z/nn or 'quit' to exit: ")
    if ipaddr == "quit":
        break
    else:
        print("In netmask notation, that should be " + cidr_to_netmask(ipaddr))

print()
