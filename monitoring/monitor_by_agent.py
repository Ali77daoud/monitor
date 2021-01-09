import psutil
import platform

class Agent_monitor:
    #cpu
    def get_cpu(self):
        name = psutil.cpu_times(percpu=False)
        print(
            f'time user = {name[0]} sec     time system = {name[1]} sec   time idle = {name[2]} sec     time of interrupt = {name[3]} sec')

        name1 = psutil.cpu_percent(interval=2, percpu=False)
        print(f"usage of cpu = {name1} %")

        name2 = psutil.cpu_times_percent(interval=2, percpu=False)
        print(
            f"used of cpu by user = {name2[0]} %     used of cpu by system = {name2[1]} %    idle of cpu = {name2[2]} %  interrupt in cpu = {name2[3]} %")

        name3 = psutil.cpu_count(logical=False)
        print(f'number of cores = {name3} core')

        core = psutil.cpu_count(logical=True)
        print(f'number of logical processors = {core} core')
        cpu1 = psutil.cpu_freq(percpu=False)
        print(f'freq of cpu :  current freq = {cpu1[0]} Mhz   min freq = {cpu1[1]} Mhz  max freq = {cpu1[2]} Mhz')
    #Ram
    def get_ram(self):
        ram = psutil.virtual_memory()
        print(
            f'total ram = {ram[0]} MB   available space = {ram[1]} MB    percent of used = {ram[2]} %   used space = {ram[3]} MB    free space = {ram[4]} MB')
    #Disk
    def get_disk(self):
        disk_info = psutil.disk_partitions()
        print("Disks:")

        for x in disk_info:
            try:
                disk = {
                    "name": x.device,
                    "mount_point": x.mountpoint,
                    "type": x.fstype,
                    "total_size": psutil.disk_usage(x.mountpoint).total,
                    "used_size": psutil.disk_usage(x.mountpoint).used,
                    "percent_used": psutil.disk_usage(x.mountpoint).percent
                }

                print("\tDisk name", disk["name"], "\tMount Point:", disk["mount_point"], "\tType", disk["type"],
                      "\tSize:", disk["total_size"] / 1e+9, "\tUsage:", disk["used_size"] / 1e+9, "\tPercent Used:",
                      disk["percent_used"], '%')
            except:
                print("")
    # Network Info
    def get_network(self):
        nics = []
        print("NICs:")
        for name, snic_array in psutil.net_if_addrs().items():
            # Create NIC object
            nic = {
                "name": name,
                "mac": "",
                "address": "",
                "address6": "",
                "netmask": ""
            }
            # Get NiC values
            for snic in snic_array:
                if snic.family == -1:
                    nic["mac"] = snic.address
                elif snic.family == 2:
                    nic["address"] = snic.address
                    nic["netmask"] = snic.netmask
                elif snic.family == 23:
                    nic["address6"] = snic.address
            nics.append(nic)
            print("\tNIC:", nic["name"], "\tMAC:", nic["mac"], "\tIPv4 Address:", nic["address"], "\tIPv4 Subnet:",
                  nic["netmask"], "\tIPv6 Address:", nic["address6"])
    # Platform Info
    def get_platform(self):
        system = {
            "name": platform.system(),
            "version": platform.release()
        }
        print("OS:\n\t", system["name"], system["version"])

m=Agent_monitor()
m.get_ram()