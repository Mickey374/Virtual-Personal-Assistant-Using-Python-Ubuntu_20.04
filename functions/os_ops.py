import os
import subprocess as sp

paths = {
    'vscode': "/usr/bin/code",
    'calculator': "/usr/bin/gnome-calculator"
}

def open_camera():
	sp.run('start /usr/bin/cheese', shell=True)

def open_vscode():
	os.startfile(paths['vscode'])

def open_calculator():
	os.startfile(paths['calculator'])

def open_term():
	os.system('start cmd')
