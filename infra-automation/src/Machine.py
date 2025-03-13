#stores machine details
class Machine:

    def __init__(self, name, os, cpu, ram, disk_usgae): #machine represintation as dict.
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
        self.disk_usgae = disk_usgae
        
    def machine_dict(self):
            return{ 
                "name" : self.name, "os" : self.os, "cpu" : self.cpu, 
                "ram" : self.ram, "disk_usage" : self.disk_usgae
            }
    def logging_creation(self):
        with open('logs/machine_creation.log', 'a') as log_file:
            log_file.write(f'\nThe machine has been created: {Machine.machine_dict}\n')

#machine = Machine("web-server", "Ubuntu", "2vCPU", "4GB", "10GB")
#machine.logging_creation()

