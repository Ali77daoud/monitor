from pysnmp.hlapi import *
from datetime import timedelta

class snmp_monitor:
    def __init__(self,ip,community):
        self.ip=ip
        self.community=community
#return device name

    def get_devicename(self):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData('ali'),
                   UdpTransportTarget(('192.168.1.1', 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0')))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(varBind[1])
#return the interfaces using getnext

    def get_interfaces(self):
        iterator = nextCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2')),
                   maxCalls=self.get_numberofinter()
        )


        for errorIndication, errorStatus, errorIndex, varBinds in iterator:
            if errorIndication:
                print(errorIndication)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
                break

            else:
                for varBind in varBinds:
                    print(varBind[1])
#return the number of interfaces using get

    def get_numberofinter(self):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.1.0')))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                return varBind[1]
#return uptime of the device
    def get_uptime(self):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                s = int(varBind[1])
                seconds = int(s / 100)
                up_time = timedelta(seconds=seconds)
                print(up_time)

m=snmp_monitor('192.168.1.1','ali')
m.get_devicename()