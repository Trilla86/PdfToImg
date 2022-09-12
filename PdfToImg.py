import sys
import fitz

# Creamos la lista con los parámetros recibidos.
ruta = sys.argv
# Eliminamos el primer argumento.
del ruta[0]

# Creamos la ruta del archivo si viene con espacios.
if len(ruta) > 1:
    rutaPdf = " ".join(ruta)
else:
    rutaPdf = ruta[0]

# Comprobamos que es un archivo de pdf.
if rutaPdf[-4:].lower() == ".pdf":
    rutaImg = rutaPdf[0:len(rutaPdf)-4] # Creamos la ruta de la imagen o imagenes dependiendo de las páginas del pdf.
    mat = fitz.Matrix(200 / 72, 200 / 72)
    doc = fitz.open(rutaPdf)
    for page in doc:
        pix = page.get_pixmap(matrix=mat)
        img_filename =  rutaImg + str(page.number) + ".jpg"
        pix.pil_save(img_filename, format="JPEG", dpi=(100,100))
else:
    print("No es un pdf.")

