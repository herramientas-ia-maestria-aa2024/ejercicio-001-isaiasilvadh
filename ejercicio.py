# Ubicación y nombre del archivo
nombre_archivo = "D:\\UTPL Maestría\\Herramientas IA\\ejercicio-001-isaiasilvadh\\informacion.txt"

try:
    # Abrir el archivo
    with open(nombre_archivo, 'r') as archivo:
        # Leer todas las líneas del archivo y mostrarlas
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea.rstrip())  # Imprimir cada línea
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
