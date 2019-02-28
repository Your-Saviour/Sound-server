from netifaces import interfaces, ifaddresses, AF_INET
bigdict = {}
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    print('{}: {}'.format(ifaceName, ', '.join(addresses)))
    addressesnew = ', '.join(addresses)
    if addressesnew != 'No IP addr':
        bigdict[ifaceName] = addressesnew

print(bigdict)
