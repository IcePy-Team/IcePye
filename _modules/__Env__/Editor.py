from _modules import log, cd
from _modules.clear import clear
from _modules.basemenus import tooltip

EditorVer = '0.1'

def editor_load(projectname, code, builderver):

    clear()
    log.lok('Loading Editor...', 0)
    cd.cd(0.6)
    log.lok('Loading Finish!', 0.4)
    log.lok('Loading project...', 0.8)
    log.lok(f'Loaded! Statistic:\n\n Name: {projectname}  Code: {code}\n  BuilderVersion: {builderver}', 1)

    def main():

        def main_menu():
            clear()
            tooltip.add(3_1, 'Project', 'Editor', '', parametr2='Editor', parametr1=f'v{EditorVer}')

        main_menu()
    main()