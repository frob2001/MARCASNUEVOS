import json
import re

def count_ids_in_txt(file_path):
    id_count = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            
            # Usar regex para extraer el contenido del campo "result"
            match = re.search(r'result:\[(.*?)\]', line)
            if match:
                result_content = match.group(0)  # Obtener el contenido dentro de "result:[...]"
                result_content = result_content.replace('result:', '')  # Quitar el prefijo "result:"
                
                try:
                    data = json.loads(result_content)
                    if isinstance(data, list):
                        id_count += sum(1 for item in data if "Id" in item)
                except json.JSONDecodeError:
                    continue  # Saltar líneas que no son JSON válidos

    return id_count

# Ejemplo de uso
file_path = 'PASO1\\response_data.txt'
id_count = count_ids_in_txt(file_path)
print(f"El número de 'Id' en el archivo es: {id_count}")
