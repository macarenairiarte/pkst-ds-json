# -*- coding: utf-8 -*-

import os
import re

# Obtener la ruta absoluta del directorio donde está el script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Directorios donde se encuentran los archivos CSS generados
directories = [
    os.path.join(base_dir, '../css/variables/foundations/'),
    os.path.join(base_dir, '../css/variables/tokens/'),
    os.path.join(base_dir, '../css/variables/components/'),
    os.path.join(base_dir, '../css/studio/variables/template/'),
    os.path.join(base_dir, '../css/studio/variables/streaming/')
]

# Función para extraer y resolver el valor final de una variable CSS
def resolve_variable_value(variable_name, all_variables, seen_variables=None):
    if seen_variables is None:
        seen_variables = set()

    if variable_name in seen_variables:
        return "Circular reference detected"

    seen_variables.add(variable_name)

    if variable_name in all_variables:
        value = all_variables[variable_name]
        # Si el valor es otra variable, resolvemos recursivamente
        var_match = re.match(r'var\(--([\w\-]+)\)', value)
        if var_match:
            inner_var_name = var_match.group(1)
            return resolve_variable_value(inner_var_name, all_variables, seen_variables)
        else:
            return value.strip()
    return None

# Función para recopilar todas las variables CSS de todos los directorios
def collect_all_variables():
    all_variables = {}
    ordered_variables = []

    for directory in directories:
        for filename in os.listdir(directory):
            if filename.endswith('.css'):
                css_path = os.path.join(directory, filename)
                with open(css_path, 'r') as file:
                    content = file.read()
                    variables = re.findall(r'--([\w\-]+):\s*([^;]+);', content)
                    for var_name, var_value in variables:
                        # Evitar duplicación del prefijo pkst-
                        if var_name.startswith("pkst-pkst-"):
                            var_name = var_name.replace("pkst-pkst-", "pkst-")
                        ordered_variables.append((var_name, var_value))
                        all_variables[var_name] = var_value
    
    return all_variables, ordered_variables

# Recopilar todas las variables antes de resolver
all_variables, ordered_variables = collect_all_variables()

# Resolver los valores finales en el orden en que fueron encontrados
resolved_variables = []
for var_name, original_value in ordered_variables:
    final_value = resolve_variable_value(var_name, all_variables)
    resolved_variables.append((var_name, original_value, final_value))

# Aplicar los cambios directamente en los archivos CSS
for directory in directories:
    for filename in os.listdir(directory):
        if filename.endswith('.css'):
            css_path = os.path.join(directory, filename)
            with open(css_path, 'r') as file:
                content = file.read()
            
            # Reemplazar las variables con las nuevas declaraciones
            for var_name, original_value, final_value in resolved_variables:
                if re.match(r'var\(--([\w\-]+)\)', original_value):
                    referenced_var_name = re.match(r'var\(--([\w\-]+)\)', original_value).group(1)
                    replacement = '--{}: var(--{}, {});'.format(var_name, referenced_var_name, final_value)
                    content = re.sub(r'--{}:\s*[^;]+;'.format(re.escape(var_name)), replacement, content)
            
            # Guardar los cambios
            with open(css_path, 'w') as file:
                file.write(content)

print("Se han aplicado fallbacks a las variables CSS correctamente.")
