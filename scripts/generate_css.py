# -*- coding: utf-8 -*-
import json
import os
import io
from collections import OrderedDict
from size import format_size_variables

# Función para convertir un diccionario de variables en un archivo CSS
def convert_to_css(group_name, variables, file_name):
    def process_dict(prefix, d):
        css_lines = []
        for key, value in d.items():
            if isinstance(value, dict) and 'value' in value:
                variable_name = u"--pkst-{}-{}".format(prefix, key)
                css_lines.append(u"  {}: {};".format(variable_name, value['value']))
            elif isinstance(value, dict):
                sub_prefix = "{}-{}".format(prefix, key)
                css_lines.extend(process_dict(sub_prefix, value))
        return css_lines

    with io.open(file_name, 'w', encoding='utf-8') as css_file:
        css_file.write(u":root {\n")
        css_lines = process_dict(group_name, variables)
        css_file.write(u"\n".join(css_lines))
        css_file.write(u"\n}\n")

# Función para leer un archivo JSON manteniendo el orden
def read_json(file_path):
    try:
        with io.open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file, object_pairs_hook=OrderedDict)
            return data
    except Exception as e:
        return None

# Directorios base de las carpetas JSON
base_dir = os.path.join(os.path.dirname(__file__), '..')
json_variables_tokens_dir = os.path.join(base_dir, 'json', 'variables', 'tokens')
json_variables_foundations_dir = os.path.join(base_dir, 'json', 'variables', 'foundations')
json_variables_components_dir = os.path.join(base_dir, 'json', 'variables', 'components')

json_studio_template_dir = os.path.join(base_dir, 'json', 'studio', 'template')
json_studio_streaming_dir = os.path.join(base_dir, 'json', 'studio', 'streaming')

# Directorios base de salida CSS
css_foundations_dir = os.path.join(base_dir, 'css', 'variables', 'foundations')
css_tokens_dir = os.path.join(base_dir, 'css', 'variables', 'tokens')
css_components_dir = os.path.join(base_dir, 'css', 'variables', 'components')

css_studio_template_dir = os.path.join(base_dir, 'css', 'studio', 'variables', 'template')
css_studio_streaming_dir = os.path.join(base_dir, 'css', 'studio', 'variables', 'streaming')

# Crear las carpetas CSS si no existen
os.makedirs(css_foundations_dir, exist_ok=True)
os.makedirs(css_tokens_dir, exist_ok=True)
os.makedirs(css_components_dir, exist_ok=True)
os.makedirs(css_studio_template_dir, exist_ok=True)
os.makedirs(css_studio_streaming_dir, exist_ok=True)

# Función para procesar archivos en un directorio y generar CSS
def process_json_directory(json_dir, css_dir, group_processor=None):
    if not os.path.exists(json_dir):
        return

    for root, _, files in os.walk(json_dir):
        for file in files:
            if file.endswith('.json'):
                json_name = file.replace('.tokens.json', '').replace('_', '')
                file_path = os.path.join(root, file)
                
                data = read_json(file_path)
                if data is None:
                    continue

                # Aplicar procesamiento específico si es necesario
                if group_processor and json_name == 'size' and 'foundations' in json_dir:
                    data = group_processor(json_name, data)

                # Crear el archivo CSS correspondiente
                css_file_name = os.path.join(css_dir, f"_{json_name}.css")
                convert_to_css(json_name, data, css_file_name)

# Procesar las carpetas y generar los CSS
process_json_directory(json_variables_foundations_dir, css_foundations_dir, format_size_variables)
process_json_directory(json_variables_tokens_dir, css_tokens_dir)
process_json_directory(json_variables_components_dir, css_components_dir)
process_json_directory(json_studio_template_dir, css_studio_template_dir)
process_json_directory(json_studio_streaming_dir, css_studio_streaming_dir)

# Mensaje final de éxito
print("Todos los archivos CSS fueron generados exitosamente.")
