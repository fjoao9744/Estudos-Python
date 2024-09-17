#guanabra

temp = []
princ = []

while True:
    temp.append(str(input("nome: ")))
    temp.append(float(input("peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]


    princ.append(temp[:])

    temp.clear()
    resp = str(input("Quer continuar?[S/N] "))

    if resp in "nN":
        break

print(princ)
print(f"você cadastrou {len(princ)} pessoas")
print(f"o maior peso foi de {mai}Kg. Peso de ", end='')
for p in princ:
    if p[1] == mai:
        print(f"{p[0]}", end="")
print(f"o menor peso foi de {men}Kg. Peso de ", end='')
for p in princ:
    if p[1] == men:
        print(f"{p[0]}", end="")


