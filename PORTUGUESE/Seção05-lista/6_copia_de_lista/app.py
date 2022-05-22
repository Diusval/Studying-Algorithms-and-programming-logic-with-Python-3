from ipaddress import NetmaskValueError


lista = [1, 2, 3]

nova_lista = []

nova_lista = lista

print(lista)
print(nova_lista)

nova_lista[0] = 1000

print(nova_lista)

print("Lista um")

print(lista)

lista[0] = 5000

print(nova_lista)