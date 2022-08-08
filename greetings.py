import os
import sys
import time
scriptpath = "../storage/emulated/0/aulia/aulia.py"
sys.path.append(os.path.abspath(scriptpath))
def greetings():
    os.system("clear")
    greet = '''
    \033[2;31;40m
   ____ ____  _____ _____ _____ ___ _   _  ____ ____  
  / ___|  _ \| ____| ____|_   _|_ _| \ | |/ ___/ ___| 
 | |  _| |_) |  _| |  _|   | |  | ||  \| | |  _\___ \ 
 | |_| |  _ <| |___| |___  | |  | || |\  | |_| |___) |
  \____|_| \_\_____|_____| |_| |___|_| \_|\____|____/ 
                                                      
\033[0;0m'''
    greet1 = '''
    "HAI! SAYA \033[2;31;40mZETO\033[0;0m,
    SENANG MENYAPA ANDA SEKARANG :)
    
    \033[2;31;40m"AULIA"\033[0;0m ADALAH PROGRAM BELAJAR SEDERHANA
    UNTUK DAPAT MEMAHAMI DAN MENCARI SOLUSI
    DARI SETIAP PERTANYAAN PADA SOAL MATEMATIKA SEKOLAH.
    
    PROGRAM INI DIBUAT OLEH DIRI SAYA SENDIRI,
    DENGAN PENGETAHUAN SEADANYA, DAN MINAT SAYA.
    
    SEMOGA, DENGAN MENGGUNAKAN APLIKASI SEDERHANA INI, 
    DAPAT MEMBANTU ANDA UNTUK LEBIH MEMAHAMI MATEMATIKA
    DENGAN LEBIH BAIK, TERIMA KASIH.
    SELAMAT BELAJAR DAN BERSENANG-SENANG!
    SALAM DARI SAYA.
                                                "𝔃𝓮𝓽𝓸"'''
    for char in greet:
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in greet1:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n","_"*55)
def tujuan():
    os.system("clear")
    greet2 = '''
    BERAWAL DARI KEINGINAN UNTUK MEMBERIKAN SEBUAH HADIAH
    KEPADA ADIK SAYA TERCINTA, AGAR BISA MEMAHAMI DAN MENIKMATI
    SELURUH PROSES BELAJAR MATEMATIKA.
    TIDAK SEPERTI KAKAK'NYA INI, YANG BAHKAN TIDAK MENDAPATKAN
    KEMAMPUAN DAN PEMAHAMAN DARI MATERI SAAT DIBANGKU SEKOLAH.
    ALHASIL, MENJADI PRIBADI YANG BODOH DAN TIDAK MEMILIKI
    SEMANGAT HIDUP.
    
    SAYA RASA, DIA BISA MENJADI PRIBADI YANG LEBIH BAIK DARI KAKAK'NYA
    DAN BISA MEMILIKI MASA DEPAN YANG CEMERLANG.
    DENGAN ALAT SESERHANA INI, SAYA BELAJAR SECARA OTODIDAK,
    DENGAN SEGALA KEKURANGAN SAYA, SAYA MEMBUAT INI PERLAHAN
    DAN MENGULANG SEGALA PENGETAHUAN MATERI DARI AWAL.
    DEMI BISA MENDUKUNG BELAJAR AULIA.\n'''
    for char in greet2:
        time.sleep(0.045)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    import aulia
greetings()
print("\n")
time.sleep(1)
pilih = input("    KEMBALI KE MENU? 'Y/N': ")
if pilih == "Y":
    import aulia
elif pilih == "+":
    tujuan()
elif pilih == 'N':
    print("\nPROGRAM TELAH BERHENTI\n")
    time.sleep(1)
else:
    print("     MOHON MASUKAN INPUT ANDA!")
    time.sleep(0.5)
    import aulia