# -*- coding: utf-8 -*-
from collections import OrderedDict

def px_to_rem(px_value):
    rem_value = float(px_value) / 16
    return ("{:.4f}".format(rem_value)).rstrip('0').rstrip('.') + "rem"

def format_size_variables(group_name, variables):
    formatted_variables = OrderedDict()
    for key, value in variables.items():
        if isinstance(value, dict) and 'value' in value:
            px_value = value['value']
            if isinstance(px_value, (int, float)):  # Verifica si el valor es un número
                formatted_variables[key] = {
                    'value': px_to_rem(px_value)
                }
        elif isinstance(value, dict):
            formatted_subvariables = OrderedDict()
            for sub_key, sub_value in value.items():
                if 'value' in sub_value:
                    px_value = sub_value['value']
                    if isinstance(px_value, (int, float)):  # Verifica si el valor es un número
                        formatted_subvariables[sub_key] = {
                            'value': px_to_rem(px_value)
                        }
            formatted_variables[key] = formatted_subvariables
    return formatted_variables
