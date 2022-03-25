Points: 2/4
stdout:
stderr: Killed after timeout!
return code: 127
tutor notes:

hardcoding offsets may work but it would have been more comfortable to use:

find_gadget("pop rax; ret", libc)


offset seems to be wrong
why big endian for the cookie?
when you do pop_rdi in the payload it should be a pointer to "command" not "command" itself
general idea seems to be correct with a bunch of mistakes plus no docs