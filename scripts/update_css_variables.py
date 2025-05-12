import os
import re

# Directorios donde se encuentran los archivos CSS generados
foundations_directory = os.path.join(os.path.dirname(__file__), '..', 'css/variables/foundations/')
tokens_directory = os.path.join(os.path.dirname(__file__), '..', 'css/variables/tokens/')
components_directory = os.path.join(os.path.dirname(__file__), '..', 'css/variables/components/')
studio_template_directory = os.path.join(os.path.dirname(__file__), '..', 'css/studio/variables/template/')
studio_streaming_directory = os.path.join(os.path.dirname(__file__), '..', 'css/studio/variables/streaming/')

# Función para reemplazar referencias de variables en el contenido CSS
def replace_references_in_css(content):
    def replace_match(match):
        var_name = match.group(1)
        return f'var(--pkst-{var_name.replace(".", "-")})'
    
    # Encuentra la posición de apertura de :root {
    root_start = content.find(':root {')
    if root_start != -1:
        # Encuentra la posición del primer cierre de llaves después de :root
        root_end = content.find('}', root_start)
        if root_end != -1:
            # Separa el contenido en :root y el resto
            content_prefix = content[:root_start + len(':root {')]
            content_suffix = content[root_start + len(':root {'):]
            
            # Reemplaza las referencias de variables dentro del contenido
            content_suffix = re.sub(r'\{([^\}]+)\}', replace_match, content_suffix)
            
            return content_prefix + content_suffix
    return content

# Función para procesar archivos CSS en un directorio
def process_css_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.css') and filename not in ['color.css', 'size.css']:
            css_path = os.path.join(directory, filename)
            with open(css_path, 'r') as file:
                content = file.read()
            
            # Reemplazar las referencias de variables
            updated_content = replace_references_in_css(content)
            
            # Guardar el contenido actualizado en el mismo archivo
            with open(css_path, 'w') as file:
                file.write(updated_content)

# Procesar archivos CSS en los directorios de variables y componentes
process_css_files(foundations_directory)
process_css_files(tokens_directory)
process_css_files(components_directory)
process_css_files(studio_template_directory)
process_css_files(studio_streaming_directory)

print("Archivos CSS actualizados correctamente.")
