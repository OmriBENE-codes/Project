#User input Infrastructure Provisioning
from pydantic import ValueError
from src.Machine import Machine
import json

def user_vm_input(): #askes user for input to validate it.
    selected_machine = [] #empty list for user input as json at the end.
    while True: #loop if user wants to continue or stop the process.
        name = input("Please enter the machine name: (write 'esc' to exit)")
        if name.lower() == 'esc': #usinng lower case for no mistyping 
            break
        os = input('Enter the OS (e.g ubuntu, windows, mac etc.): ')
        cpu = int(input('Enter the number of cpu cores to use: '))
        ram = input('Enter the amount of RAM to use in GB: (e.g 1GB, 3GB)')
        disk_usage = input('Enter Disk usage in GB: ')

        machine_content = { #new dictionary to save the inputs for the machine
            "name" : name,
            "os" : os,
            "cpu" : cpu,
            "ram" : ram,
            "disk usage" : disk_usage
        }
        selected_machine.append(machine_content) #adding the content to the empty list
    return selected_machine

machine_info = user_vm_input #getting the return from user_vm_input to save in a json file.
with open('configs/instance.json', 'w') as j_file:
    j_file.write(json.dump(machine_info, indent=3)) #writes the content to the file and give it a nice look with indent


