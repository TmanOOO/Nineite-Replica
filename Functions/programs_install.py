import subprocess

def install_program(program_path):
    subprocess.run(f"{program_path} /S", check=True)