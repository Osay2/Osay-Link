import time
from requests import get
import webbrowser
import requests as nya
import os

blue = "\033[1;34;40m"
reset = "\033[0;37;40m"
cyan = "\033[1;36;40m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"


os.system("clear")

print()
print("""

┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋┏┓
┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋┃┃
┃┃╋┃┣━━┳━━┳┓╋┏┓╋╋┃┃╋╋┏┳━┓┃┃┏┓
┃┃╋┃┃━━┫┏┓┃┃╋┃┣━━┫┃╋┏╋┫┏┓┫┗┛┛
┃┗━┛┣━━┃┏┓┃┗━┛┣━━┫┗━┛┃┃┃┃┃┏┓┓
┗━━━┻━━┻┛┗┻━┓┏┛╋╋┗━━━┻┻┛┗┻┛┗┛
╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋┗━━┛""")
print(red+"""				by Osay""")
print()
print(yellow+"Su enlace va a ser acortar en TinYurl\n")

a=input(green+'Ingrese el enlace que va a acortar:\t ')

b='http://tinyurl.com/api-create.php?url='+a

print("")
print()


x=nya.get(b)
if x.status_code==200:
    x=get(b).text
    print(green+"¡Hecho!")
    time.sleep(1)
    
    print(blue+"""===================""")
    print(cyan+""" Enlace Original: """+a)
    print(""" Enlace Acortado: """+x)
    print(blue+"""===================""")
    
    time.sleep(5)
    print(reset+" ")
    exit()
else:
    print(blue+"""===============""")
    print(red+"Error\n")
    time.sleep(1)
    print(green+"Reiniciando script...")
    print(blue+"""===============""")
    time.sleep(3)
    print(reset+" ")
    os.system("python osay-link.py")
 