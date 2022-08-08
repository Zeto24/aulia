import os
import sys
import time

def sd():
    os.system("clear")
    logo = '''\033[2;31;40m
    
  /$$$$$$  /$$$$$$$ 
 /$$__  $$| $$__  $$
| $$  \__/| $$  \ $$
|  $$$$$$ | $$  | $$
 \____  $$| $$  | $$
 /$$  \ $$| $$  | $$
|  $$$$$$/| $$$$$$$/
 \______/ |_______/ 
                    \033[0;0m'''
    for i in logo:
        time.sleep(0.004)
        sys.stdout.write(i)
        sys.stdout.flush()
        
    import sd
def smp():
    os.system("clear")
    logo = '''\033[6;31;40m     
                 
             !!! 
            !!:!!
            !:::!
            !:::!
            !:::!
            !:::!
            !:::!
            !:::!
            !:::!
            !:::!
            !!:!!
             !!! 
                 
             !!! 
            !!:!!
             !!! 
                 
 '''
    for i in logo:
        time.sleep(0.0015)
        sys.stdout.write(i)
        sys.stdout.flush()
    print("OPSI TIDAK ADA/BELUM RILIS\033[0;0m")
def smk():
    os.system("clear")
    logo = '''\033[2;31;40m     
                 
             !!! 
            !!:!!
            !:::!
            !:::!
            !:::!
            !:::!
            !:::!
            !:::!
            !:::!
            !:::!
            !!:!!
             !!! 
                 
             !!! 
            !!:!!
             !!! '''
    for i in logo:
        time.sleep(0.0015)
        sys.stdout.write(i)
        sys.stdout.flush()        
    print("OPSI TIDAK ADA/BELUM RILIS\033[0;0m")   
def menu():
    os.system("clear")
    logo = '''\033[2;31;40m
    
.##...##...####...######..##..##..........##...##..######..##..##..##..##.
.###.###..##..##....##....###.##..........###.###..##......###.##..##..##.
.##.#.##..######....##....##.###..........##.#.##..####....##.###..##..##.
.##...##..##..##....##....##..##..........##...##..##......##..##..##..##.
.##...##..##..##..######..##..##..........##...##..######..##..##...####..
..........................................................................\033[0;0m'''
    type = '''
    
[TINGKAT SEKOLAH]

1.SD  [BASIC]
2.SMP [INTERMEDIATE] \033[2;31;40m!OPSI INI KOSONG\033[0;0m
3.SMK [ADVANCED]     \033[2;31;40m!OPSI INI KOSONG\033[0;0m'''
    for char in logo:
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in type:
        time.sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    pilih = input("\n\nPILIH SATU OPSI: ")
    if pilih == "1":
        sd()
    elif pilih == "2":
        smp()
        pilih = input("\n KEMBALI? (enter) ")
        if pilih == "Y":
            os.system("clear")
            import menu
        else:
            os.system("clear")
            import menu
    elif pilih == "3":
        smk()
        pilih = input("\n KEMBALI? (enter) ")
        if pilih == "Y":
            os.system("clear")
            import menu
        else:
            os.system("clear")
            import menu
    else:
        print("MOHON MASUKAN INPUT ANDA!")
        time.sleep(0.1)
        os.system("clear")
        import menu
menu()