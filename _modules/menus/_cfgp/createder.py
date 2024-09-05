import os
from _modules.menus import homepage

def __createder__(_nop, _cop):

    pp = f'Projects/{_nop}'

    with open(f'{pp}/main.py', "w") as file:
        file.write("import pygame\n\ndef main():\n  print('This is project by IcePy')\n\n\n\n\nif __name__ == '__main__':\n    main()")
    with open(f'{pp}/.ignore.projecticepy', "w") as file:
        file.write(f"BuilderVer={homepage.AppVersion}\nCode={_cop}\nName={_nop}\nDefaultBlockImport\n   \Pyg\n  \Cmd")

    ibp = f'{pp}/ImportedBlocks'

    os.mkdir(f'{ibp}')
    os.mkdir(f'{ibp}/PyG')
    os.mkdir(f'{ibp}/Cmd')