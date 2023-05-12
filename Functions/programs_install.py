import subprocess

def install_program(program_path):
    subprocess.run(program_path, check=True)