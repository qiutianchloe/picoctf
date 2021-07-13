from Crypto.Util.number import inverse
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537
p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c, d, n)

print(hex(m)[2:-1].decode("hex"))