import os
import subprocess

def client_specific_installs(programs):
    for program in programs:
        # Check if the installer file exists
        if not os.path.exists(program['filename']):
            print(f"{program['name']} installer not found in {os.getcwd()}")
            continue

        # Run the installer silently
        print(f"Installing {program['name']}...")
        result = subprocess.run([program['filename'], '/S'], capture_output=True)

        # Check the output for errors
        if result.returncode != 0:
            print(f"Error installing {program['name']}:")
            print(result.stderr.decode('utf-8'))
        else:
            print(f"{program['name']} installed successfully!")

programs = [
    {'name': 'Program 1', 'url': 'http://url-to-program1.com', 'filename': 'program1.exe'},
    {'name': 'Program 2', 'url': 'http://url-to-program2.com', 'filename': 'program2.exe'},
    {'name': 'Program 3', 'url': 'http://url-to-program3.com', 'filename': 'program3.exe'}
]

# Install client-specific programs
client_specific_installs(programs)
