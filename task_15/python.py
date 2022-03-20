#!/usr/bin/env python3

# Ver. 1.0 ~ Spartak, Sean, Jakob

import os

flag = ""

gdb.execute('file extractme')
b_main = gdb.execute('b main', to_string=True) #

gdb.execute('r')

for i in reversed(range(0, 0x16)):
    command = 'watch $ecx ==' + str(hex(i))
    gdb.execute(command, to_string=True)
    gdb.execute('c')
    if(i == 0x15):
        continue
    eax = gdb.execute('info registers eax', to_string=True)
    eax = eax[35:].strip("\n")
    flag += chr(int(eax))

print(flag)

gdb.execute('q')
