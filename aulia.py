import os
import sys
from time import sleep
#scriptpath = "../storage/emulated/0/aulia/login.py"
#sys.path.append(os.path.abspath(scriptpath))
#scriptpath = "../storage/emulated/0/aulia/greetings.py"
#sys.path.append(os.path.abspath(scriptpath))
#scriptpath = "../storage/emulated/0/aulia/list.py"
#sys.path.append(os.path.abspath(scriptpath))
def logo():
    os.system("clear")
    words = ''' \033[2;31;40m
  ______   __    __  __        ______   ______  
 /      \ |  \  |  \|  \      |      \ /      \ 
|  $$$$$$\| $$  | $$| $$       \$$$$$$|  $$$$$$\ ✿       
| $$__| $$| $$  | $$| $$        | $$  | $$__| $$
| $$    $$| $$  | $$| $$        | $$  | $$    $$
| $$$$$$$$| $$  | $$| $$        | $$  | $$$$$$$$
| $$  | $$| $$__/ $$| $$_____  _| $$_ | $$  | $$
| $$  | $$ \$$    $$| $$     \|   $$ \| $$  | $$
 \$$   \$$  \$$$$$$  \$$$$$$$$ \$$$$$$ \$$   \$$
 '''
    text = '''   ARITHMETIC UNDER-AGE LEARNING IN APPLICATION\033[0;0m\n'''
    for char in words:
        sleep(0.0015)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print("_"*49)    
    for char in text:
        sleep(0.040)
        sys.stdout.write(char)
        sys.stdout.flush()
def main():
    logo()
    print("\n","="*5,"PILIHAN MENU","="*5)
    print("\n1.LOGIN\n2.PERKENALAN\n3.INFORMASI DAN LIST\n0.KELUAR PROGRAM")
    pilih = input("MASUKAN PILIHAN : ")
    if pilih == "1":
        import login
    elif pilih == "2":
        import greetings
    elif pilih == "3":
        import list
    #elif pilih == "4":
        #import update
    elif pilih == "0":
        print("\nPROGRAM TELAH BERHENTI")
        sleep(1)
        os.system("clear")
        sys.exit(1)
    else:
        print("\nMOHON MASUKAN INPUT ANDA!")
        sleep(0.5)
        os.system("clear")
        import aulia
main()        