Points: 4/4

stdout: 

stderr: Traceback (most recent call last):
  File "/exercise/./solution", line 111, in <module>
    main()
  File "/exercise/./solution", line 79, in main
    libc = ELF("/usr/lib/libc.so.6", checksec=False) 
  File "/usr/local/lib/python3.9/dist-packages/pwnlib/elf/elf.py", line 215, in __init__
    self.file = open(path,'rb')
FileNotFoundError: [Errno 2] No such file or directory: '/usr/lib/libc.so.6'


return code: 1

tutor notes:
- please use the container to check you solution ;)
