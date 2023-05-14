import os
from Functions.files_install import download_file
from Functions.programs_install import install_program

def client_installs():
    # List of programs to install
    programs = [
        {
            'name': 'Firefox',
            'url': 'https://download.mozilla.org/?product=firefox-latest&os=win&lang=en-US',
            'filename': 'firefox_installer.exe'
        },

    ]
    # Add more programs as needed
    

    # Create a directory to store the downloaded files
    download_dir = 'downloads'
    os.makedirs(download_dir, exist_ok=True)

    # Download and install each program
    for program in programs:
        print(f"Downloading {program['name']}...")
        download_path = os.path.join(download_dir, program['filename'])
        download_file(program['url'], download_path)

        print(f"Installing {program['name']}...")
        install_program(download_path)

        print(f"{program['name']} installed successfully.\n")

if __name__ == '__main__':
    client_installs()
