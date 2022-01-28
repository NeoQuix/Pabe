# Python helper Script 

import gdb

# break on every function in the file 
gdb.execute('file traceme')
gdb.execute('rbreak', to_string = True)

gdb.execute("r")

# run continue until we get an error (so the programm terminated)
while True:
    try: 
        gdb.execute("c")
    except: 
        break

gdb.execute('q')
