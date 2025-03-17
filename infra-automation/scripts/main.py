import sys
import os
import json
import argparse



def parse_arguments():
    parser = argparse.ArgumentParser(description="Enter machine configuration details.")
    # Add argument for machine name
    parser.add_argument('--name', type=str, help="Enter the machine name (write 'esc' to exit)")
    
    # Add argument for OS
    parser.add_argument('--os', type=str, choices=['ubuntu', 'windows', 'mac', 'linux'],
                        help="Enter the OS (e.g ubuntu, windows, mac etc.)")
    
    # Add argument for the number of CPU cores
    parser.add_argument('--cpu', type=int, help="Enter the number of CPU cores to use")
    
    # Add argument for RAM
    parser.add_argument('--ram',type=str,help="Enter the amount of RAM to use in GB (e.g 1GB, 3GB)")
    
    # Add argument for disk usage
    parser.add_argument('--disk_usage', type=int, help="Enter Disk usage in GB")
    args = parser.parse_args()
    return args

def validate_ram(ram):
    if ram.endswith("GB"):
        try:
            ram_size = int(ram[:-2])  # Remove 'GB' and convert to integer
            if ram_size > 0:
                return ram_size
            else:
                raise ValueError("RAM size must be greater than 0.")
        except ValueError:
            raise ValueError("Invalid RAM value. Please enter a valid number followed by 'GB'.")
    else:
        raise ValueError("RAM must be specified in GB (e.g 1GB, 3GB).")


def main():
    args = parse_arguments() 
    #Initalizes the arguments being passed when running the code, then they are used inside our code.

    # Check for the 'esc' condition
    if args.name.lower() == 'esc':
        print("Exiting program...")
        sys.exit()

    try:
        # Validate RAM input
        ram_size = validate_ram(args.ram)
        
        # Create the configuration dictionary
        config_data = {
            'name': args.name,
            'os': args.os,
            'cpu': args.cpu,
            'ram': f"{ram_size}GB",
            'disk_usage': args.disk_usage
        }
        print(config_data)
        with open('instance.json', 'w') as json_file:
             json.dump(config_data, json_file, indent=4)
        file_path = 'instance.json'
        print(f"Config data saved to {file_path}")

        # Print the configuration
        print("\nMachine Configuration:")
        print(f"Machine Name: {args.name}")
        print(f"Operating System: {args.os}")
        print(f"CPU Cores: {args.cpu}")
        print(f"RAM: {ram_size}GB")
        print(f"Disk Usage: {args.disk_usage}GB")


    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



