import os
import sys
import time

def kalkulator():
    os.system("clear")
    logo = '''\033[2;31;40m    
    _              _ ___ _  _ 
|/ |_||  |/ | ||  |_| | / \|_)
|\ | ||__|\ |_||__| | | \_/|\•
\033[0;0m'''
    for i in logo:
        time.sleep(0.0043)
        sys.stdout.write(i)
        sys.stdout.flush()
    print("_"*35)
    a = input("[INPUT SOAL] :\n-> ")
    print("_"*35)
    hsl = eval(a)
    time.sleep(0.1)
    print("\n[HASIL]\n->", a, "=\033[2;31;40m",hsl,"\033[0;0m")
    print("_"*35)
def info():
    os.system("clear")
    i = '''
    ____________________________________________________________________
    
                        \033[2;31;40m[INI HANYA INFORMASI TAMBAHAN]\033[0;0m
    ____________________________________________________________________
    URUTAN "\033[2;31;40mKaBaTaKu\033[0;0m" (Kali, Bagi, Tambah, Kurang). 
    Mengapa aturan tersebut diberi nama KaBaTaKu bukan "\033[2;31;40mTaKuKaBa" 
    (Tambah,Kurang, Kali, Bagi) ? 

    Untuk mengetahui penamaan tersebut, 
    hal ini berkaitan dengan aturan didalamnya, yaitu : 
    
    1. Jika dalam suatu persamaan/kalimat matematika terdapat 
        tambah dan kurang, 
        maka dikerjakan dari yang paling depan/kiri. 
    
    Contoh :
    
    \033[2;31;40m4+3-5=\033[0;0m
    
    Jawab :
    \033[2;31;40m
    (4+3)-5=
    7-5=2
    \033[0;0m
    2. Jika dalam suatu persamaan/kalimat matematika terdapat 
        tambah, kurang,kali atau bagi, 
        maka hitung dulu kali atau bagi, baru tambah dan kurang.
    
    Contoh :
   \033[2;31;40m 
    5+7x2-8=
    \033[0;0m
    Jawab :
    
    \033[2;31;40m5+(7x2)-8=
    (5+14)-8=
    19-8=11 (Benar)
    \033[0;0m
    Bukan,
    \033[2;31;40m
    5+7x2-8= 
    (5+7)x2-8=
    (12x2)-8= 
    24-8=16 (Salah)
    \033[0;0m
    3. Jika dalam suatu persamaan/kalimat matematika terdapat 
        tambah, kurang,kali, dan bagi, maka hitung kali atau bagi dulu 
        dengan menghitung yang paling depan/kiri, 
        lalu hitung tambah dan kurang.
    
    Contoh : 
    
    \033[2;31;40m8+6:2x3-7=\033[0;0m
    
    Jawab :
   \033[2;31;40m 
    8+(6:2)x3-7= 
    8+(3x3)-7=
    (8+9)-7=  
    17-7=10 (Benar)
    \033[0;0m
    Bukan ,
    \033[2;31;40m
    8+6:2x3-7= 
    8+6:(2x3)-7= 
    8+(6:6)-7=   
    (8+1)-7=   
    9-7=2 (Salah)
    \033[0;0m
    Atau bukan juga ,
    \033[2;31;40m
    8+6:2x3-7=    
    (8+6):2x3-7=
    (14:2)x3-7= 
    (7x3)-7= 
    10-7=3 (Salah)
    \033[0;0m
    Maka dari itu, aturan ini disebut "\033[2;31;40mKaBaTaKu\033[0;0m"  yaitu 
    Kali atau bagi dulu, baru tambah atau kurang.
    
    Lalu, bagaimana jika terdapat tanda kurung "\033[2;31;40m( )\033[0;0m" dalam 
    suatu persamaan/kalimat matematika ?
    
    4. Jika terdapat tanda kurung "\033[2;31;40m( )\033[0;0m" pada persamaan/kalimat matematika
        yang terdapat tambah, kurang, kali, dan bagi, 
        maka selesaikan yang berada di dalam kurung, lalu kali atau bagi 
        yang berada di luar tanda kurung, lalu yang terakhir tambah atau kurang.'''    
    for char in i:
        time.sleep(0.0015)
        sys.stdout.write(char)
        sys.stdout.flush()

os.system("clear")        
kalkulator()
pilih = input("\nKEMBALI? 'N/Y/I' : ")
if pilih == "N":
    import kalk
elif pilih == "Y":
    import sd
elif pilih == "I":
    info()
    pilih1 = input("\n\nKEMBALI? (enter) ")
    if pilih1 == "Y":
        import kalk
    else:
        import kalk
else:
    print("\nMOHON MASUKAN INPUT ANDA!")
    time.sleep(0.1)
    import kalk