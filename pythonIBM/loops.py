# For loops

cuadros = ["red","yellow","green","purple","blue"]

print(cuadros)

for i in range(0,5):
    cuadros[i]= "white"

print(cuadros)


cuadros = ["red","yellow","green",]

for cuadro in cuadros:
    cuadro

print(cuadro)

cuadros = ["red","yellow","green",]

for i, cuadro in enumerate(cuadros):
    cuadro
    i

print(cuadro)
print(i)

# While loops

rectagulos=["orange","orange","purple","orange","blue"]
nuevos_rectangulos=[]

i=0
while(rectagulos[i]=="orange"):
    nuevos_rectangulos.append(rectagulos[i])
    i=i+1

print(nuevos_rectangulos)


for i in range(-4, 5):
    print(i)

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

for x in range(0, 3):
    print(x)

for x in ['A', 'B', 'C']:
    print(x + 'A')

for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)