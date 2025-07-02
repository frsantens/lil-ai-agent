def get_files_info(working_directory, directory=None):
    os.path.join(working_directory, directory)
    if working_directory is not in os.path.abspath(directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    for content in os.listdir(directory):
        content_str = f"- {content}: {os.path.getsize(os.path.join(directory, content))} bytes, is_dir={os.path.isdir(os.path.join(directory, content))}"
        print(content_str)