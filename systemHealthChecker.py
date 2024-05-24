###################################################
# A simple python script to monitor system health #
# Author Alexandru Filcu                          #
###################################################

##############################
# Import the necessary tools #
##############################

import os
import subprocess

#################################
# The check_disk_space function #
#################################

def check_disk_space():
    '''
    This function checks the disk space usage on the system.
    '''
    try:
        print("Now checking the disk space...")
        df_output = subprocess.check_output(['df', '-aHT'], universal_newlines=True)
        print("Disk Space Usage:\n", df_output)
    except subprocess.CalledProcessError as e:
        print("Failed to retrieve disk space information.")
        print("Error: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred.")
        print("Error: {}".format(e))

################################
# The check_cpu_usage function #
################################

def check_cpu_usage():
    '''
    This function checks the cpu usage on the system.
    '''
    try:
        print("Now checking the CPU usage...")
        top_output = subprocess.check_output(['top', '-bn1'], universal_newlines=True)
        for line in top_output.split('\n'):
            if line.startswith('%Cpu'):
                print("CPU Usage:\n", line)
                break
    except Exception as e:
        print("Failed to retrieve CPU usage:", e)

###################################
# The check_memory_usage function #
###################################

def check_memory_usage():
    '''
    This function checks the memory usage on the system.
    '''
    try:
        print("Now checking the memory usage...")
        mem_usage = subprocess.check_output(['free', '-h'], universal_newlines=True)
        print("Memory Usage:\n", mem_usage)
    except Exception as e:
        print("Failed to retrieve memory usage:", e)

######################################
# The check_active_services function #
######################################

def check_active_services():
    '''
    This function checks the active services on the system.
    '''
    try:
        print("Now checking active services...")
        systemctl_output = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--state=active'], universal_newlines=True)
        print("Active Services:\n", systemctl_output)
    except Exception as e:
        print("Failed to list active services:", e)

#############################
# The check_uptime function #
#############################

def check_uptime():
    '''
    This function checks the system uptime.
    '''
    try:
        print("Now checking system uptime...")
        uptime = subprocess.check_output(['uptime'], universal_newlines=True)
        print("System Uptime:\n", uptime.strip())
    except Exception as e:
        print("Failed to retrieve system uptime:", e)

######################################
# The check_connected_users function #
######################################

def check_connected_users():
    '''
    This function checks the connected users on the system.
    '''
    try:
        print("Now checking connected users...")
        who_output = subprocess.check_output(['who'], universal_newlines=True)
        users_list = [line.split()[0] for line in who_output.split('\n') if line.strip()]
        unique_users = set(users_list)
        num_users = len(unique_users)
        print("Connected Users:")
        print("\n".join(users_list))
        print("\nNumber of connected users: {}".format(num_users))
    except Exception as e:
        print("Failed to retrieve connected users:", e)

#####################
# The main function #
#####################

def main():
    while True:
        print("Choose an option:")
        print("1. Check Disk Space")
        print("2. Check CPU Usage")
        print("3. Check Memory Usage")
        print("4. Check Active Services")
        print("5. Check System Uptime")
        print("6. Check Connected Users")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            check_disk_space()
        elif choice == '2':
            check_cpu_usage()
        elif choice == '3':
            check_memory_usage()
        elif choice == '4':
            check_active_services()
        elif choice == '5':
            check_uptime()
        elif choice == '6':
            check_connected_users()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
