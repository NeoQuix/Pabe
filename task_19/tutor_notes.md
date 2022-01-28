Points: 8/8

stdout: 

stderr: Traceback (most recent call last):
  File "/exercise/./solution", line 72, in <module>
    main()
  File "/exercise/./solution", line 59, in main
    print(io.recv().decode('utf-8')[:-1])
  File "/usr/local/lib/python3.9/dist-packages/pwnlib/tubes/tube.py", line 105, in recv
    return self._recv(numb, timeout) or b''
  File "/usr/local/lib/python3.9/dist-packages/pwnlib/tubes/tube.py", line 183, in _recv
    if not self.buffer and not self._fillbuffer(timeout):
  File "/usr/local/lib/python3.9/dist-packages/pwnlib/tubes/tube.py", line 154, in _fillbuffer
    data = self.recv_raw(self.buffer.get_fill_size())
  File "/usr/local/lib/python3.9/dist-packages/pwnlib/tubes/process.py", line 727, in recv_raw
    raise EOFError
EOFError


return code: 1

tutor notes:
* Solution works in isolation container
* the 64-bit ABI does require that the stack is 16 byte aligned before any call instruction so that push might resolve that issue here
* Also if the compiler wants to be smart and sees that building up a stack frame can be optimized out it may do so
* Feel free to ask this particular question on Friday during the exercise session! It's a good one that might be of interest to others!
