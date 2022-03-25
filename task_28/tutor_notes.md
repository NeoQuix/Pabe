Points: 6/8
stdout:
stderr: Traceback (most recent call last):
File "/exercise/./solution", line 94, in 
main()
File "/exercise/./solution", line 31, in main
libc = ELF(exe.libc.path, checksec=False)
AttributeError: 'NoneType' object has no attribute 'path'
return code: 1
tutor notes:

General idea seems to be correct

Error in the init portion for libc
The while and for loops seem unecessary complicated