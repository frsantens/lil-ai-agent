import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(['python3', abs_file_path], capture_output=True, timeout=30, cwd=abs_working_dir, text=True)
        output = ''
        if result.stdout != '':
            output += f'STDOUT: {result.stdout}'
        if result.stderr != '':
            output += f'\nSTDERR: {result.stderr}'
        if result.stdout == '' and result.stderr == '':
            output = 'No output produced.'
        if result.returncode != 0:
            output += f'\nError: Process exited with code {result.returncode}'

        # if result.stdout == '' and result.stderr != '':
        #     output = f'STDERR: {result.stderr}'
        # elif result.stdout != '' and result.stderr == '':
        #     output = f'STDOUT: {result.stdout}'
        # elif result.stdout != '' and result.stderr != '':
        #     output = f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'
        # else:
        #     output = 'No output produced.'
        # if result.returncode != 0:
        #     output += f'\nError: Process exited with code {result.returncode}'
        return output
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
               
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the specified working directory. The file must be a valid Python script and is constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory. ",),
        },
    ),
)
