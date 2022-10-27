import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Casi listo!")
print(f"Inicializando un Repositorio Git...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'init', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}El inicio de tu destino comienza ahora!. Crea y diviertete!{RESET_ALL}")