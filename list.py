import os
import sys
import time
scriptpath = "../storage/emulated/0/aulia/aulia.py"
sys.path.append(os.path.abspath(scriptpath))
def listalat():
    os.system("clear")
    alat = '''
    \033[2;31;40m
  _     ___ ____ _____      _    _        _  _____ 
 | |   |_ _/ ___|_   _|    / \  | |      / \|_   _|
 | |    | |\___ \ | |     / _ \ | |     / _ \ | |  
 | |___ | | ___) || |    / ___ \| |___ / ___ \| |  
 |_____|___|____/ |_|   /_/   \_\_____/_/   \_\_|  
 \033[0;0m                                                  

    LIST BERDASARKAN TINGKAT SEKOLAH
    ________________________________
    A.SD :
        1.BILANGAN 1-99
        2.ANGKA GANJIL ATAU GENAP
        3.KALKULATOR SEDERHANA
        4.'''
    for char in alat:
        time.sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()
listalat()