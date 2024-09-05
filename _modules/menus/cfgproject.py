import os
from colorama import Fore, Style, Back

from _modules.clear import clear
from  _modules import log
from _modules.menus import  homepage

from _modules.__Env__ import __loadeditor__

from _modules.menus._cfgp.createder import __createder__

def cfgpr(mode):
    clear()
    if mode == 'new':
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "New Project             " + Fore.WHITE + Back.RED + " X " + Style.RESET_ALL)
        print('\n\n')
        def createproject():
            name_of_project = input('   Name of project: ')
            if not os.path.exists(f'Projects'):
                os.makedirs('Projects')
            if not os.path.exists(f'Projects/{name_of_project}'):
                os.mkdir(f'Projects/{name_of_project}')



                def codeop_sel():
                    print("\n   Codes:\n    \pygame\n")
                    code_of_project = input("   Code type (default: pygame): ")

                    if code_of_project == '':
                        print('\n')
                        log.lok('Set to "pygame"!', 0)
                        code_of_project = 'pygame'
                        __createder__(name_of_project, code_of_project)
                    elif code_of_project == 'pygame':
                        print('\n')
                        log.lok('Set to "pygame"!', 0)
                        __createder__(name_of_project, code_of_project)
                    else:
                        print('\n')
                        log.ler('Not code!', 0.6)
                        print('\n')
                        codeop_sel()

                codeop_sel()
                log.lok('Wait a create project cfg file... (1,5 secs)', 1.5)
                with open(f'Projects/{name_of_project}/.ignore.projecticepy', 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith('Code='):
                            code_of_project = line.strip().split('=')[1]

                def toe_sel():
                    toe = input('Tutorial (t) or Editor (e)?\n  ')
                    if toe == "e":
                        __loadeditor__.load(f'{name_of_project}', code_of_project)
                    elif toe == "t":
                        print()
                    else:
                        log.ler(f'{toe} is not select!', 0.6)
                        toe_sel()
                toe_sel()
            else:
                clear()
                log.ler('This project already exists!', 0.7)
                cfgpr('new')
        createproject()
    else:
        log.ler('Not set mode. Reverse to homepage in 1 sec...', 1)
        homepage.start_menu()
