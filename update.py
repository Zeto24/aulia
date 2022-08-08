import os
import sys
import time
def update():
    os.system("rm -r aulia")
    os.system("git clone https://github.com/Zeto24/aulia.git")
    os.system("clear")
    print("\n","-"*32)
    print(" UPDATE/REINSTALL TOOLS BERHASIL!")
    time.sleep(0.015)
    os.system("cd aulia")
    os.system("python aulia.py")
    
for i in range(10):
    sys.stdout.write('•')
    sys.stdout.flush()
    time.sleep(1)
update()