# Función para contar las ocurrencias exactas de '"Id"' en un archivo de texto
def contar_ids_con_comillas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            # Contar ocurrencias exactas de '"Id"'
            return contenido.count('"Inactivo":false')
    except Exception as e:
        return f"Error al leer el archivo: {e}"

# Ejemplo de uso
nombre_del_archivo = 'resultados_api.txt'
print("Cantidad de '\"Id\"' encontrados:", contar_ids_con_comillas(nombre_del_archivo))
