# Tarea: Trabajo con Archivos de Texto
# Lenguaje: Python

# 1. ESCRITURA DE ARCHIVO DE TEXTO:

# Abrimos o creamos 'my_notes.txt' en modo de escritura ('w'). 
# 'with open' asegura que el archivo se cierre correctamente.
with open('my_notes.txt', 'w', encoding='utf-8') as archivo:
    
    # Escribimos al menos tres líneas de notas personales.
    archivo.write("Nota 1: Hoy me concentraré en practicar las estructuras de control.\n")
    archivo.write("Nota 2: El manejo de archivos en Python es más sencillo de lo que pensé.\n")
    archivo.write("Nota 3: Revisar mañana el concepto de 'encoding' (UTF-8) para caracteres especiales.\n")
    
    print("--- 1. Escritura completada: 'my_notes.txt' creado/actualizado. ---")


# 2. LECTURA DE ARCHIVO DE TEXTO:

# Abrimos el archivo 'my_notes.txt' en modo de lectura ('r').
with open('my_notes.txt', 'r', encoding='utf-8') as archivo:
    
    print("\n--- 2. Lectura del Contenido de 'my_notes.txt' ---")
    
    # Leemos el contenido del archivo línea por línea usando un bucle 'for'.
    
    contador_lineas = 1
    for linea in archivo:
        # Mostramos en la consola cada línea leída. 
        # Usamos '.strip()' para quitar el salto de línea (\n) extra.
        print(f"Línea {contador_lineas}: {linea.strip()}")
        contador_lineas += 1

    print("--- 2. Lectura completada. ---")


# 3. CIERRE DE ARCHIVOS:
# La estructura 'with open()' se encarga del cierre automático.
print("\n--- 3. Cierre de Archivos ---")
print("El archivo 'my_notes.txt' se ha cerrado de forma automática y segura.")