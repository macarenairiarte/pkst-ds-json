import subprocess
import os

# Define the paths to the scripts
generate_jston_script = os.path.join(os.path.dirname(__file__), 'generate_json.py')
generate_css_script = os.path.join(os.path.dirname(__file__), 'generate_css.py')
update_css_variables_script = os.path.join(os.path.dirname(__file__), 'update_css_variables.py')
add_fallbacks_script = os.path.join(os.path.dirname(__file__), 'add_fallbacks.py')

# Run generate_json.py
subprocess.call(['python3', generate_jston_script])

# Run generate_css.py
subprocess.call(['python3', generate_css_script])

# Run update_css_variables.py
subprocess.call(['python3', update_css_variables_script])

# Run add_fallbacks.py
subprocess.call(['python3', add_fallbacks_script])

print("Todos los scripts se han ejecutado correctamente.")
