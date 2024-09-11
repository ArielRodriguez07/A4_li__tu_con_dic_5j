print("Ejemplo de tuplas")
canciones=("Te amo","El NoaNoa","Amor eterno")

print(canciones)
y = list(canciones)
print(y)
y[1] = "La puerta negra"
x = tuple(y)
print(x)
print("Listado de elementos de la tupla canciones ciclo for")
for rodriguez in canciones:
    print(rodriguez)