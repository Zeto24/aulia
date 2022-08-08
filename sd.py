import os
import sys
import time

def menu1():
    urutan = '''
    [PILIHAN OPSI]
    
    1.MENGENAL BILANGAN CACAH
    2.KALKULATOR
    3.MENGENAL SATUAN WAKTU, PANJANG, DAN BERAT
    '''
    for char in urutan:
        time.sleep(0.003)
        sys.stdout.write(char)
        sys.stdout.flush()
menu1()
pilih = input("MASUKAN OPSI ANDA : ")
if pilih == "1":
    import bilcacah
elif pilih == "2":
    import kalk
else:
    print("MOHON MASUKAN INPUT ANDA!")
    time.sleep(0.1)
    import sd