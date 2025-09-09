from os.path import join,abspath,isdir,getsize
from os import listdir
def get_files_info(working_directory, directory="."):
    rel_path=join(working_directory,directory)
    work_path=abspath(working_directory)
    file_path=join(work_path,directory)
    if not abspath(rel_path).startswith(work_path):
        return f'Error: Cannot list"{directory}" as it is outside the permitted working directory'
    if not isdir(file_path):
        return f'Error: "{directory}" is not a directory'
    out_str = ''
    
    for file in listdir(file_path):
        out_str += f"- {file}: file_size= {getsize(join(file_path,file))} bytes, is_dir={isdir(join(file_path,file))}\n"
    
    return out_str
    
