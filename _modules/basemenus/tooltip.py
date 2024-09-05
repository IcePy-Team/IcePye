from colorama import Fore, Back, Style

def add(style, text, text2, text3, parametr1, parametr2):
    if style == 1:
        print(Back.WHITE + Fore.BLACK + text + Style.RESET_ALL)
    elif style == 2:
        print(Back.WHITE + Fore.BLACK + text + " " + Style.RESET_ALL + Back.WHITE + Fore.BLACK + text2  + Style.RESET_ALL + " ")
    elif style == 3:
        print(Back.WHITE + Fore.BLACK + text + " " + Style.RESET_ALL + Back.WHITE + Fore.BLACK + text2 + Style.RESET_ALL + " " + Back.WHITE + Fore.BLACK + text3 + Style.RESET_ALL + " ")
    elif style == 3_1:
        print(Style.BRIGHT + Fore.CYAN + parametr2 + " | " + parametr1 + Style.RESET_ALL + " \n" + Back.WHITE + Fore.BLACK + text + Style.RESET_ALL + " " + Back.WHITE + Fore.BLACK + text2 + Style.RESET_ALL + " " + Back.WHITE + Fore.BLACK + text3 + Style.RESET_ALL + " ")