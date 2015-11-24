from subprocess import check_output

class net():

    @staticmethod
    def ifconfig_iface():
        ifconfig = check_output(['ifconfig', 'eth0'])
        ifconfig.split()
        iface =(ifconfig.split()[0])
        return iface

    @staticmethod
    def ifconfig_IP():
        # this is for IPV4 not IPV6

        # ipv6 is [11]
        ifconfig = check_output(['ifconfig', 'eth0'])
        ifconfig.split()
        ip = (ifconfig.split()[6][5:])
        return ip

    @staticmethod
    def ifconfig_Mac():

        # going to get hardware Mac address
        ifconfig = check_output(['ifconfig', 'eth0'])
        ifconfig.split()
        mac = (ifconfig.split()[4])
        return mac

    @staticmethod
    def ifconfig_Bcast():

        ifconfig = check_output(['ifconfig', 'eth0'])
        ifconfig.split()
        bcast = (ifconfig.split()[7][6:])
        return bcast

    @staticmethod
    def ifconfig_subnet():

        ifconfig = check_output(['ifconfig', 'eth0'])
        ifconfig.split()
        subnet = (ifconfig.split()[8][5:])
        return subnet

    @staticmethod
    def ifconfig_IPV6():

        ifconfig = check_output(['ifconfig', 'eth0'])
        ifconfig.split()
        ipv6 = (ifconfig.split()[11])
        return ipv6



