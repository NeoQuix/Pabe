#! /usr/bin/env python3

# Python helper Script 
# It just sets a breakpoint bevor main returns (before the leave)
# And gets the Solution String from the Stack
# The Addresses etc. were calculated with gdb (assembler dump from main)
# There was a Loop which XORT some Bytes (7 Iterations; <=6) and saved it as a local Variable on the Stack

# This script prints the Flag on stderr because despite the to_string Flags pwndbg and gdb still are printing some Lines
# The Solution script which captures all of the Output of this script then simply prints the Flag on Stddout  

import gdb
import sys

# Load File, set breakpoint, run programm, get the Solution Flag from the Stack
gdb.execute('file xor', to_string = True)
gdb.execute('b *(main + 73)', to_string = True)
gdb.execute('run', to_string = True)
solution = gdb.execute('x/-7b $rbp-5', to_string = True)
gdb.execute('c', to_string = True)

# Convert to String (Array of Chars, Offset will be always the same)
Byte1 = chr(int(solution[16:18]))
Byte2 = chr(int(solution[19:21]))
Byte3 = chr(int(solution[22:24]))
Byte4 = chr(int(solution[25:27]))
Byte5 = chr(int(solution[28:30]))
Byte6 = chr(int(solution[31:33]))
Byte7 = chr(int(solution[34:36]))

# Make a String + Print it
solution = Byte1 + Byte2 + Byte3 + Byte4 + Byte5 + Byte6 + Byte7
print(solution, file=sys.stderr)

# Exit GDB
gdb.execute('q', to_string = True)

