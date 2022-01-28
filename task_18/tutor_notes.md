Points: 0/4

stdout: 

stderr: 

return code: 0

tutor notes:
you could get at least one point if you write your exploitation roadmap here

Sure, but we do not need the point ;D 
A comment if our approach could have worked, would be great tho
(We didn't have much time for this sheet, so this task was a bit forgotten)

Comments to our approach: 
1. There is no Method which makes a shell + NX/ASLR is enabled, so we can't just simply inject some shellcode (or jump to an method which opens a shell for us)
2. The Binary prints some values/addr. from the Stack and has (obviously a buffer Overflow with gets in welcomeMe; found with ghidra)
3. So our idea was to perform a ret2glibc 
    - therefore we would a need to leak the addr. of a libc function to calculate the offset to system (maybe with __libc_start_main)
    - we would need to find a pointer to bin/sh for the argument of system ()
    - after that we would simply set the ret addr to system and put the argument (and a saved rbp) above it (like in the Basic Exploitation lecture)
4. But yeah... for 4 Points a bit too much work (task_20 gave 16, for much less work?)
5. Don't even know if it is possible to calculate the offset to system from libc base && how exactly we would find the bin/sh pointer (if possible, then with the same offset via libc base)