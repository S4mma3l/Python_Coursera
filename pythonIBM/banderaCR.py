import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Aca se crea una figura y un eje.

fig, ax = plt.subplots()

# aca se definen los rectangulos y colores de la bandera
# se repite dependiendo las franjas de la badera, solo se deben de cambiar los colores

a = patches.Rectangle(
    (0, 1), width=19, height=2, facecolor="#002058", edgecolor="#002058"
)
b = patches.Rectangle(
    (0, 3), width=19, height=3, facecolor="#FFFFFF", edgecolor="#FFFFFF"
)
c = patches.Rectangle(
    (0, 5), width=19, height=2, facecolor="#EF3340", edgecolor="#EF3340"
)  # COLOR ROJO
d = patches.Rectangle(
    (0, 7), width=19, height=3, facecolor="#FFFFFF", edgecolor="#FFFFFF"
)  # COLOR BLANCO
e = patches.Rectangle(
    (0, 9), width=19, height=2, facecolor="#002058", edgecolor="#002058"
)  # COLOR AZUL

# Definir los rectangulos en el eje.

ax.add_patch(a)
ax.add_patch(b)
ax.add_patch(c)
ax.add_patch(d)
ax.add_patch(e)

# aca agregamos el escudo de la bandera

try:
    img = mpimg.imread(
        "pythonIBM\escudo_costa_rica.png"
    )  # debemos de verificar que la imagen se encuentre en esta ruta
    imagebox = OffsetImage(img, zoom=0.024)  # Aca definimos el tamano del escudo
    ab = AnnotationBbox(imagebox, (10, 6), frameon=False, pad=0)
    ax.add_artist(ab)
except FileNotFoundError:
    print("No se encuentra la imagen, verifica la ruta")

# Aca configuramos  aspecto y los limites del grafico

ax.set_aspect("equal")
ax.set_xlim(-1, 20)
ax.set_ylim(0, 12)

# con es siguiente codigo presentamos en pantalla

plt.show()
