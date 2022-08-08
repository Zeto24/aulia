import os
import sys
import string
import time
from time import sleep
#scriptpath = "../storage/emulated/0/aulia/login.py"
#sys.path.append(os.path.abspath(scriptpath))
def login():
    os.system("clear")
    word = '''\033[2;31;40m
 _____ ___  ____  __  __   _     ___   ____ ___ _   _ 
|  ___/ _ \|  _ \|  \/  | | |   / _ \ / ___|_ _| \ | |
| |_ | | | | |_) | |\/| | | |  | | | | |  _ | ||  \| |
|  _|| |_| |  _ <| |  | | | |__| |_| | |_| || || |\  |
|_|   \___/|_| \_|_|  |_| |_____\___/ \____|___|_| \_|
\033[0;0m'''
    print(word,"\n")
    print("="*45,"\n")
    nama = input("NAMA            : ")
    nama1 = nama.upper()
    sekolah = input("[TINGKAT SEKOLAH]\n'SD/SMP/SMK'    : ")
    sekolah1 = sekolah.upper()
    if sekolah1 == 'SD':
        kelas = input("[KELAS]\n'1/2/3/4/5/6'   : ")
    elif sekolah1 == 'SMP':
        kelas = input("[KELAS]\n'7/8/9'      :")
    elif sekolah1 == 'SMK':
        kelas = input("[KELAS]\n'10/11/12' : ")
    namase = input("NAMA SEKOLAH    : ")
    namase1 = namase.upper()
    sleep(0.1)		
    lanjut = input("\nLOGIN? 'Y/R'    : ")
    lanjut = lanjut.upper()
    if lanjut == "Y":
        print("\nSELAMAT DATANG","\033[2;31;40m",nama1,"\033[0;0m")
        print("SELAMAT BELAJAR :)")
        time.sleep(2)
        os.system("clear")
        import menu
    elif lanjut == "R":
       import login
    else:
       print("MOHON MASUKAN INPUT ANDA")
       sleep(0.5)
       import login
login()