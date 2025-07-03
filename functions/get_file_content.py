import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    url = os.path.abspath(os.path.join(working_directory, file_path))
    if not url.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(url):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(url, "r") as f:  
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(url) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        print(f'Error: {e}')


           
schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file, constrained to the working directory. If the file is larger than 10000 characters, it truncates the content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory. If not provided, reads from the working directory itself.",
            ),
        },
    ),
)
