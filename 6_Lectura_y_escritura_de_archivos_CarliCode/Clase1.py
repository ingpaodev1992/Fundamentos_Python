# Manejo de Archivos .TXT

def contar_palabras(Cuerpos_Celestes):
    with open(Cuerpos_Celestes, 'r') as archivo:
        contenido = archivo.read()
        palabras = contenido.split()  # Divide el texto en palabras
        print(f"El archivo tiene {len(palabras)} palabras.")

contar_palabras("Cuerpos_Celestes.txt")
