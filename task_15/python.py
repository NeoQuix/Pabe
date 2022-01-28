#!/usr/bin/env python3

# Ver. 1.0 ~ Spartak, Sean, Jakob

import os

# create a list, that hold 21 items, set i to zero to start of
flag = [None] * 21
i = 0

gdb.execute('set confirm off') # sets confirmation off to quit without any additional prints
gdb.execute('set disable-randomization off')

gdb.execute('file extractme') # opens the xor file
b_main = gdb.execute('b main', to_string=True) # sets a breakpoint at main, we nee to do so since watchpoints can only be enabled when registers are already there

gdb.execute('commands\nsilent\nend\n') # sets the silent command for breakpoint 1 to be silent when breakpoint 1 is reached

gdb.execute('r') # runs the program

# creates a watchpoint to hold when ecx changes to 0x15, which is the length of our flag
# we need to continue the program and watch for 0x14 since at that point the first character is decrypted and inside of eax
w_15 = gdb.execute('watch $ecx == 0x15', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')

# creates a watchpoint to hold when ecx changes to 0x14. This happens until line 196 while counting values for ecx down to 0.
# we silence every watchpoint
# we continue and then reach the point where ecx == 0x14 and the other values respectively since ecx is the counting register
# and we count down to 0. That's when the last character got decrypted
# we now take a look at register eax, get that information into a string and then strip it so that only the integer value stays. After that we store it in flag[i]
# i gets increased since we want to write at the next position the next time
w_14 = gdb.execute('watch $ecx == 0x14', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_13 = gdb.execute('watch $ecx == 0x13', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_12 = gdb.execute('watch $ecx == 0x12', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_11 = gdb.execute('watch $ecx == 0x11', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_10 = gdb.execute('watch $ecx == 0x10', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_0f = gdb.execute('watch $ecx == 0xf', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_0e = gdb.execute('watch $ecx == 0xe', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_0d = gdb.execute('watch $ecx == 0xd', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_0c = gdb.execute('watch $ecx == 0xc', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_0b = gdb.execute('watch $ecx == 0xb', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_0a = gdb.execute('watch $ecx == 0xa', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_09 = gdb.execute('watch $ecx == 0x9', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_08 = gdb.execute('watch $ecx == 0x8', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_07 = gdb.execute('watch $ecx == 0x7', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_06 = gdb.execute('watch $ecx == 0x6', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_05 = gdb.execute('watch $ecx == 0x5', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_04 = gdb.execute('watch $ecx == 0x4', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_03 = gdb.execute('watch $ecx == 0x3', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_02 = gdb.execute('watch $ecx == 0x2', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_01 = gdb.execute('watch $ecx == 0x1', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax
i += 1

w_00 = gdb.execute('watch $ecx == 0x0', to_string=True)
gdb.execute('commands\nsilent\nend\n')
gdb.execute('c')
eax = gdb.execute('info registers eax', to_string=True)
eax = eax[35:].strip("\n")
flag[i] = eax


# create a string flag_str to be able to store the flag
flag_str = ""
# convert the flag from string values to integers and then to their ascii representation
for x in range(21):
    flag[x] = chr(int(flag[x]))
# join the string flag_str with the flag list and print the flag (on stderr, so the Mainprocess can catch it easily)
flag_str = "".join(flag)
print(flag_str, file = sys.stderr)

gdb.execute('q') # quit gdb since we already printed the flag
