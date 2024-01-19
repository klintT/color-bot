import utilities.api.item_ids as item_ids
def file_to_dict(file_path):
    constants_dict = {}
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            parts = line.strip().split('=')
            if len(parts) == 2:
                variable_name = parts[0].strip()
                try:
                    constant_value = int(parts[1].strip())
                    constants_dict[variable_name] = constant_value
                except ValueError:
                    print(f"Error on line {line_number}: Unable to convert constant value to integer.")
            else:
                print(f"Error on line {line_number}: Line does not match expected format.")
    return constants_dict

def dict_to_file(constants_dict, output_file_path):
    with open(output_file_path, 'w') as output_file:
        output_file.write("{\n")
        for variable_name, constant_value in constants_dict.items():
            output_file.write(f'    "{variable_name}": {constant_value},\n')
        output_file.write("}\n")

# Replace 'path/to/your/constants_file.py' with the actual file path
file_path = './src/utilities/api/item_ids.py'
output_file_path = './src/utilities/api/item_ids_dict.py'  # Specify the output file path

# Convert file to dictionary
constants_dict = file_to_dict(file_path)

# Write dictionary to another file
dict_to_file(constants_dict, output_file_path)

# Print the resulting dictionary
print(f"Converted constants:\n{constants_dict}")
print(f"Constants written to: {output_file_path}")
