from _modules.__Env__.Editor import editor_load
from _modules.menus import homepage

def load(name, code):
    editor_load(projectname=f'{name}', code=f'{code}', builderver=f'{homepage.AppVersion}')