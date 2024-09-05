from colorama import Fore, Style
from time import sleep

def lok(text, cd):
    print('[ ' + Fore.GREEN + Style.BRIGHT + "OK" + Style.RESET_ALL + ' ] ' + text)
    sleep(cd)
def ler(text, cd):
    print('[ ' + Fore.RED + Style.BRIGHT + "ERROR" + Style.RESET_ALL + ' ] ' + text)
    sleep(cd)
