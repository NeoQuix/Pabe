Points: 8/8

stdout: >>> tracing eip = 0x30000 
   0:   31 c0                   xor    eax, eax
>>> tracing eip = 0x30002 
   0:   31 db                   xor    ebx, ebx
>>> tracing eip = 0x30004 
   0:   31 c9                   xor    ecx, ecx
>>> tracing eip = 0x30006 
   0:   b9 01 00 00 00          mov    ecx, 0x1
>>> tracing eip = 0x3000b 
   0:   a1 37 13 03 00          mov    eax, ds:0x31337
>>> READ Access! Memory: 0x31337, Size: 0x4
>>> tracing eip = 0x30010 
   0:   bb 42 00 00 00          mov    ebx, 0x42
>>> tracing eip = 0x30015 
   0:   01 d8                   add    eax, ebx
>>> tracing eip = 0x30017 
   0:   c1 e1 02                shl    ecx, 0x2
>>> tracing eip = 0x3001a 
   0:   01 c8                   add    eax, ecx
>>> tracing eip = 0x3001c 
   0:   50                      push   eax
>>> WRITE Access! Memory: 0x44ffc, Size: 0x4, Data: 0x137d
>>> tracing eip = 0x3001d 
   0:   53                      push   ebx
>>> WRITE Access! Memory: 0x44ff8, Size: 0x4, Data: 0x42
>>> tracing eip = 0x3001e 
   0:   59                      pop    ecx
>>> READ Access! Memory: 0x44ff8, Size: 0x4
>>> tracing eip = 0x3001f 
   0:   5a                      pop    edx
>>> READ Access! Memory: 0x44ffc, Size: 0x4
>>> tracing eip = 0x30020 
   0:   8d 04 01                lea    eax, [ecx+eax*1]
>>> tracing eip = 0x30023 
   0:   8d 1c 1a                lea    ebx, [edx+ebx*1]
eax = 0x13bf
ebx = 0x13bf
ecx = 0x42
edx = 0x137d


stderr: 

return code: 0

tutor notes:
