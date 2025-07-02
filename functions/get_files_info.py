import os

def get_files_info(working_directory, directory=None):
    if directory is None:
        dir = working_directory
    else:
        dir = os.path.join(working_directory, directory)
    if not os.path.abspath(dir).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir):
        return f'Error: "{directory}" is not a directory'
    content_str = []
    for content in os.listdir(os.path.abspath(dir)):
        try:
            content_str.append(f"- {content}: file_size={os.path.getsize(os.path.join(dir, content))} bytes, is_dir={os.path.isdir(os.path.join(dir, content))}")
        except Exception as e:
            content_str.append(f"Error: {e}")
    return '\n'.join(content_str)

            
