# Abrir el archivo en modo escritura ("w")
con open("my_notes.txt", "w") como archivo:
# Escribir tres líneas de notas
archivo.write("*Primera línea:* Esta es una nota sobre mi día en mi ciudad de Puyo.\n")
archivo.write("*Segunda línea:* Tengo una reunión de clases todos los sabados.\n")
archivo.write("*Tercera línea:* No me debo olvidar de hacer mis trabajos de la Universidad.\n")

# Mensaje de confirmación
print("¡Notas escritas correctamente en el archivo my_notes.txt!")

# Abrir el archivo en modo lectura ("r")
con open("my_notes.txt", "r") como archivo:

# Leer cada línea del archivo
linea = archivo.readline()

# Recorrer las líneas y mostrarlas en la consola.
mientras linea:
print(linea.strip()) # Eliminar espacios en blanco al final
linea = archivo.readline()

# Mensaje de confirmación
print("¡¡Contenido del archivo leído correctamente!")
# El archivo se cerrará automáticamente al salir del bloque 'with'