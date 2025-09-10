from os.path import exists,dirname,abspath,join
from os import makedirs


def write_file(working_directory, file_path, content):
    rel_path=join(working_directory,file_path)
    working_path=abspath(working_directory)
    abs_file=abspath(rel_path)
    if not abs_file.startswith(working_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not exists(file_path):
        try:
            makedirs(file_path)
        except Exception:
            return f'Error: Could not make directory'
    with open(abs_file, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'