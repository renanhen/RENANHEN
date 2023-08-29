frase = "Hello world!"

print(frase[0:6])
print(frase[6:])
print(frase[0])

a = "Hello "
b = "world"
print(a + b)
c = "!"
print(a + b + c * 3)

nome = "Michele"
idade = 44
altura = 1.58
print("A %s tem %d anos e %.2f m de altura." % (nome, idade, altura))
print("A {} tem {} anos e {} m de altura.".format(nome, idade, altura))
print(f"A {nome} tem {idade} anos e {altura} m de altura.")

print(len(frase))
print(frase[0])
print(frase[1])

a = "Hello"
b = "world!"

print(a+" "+b )

print(frase[6:])

frase_lista = list(frase)
print(frase_lista)
frase_lista[5]=","
print(frase_lista)

frase ="".join(frase)
print(frase)
frase_inteira =" ".join(frase_lista)
print(frase_inteira)

print(frase.startswith("Hello"))
print(frase.endswith("world"))

print("Hello" in frase)
print("hello" in frase)
print(frase.count("a"))
print(frase.count("o"))
print(frase.count("Hello"))


print(frase.find('Hello'))
print(frase.find("mundo"))
print(frase.find("o"))
print(frase.find("e"))
print(frase.find("a"))
print(frase.find("Ola"))


print(frase.split())
print(frase.replace("world","mundo"))
print(frase)
frase = frase.replace("world","mundo")
print(frase)



