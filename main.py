import os
from _modules import clear, log
from _modules.menus import homepage

print(os.name)

system_type = 'NotSet'

if os.name == 'nt':
    system_type = 'MsDOS'
elif os.name == 'posix':
    system_type = 'Unix'

if not os.path.exists('config/Systeminfo.cfg'):
    os.makedirs('config')
    with open('config/Systeminfo.cfg', 'w') as f:
        f.write(f'DE=\nSYS={system_type}')
clear.clear()

log.lok(f'Your system type: ' + system_type, 0.3)
log.lok('Loading IcePy...', 0.5)
log.lok('Loaded IcePy', 0.2)
log.lok('Loaded modules: clear, log, menus.homepage, menus.cfgproject', 0.4)
log.lok('All fine! Hello world!', 0.6)


if __name__ == '__main__':
    homepage.start_menu()