from os.path import abspath, join, isfile
from .config import CHARACTER_LIMIT
def get_file_content(working_directory, file_path):
    rel_path=join(working_directory,file_path)
    working_path=abspath(working_directory)
    abs_file=abspath(rel_path)
    print(abs_file)
    if not abs_file.startswith(working_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not isfile(abs_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    file_content = ''
    with open(abs_file) as f:
        file_content = f.read(CHARACTER_LIMIT)
    if len(file_content) ==  CHARACTER_LIMIT:
        file_content += "..."
    return file_content
    