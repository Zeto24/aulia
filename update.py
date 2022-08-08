import os
import sys
import time
for i in range(10):
    sys.stdout.write('•')
    sys.stdout.flush()
    time.sleep(1)
os.system("rm -rf toolus")
os.system("git clone https://github.com/Zeto24/aulia.git")
os.system("clear")
os.system("clear")
print("\n","-"*32)
print(" UPDATE/REINSTALL TOOLS BERHASIL!")
time.sleep(2)
os.system("cd toolus")
os.system("python aulia.py")