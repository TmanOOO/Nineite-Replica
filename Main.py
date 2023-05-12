import os

from Functions.files_install import download_file
from Functions.programs_install import install_program

def main():
    # List of programs to install
    programs = [
        {
            'name': 'Firefox',
            'url': 'https://download.mozilla.org/?product=firefox-latest&os=win&lang=en-US',
            'filename': 'firefox_installer.exe'
        },
        {
            'name': 'Java',
            'url': 'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=243743_61ae65e088624f5aaa0b1d2d801acb16',
            'filename': 'java_installer.exe'
        },
        {
            'name': 'Office 365',
            'url': 'https://go.microsoft.com/fwlink/p/?Hash=O%2BXDvVQz6TvuyfU3uLpp8pGg7y1uvn%2F6qjjlc0tyudDM5a%2FmMKzCNVv6gJAZwRlTGAWgsr4N6tGZjgCTYHDeWg%3D%3D&prod=O365ProPlusRetail&correlationGuid=b4aad2c1-09df-48ab-b9aa-5763efdcbd9d',
            'filename': 'office355_installer.exe'
        },
        {
            'name': 'TeamViewer15',
            'url': 'https://download.teamviewer.com/download/TeamViewer_Setup.exe',
            'filename': 'teamviewer15_installer.exe'
        },
        {
            'name': 'Google Chrome',
            'url': 'https://dl.google.com/chrome/install/standalone/GoogleChromeStandaloneEnterprise64.msi',
            'filename': 'googlechrome_installer.exe'
        },
        {
            'name': 'Adobe Acrobat',
            'url': 'https://get.adobe.com/reader/enterprise/',
            'filename': 'acrobat_installer.exe'
        }
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
    main()
