import os
import sys
import random

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def GOOD_WRITE(TEXT):
    print(color.GREEN+"    [+] "+color.GREEN+TEXT)

def INFO_WRITE(TEXT):
    print(color.BLUE+"    [i] "+color.GREEN+TEXT)

def ERROR_WRITE(TEXT):
    print(color.RED+"    [-] "+color.GREEN+TEXT)

def WARNING_WRITE(TEXT):
    print(color.YELLOW+"    [!] "+color.GREEN+TEXT)

print(color.BOLD+color.GREEN)

def BANNER():
    banner = """
                _____ _   ___   _ _      _      ______
               /  ___| | / / | | | |    | |    |___  /
               \ `--.| |/ /| | | | |    | |       / / 
                `--. \    \| | | | |    | |      / /  
          (@_  /\__/ / |\  \ |_| | |____| |____./ /___ 
     _     ) \_\____/\_| \_/\___/\_____/\_____/\_____/_______
    (_)@8@8{}<_______Automated Port-Forwarding Tool__________>
           )_/   Coded By Ghosty / DeaDHackS Team / V.1     
          (@"""
    print(banner)

def CLEAR():
    if "nt" in os.name:
        os.system("cls")
    else:
        os.system("clear")

def MAIN_MENU():
    print("""
    - 1 -: Port-Forward Port
    - 2 -: How Does It Work?
    - 3 -: Exit SKULLZ\n""")
    MAIN_MENU_CHOICE = input("    Skullz-portforward-server"+str(random.randint(1,1000))+"@root #> ")
    if MAIN_MENU_CHOICE == "1":
        PERSIST_CONNECT = ""
        PROTOCOL = ""
        ONLINE_PORT = ""
        ONLINE_HOST = ""
        LOCAL_PORT = ""
        LOCAL_HOST = ""
        CLEAR()
        BANNER()
        print("    -Do you wish to make sure the port-forwarding will be kept alive and not timing out? [Y/N]")
        ANTI_TIMING_OUT = input("    #> ")
        print("    =======================================")
        if ANTI_TIMING_OUT == "Y":
            print("    Which method do would you wish to use?:")
            print("       - 1 -: ServerInterval=60 - SSH")
            print("       - 2 -: AutoSSH - Must Be Installed.\n")
            ANTI_TIMING_OUT_CHOICE = input("    #> ")
            if ANTI_TIMING_OUT_CHOICE == "1":
                PERSIST_CONNECT = "ServerInterval"
            elif ANTI_TIMING_OUT_CHOICE == "2":
                PERSIST_CONNECT = "AutoSSH"
            else:
                PERSIST_CONNECT = "ServerInterval"
            print("    =======================================")
        print("    - What Protocol Would You Like To Port-Forward?:")
        print("      - 1 -: TCP")
        print("      - 2 -: HTTP - Custom Domain Name!")
        print("      - 3 -: SSH")
        PROTOCOL_CHOICE = input("    #> ")
        if PROTOCOL_CHOICE == "1":
            PROTOCOL = "TCP"
        elif PROTOCOL_CHOICE == "2":
            PROTOCOL = "HTTP"
        elif PROTOCOL_CHOICE == "3":
            PROTOCOL = "SSH"
        else:
            PROTOCOL = "TCP"
        print("    =======================================")
        if PROTOCOL == "HTTP":
            print("    - What Domain / IP you wish to redirect the HTTP traffic to?:")
            LHOST = input("    #> ")
            LOCAL_HOST = LHOST
            print("    =======================================")
            print("    - What Port you wish to redirect the HTTP traffic to? (80 Commonly Used):")
            LPORT = input("    #> ")
            LOCAL_PORT = LPORT
            print("    =======================================")
            print("    - What Domain you wish to use?:")
            RHOST = input("    s#> ")
            ONLINE_HOST = RHOST
            print("    =======================================")
            print("    - What Port you wish to use to access {0}?".format(LOCAL_HOST))
            RPORT = input("    #> ")
            ONLINE_PORT = RPORT
            print("    Connection Route:")
            print("       HTTP Connection => {0}:{1} HTTP Data => {2}:{2}".format(ONLINE_HOST,ONLINE_PORT,LOCAL_HOST,LOCAL_PORT))
        if PROTOCOL == "TCP":
            print("    - What IP you wish to redirect the TCP traffic to?:")
            LHOST = input("    #> ")
            LOCAL_HOST = LHOST
            print("    =======================================")
            print("    - What Port you wish to redirect the TCP traffic to?:")
            LPORT = input("    #> ")
            LOCAL_PORT = LPORT
            print("    =======================================")
            print("    - What Port you wish to access {0}?:".format(LOCAL_HOST))
            RPORT = input("    #> ")
            ONLINE_PORT = RPORT
            print("    Connection Route:")
            print("       TCP Connection => serveo.net:{0} TCP DATA => {1}:{2}".format(ONLINE_PORT,LOCAL_HOST,LOCAL_PORT))
        if PROTOCOL == "SSH":
            print("    - What IP you wish to redirect the SSH traffic to?:")
            LHOST = input("    #> ")
            LOCAL_HOST = LHOST
            print("    =======================================")
            print("    - What Port you wish to redirect the SSH traffic to? (22 Commonly Used):")
            LPORT = input("    #> ")
            LOCAL_PORT = LPORT
            print("    =======================================")
            print("    - What Domain you wish to use for the SSH server?:")
            RHOST = input("    #> ")
            ONLINE_HOST = RHOST
            print("    Connection Route:")
            print("       SSH Connection {0}:22 SSH Data => {1}:{2}".format(ONLINE_HOST,LOCAL_HOST,LOCAL_PORT))
        if PERSIST_CONNECT == "ServerInterval":
            if PROTOCOL == "TCP":
                os.system("ssh -o ServerAliveInterval=60 -R {0}:{1}:{2} serveo.net".format(ONLINE_PORT,LOCAL_HOST,LOCAL_PORT))
            if PROTOCOL == "HTTP":
                os.system("ssh -o ServerAliveInterval=60 -R {0}:{1}:{2}:{3} serveo.net".format(ONLINE_HOST,ONLINE_PORT,LOCAL_HOST,LOCAL_PORT))
            if PROTOCOL == "SSH":
                print("To access your SSH server run:")
                print("    ssh -j serveo.net user@{0}".format(ONLINE_HOST))
                os.system("ssh -o ServerAliveInterval=60 -R {0}:22:{1}:{2} serveo.net".format(ONLINE_HOST,LOCAL_PORT,LOCAL_PORT))
        elif PERSIST_CONNECT == "ServerInterval":
            if PROTOCOL == "TCP":
                os.system("autossh -M 0 {0}:{1}:{2} serveo.net".format(ONLINE_PORT,LOCAL_HOST,LOCAL_PORT))
            if PROTOCOL == "HTTP":
                os.system("autossh -M 0 {0}:{1}:{2}:{3} serveo.net".format(ONLINE_HOST,ONLINE_PORT,LOCAL_HOST,LOCAL_PORT))
            if PROTOCOL == "SSH":
                print("To access your SSH server run:")
                print("    ssh -j serveo.net user@{0}".format(ONLINE_HOST))
                os.system("autossh -M 0 {0}:22:{1}:{2} serveo.net".format(ONLINE_HOST,LOCAL_PORT,LOCAL_PORT))
        else:
            if PROTOCOL == "TCP":
                os.system("ssh -R {0}:{1}:{2} serveo.net".format(ONLINE_PORT, LOCAL_HOST,LOCAL_PORT))
            if PROTOCOL == "HTTP":
                os.system("ssh -R {0}:{1}:{2}:{3} serveo.net".format(ONLINE_HOST, ONLINE_PORT,LOCAL_HOST, LOCAL_PORT))
            if PROTOCOL == "SSH":
                print("To access your SSH server run:")
                print("    ssh -j serveo.net user@{0}".format(ONLINE_HOST))
                os.system("ssh -R {0}:22:{1}:{2} serveo.net".format(ONLINE_HOST, LOCAL_PORT,LOCAL_PORT))
        print("Thanks for using Skullz!\n")
    if MAIN_MENU_CHOICE == "2":
        print("    Skullz uses a free port-forwarding service named serveo.")
        print("    Serveo is a SSH-Based port forwarder service and SKullz automates it.")
        print("    Skullz will configure the SSH request so the port-forwarding request.")
    if MAIN_MENU_CHOICE == "3":
        print("Thanks for using Skullz")
        sys.exit()


def MAIN():
    CLEAR()
    BANNER()
    while True:
        MAIN_MENU()
MAIN()