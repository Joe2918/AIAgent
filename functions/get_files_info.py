import os
def get_files_info(working_directory, directory="."):
    abs_full_path = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'
        
    list_dir = os.listdir(abs_full_path)
        
    try:
        files_info = []
        for dir in list_dir:
            filepath = os.path.join(abs_full_path, dir)
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            files_info.append(
                f"- {dir}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

def get_file_content(working_directory, file_path):
    abs_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        MAX_CHARS = 10000

        with open(abs_full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters].'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"

