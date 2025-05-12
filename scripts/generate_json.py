import os
import json

def remove_type_keys(data):
    """Función recursiva para eliminar todas las claves 'type' de un diccionario o lista."""
    if isinstance(data, dict):
        return {key: remove_type_keys(value) for key, value in data.items() if key != 'type'}
    elif isinstance(data, list):
        return [remove_type_keys(item) for item in data]
    else:
        return data

def save_group_to_file(group_name, group_data, output_folder):
    """Guarda cada grupo en un archivo separado dentro de la carpeta correspondiente."""
    output_file = f"{group_name}.tokens.json"
    output_path = os.path.join(output_folder, output_file)
    
    # Asegura que la carpeta exista antes de guardar el archivo
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(group_data, output_file, ensure_ascii=False, indent=4)

def generate_json():
    # Define the paths for input and output folders
    input_folder_path = os.path.join(os.path.dirname(__file__), '../figma-json')
    
    # Output folders dentro de la carpeta 'json'
    output_base_folder = os.path.join(os.path.dirname(__file__), '../json')
    output_folder_tokens = os.path.join(output_base_folder, 'variables')
    output_folder_studio_tokens = os.path.join(output_base_folder, 'studio')
    
    # Verifica si la carpeta figma-json existe
    if not os.path.exists(input_folder_path):
        print(f"Error: La carpeta {input_folder_path} no existe.")
        return
    
    # Itera sobre todos los archivos en la carpeta figma-json
    for filename in os.listdir(input_folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(input_folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

                # Remueve las claves 'type' de los datos
                cleaned_data = remove_type_keys(data)

                # Define la carpeta de salida dependiendo del archivo madre
                if filename == 'tokens.json':
                    parent_folder = os.path.join(output_folder_tokens, 'tokens')
                elif filename == 'foundations.json':
                    parent_folder = os.path.join(output_folder_tokens, 'foundations')
                elif filename == 'components.json':
                    parent_folder = os.path.join(output_folder_tokens, 'components')
                elif filename == 'studio-template.json':
                    parent_folder = os.path.join(output_folder_studio_tokens, 'template')
                elif filename == 'studio-streaming.json':
                    parent_folder = os.path.join(output_folder_studio_tokens, 'streaming')
                else:
                    continue  # Si el archivo no está en la lista esperada, lo ignoramos

                # Guarda cada grupo en un archivo separado dentro de su subcarpeta correspondiente
                for group_name, group_data in cleaned_data.items():
                    save_group_to_file(group_name, group_data, parent_folder)
    
    # Mensaje final indicando que todos los archivos fueron creados correctamente
    print("Todos los archivos JSON fueron creados correctamente.")

# Asegura que este script se pueda ejecutar directamente
if __name__ == "__main__":
    generate_json()
