from colorama import Fore, Style, Back
from _modules.menus import cfgproject
from _modules.clear import clear
from _modules.basemenus import tooltip

AppVersion = 0.1

def start_menu():
    clear()

    tooltip.add(style=3_1, text='1. FILE', text2='2. OPTIONS', parametr1=f'v{AppVersion}', parametr2='IcePy', text3='')

    print('\n\n   ' + '1.1 New project')

    sm_select = input("\n     ")

    clear()

    def file_menu():

        def tm_txt_add(text):
            print(Back.WHITE + Fore.BLACK + text + Style.RESET_ALL)

        tooltip.add(style=3_1, text='1. FILE', text2='2. OPTIONS', parametr1=f'v{AppVersion}', parametr2='IcePy', text3='')
        tm_txt_add("1.1 New Project")

        fm_input = input("\n    ")

        if fm_input == '1.1':
            cfgproject.cfgpr('new')
        else:
            start_menu()

    if sm_select == '1':
        file_menu()
    elif sm_select == '1.1':
        cfgproject.cfgpr('new')
    else:
        start_menu()