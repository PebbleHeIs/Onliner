##MODULES
import os, requests, colorama, threading, asyncio, discord, time, AuthGG, getpass, webbrowser, sys
from AuthGG.client import Client
from colorama import Fore
from colorama import init
from os import system
from requests import get
##END

##CLONER
def onliner():
    os.system("CLS")
    colorama.init()
    init(strip=not sys.stdout.isatty())
    from termcolor import cprint 
    from pyfiglet import figlet_format

    cprint(figlet_format('Kings Onliner', font='starwars'),
           'yellow', 'on_red', attrs=['bold'])

    print("Discord : https://bit.ly/3HbJupE")

    print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Online')
    print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Do Not Disturb')
    print(f'{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Idle')
    onlinr = int(input('[?]> '))

    tuk = []

    tokens = open("./data/tokens.txt", "r").read().splitlines()

    asc = asyncio.new_event_loop()
    asyncio.set_event_loop(asc)

    if onlinr == 1:
        for token in tokens:
            bottuk = discord.Client(status=discord.Status.online)
            asc.create_task(bottuk.start(token, bot=False))
            tuk.append(bottuk)
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
    if onlinr == 2:
        for token in tokens:
            bottuk = discord.Client(status=discord.Status.do_not_disturb)
            asc.create_task(bottuk.start(token, bot=False))
            tuk.append(bottuk)
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
    if onlinr == 3:
        for token in tokens:
            bottuk = discord.Client(status=discord.Status.idle)
            asc.create_task(bottuk.start(token, bot=False))
            tuk.append(bottuk)
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')

    threading.Thread(target=asc.run_forever).start()

    time.sleep(5)
    exit = input('press any key: ')
    exit = clear()
    exit = os.system("exit")
    exit = print("Tokens will stay online until you EXIT the program.")

##END


## MAIN
def mainer():
    client = Client(api_key="1324955647639776688121468431273586", aid="510540", application_secret="WDEKNIlFFKiq5L6YsmJ516CCbjDh3pIri0T")


    ur = 'https://discord.com/api/v9/channels/messages'
    title = 'Kings Cheats Cloner | PebbleHeIs'
    system(f'title {title}')
    tokens = open('./data/tokens.txt', 'r').read().splitlines()

    clear = lambda: os.system('cls')
    clear()

    print("""
db   dD d888888b d8b   db  d888b  .d8888.       .d88b.  d8b   db db      d888888b d8b   db d88888b d8888b. 
88 ,8P'   `88'   888o  88 88' Y8b 88'  YP      .8P  Y8. 888o  88 88        `88'   888o  88 88'     88  `8D 
88,8P      88    88V8o 88 88      `8bo.        88    88 88V8o 88 88         88    88V8o 88 88ooooo 88oobY' 
88`8b      88    88 V8o88 88  ooo   `Y8b.      88    88 88 V8o88 88         88    88 V8o88 88~~~~~ 88`8b   
88 `88.   .88.   88  V888 88. ~8~ db   8D      `8b  d8' 88  V888 88booo.   .88.   88  V888 88.     88 `88. 
YP   YD Y888888P VP   V8P  Y888P  `8888Y'       `Y88P'  VP   V8P Y88888P Y888888P VP   V8P Y88888P 88   YD 
                                                                                                           
                                                                                                           
     Discord : https://bit.ly/3HbJupE
         """)

    print("[1] - Login")
    print("[2] - Register")
    print("[3] - YouTube")

    choice = input('[?]> ')

    if choice == '1':
        print("")
        print("")
        print("")
        user = input("Username: ")
        password = getpass.getpass("Pass: ")
        try:
            client.login(user, password)
            onliner()
        except Exception as e:
            print(e)
            print("Wait 5 seconds to go back to main menu.")
            mainer()

    if choice == '2':
        print("")
        print("")
        print("")
        mail = input("Email: ")
        key = input("Key: ")
        user = input("Username: ")
        password = getpass.getpass("Pass: ")

        try:
            client.register(email=mail, username=user, password=password, license_key=key)
            print("Wait 5 seconds to go back to the main menu and login!")
            time.sleep(5)
            mainer()

        except Exception as e:
            print(e)

    if choice == '3':
        webbrowser.open('https://www.youtube.com/channel/UC5nJcAJHJGATozSwael1AcQ')
        mainer()

## MAIN END

## START
mainer()
