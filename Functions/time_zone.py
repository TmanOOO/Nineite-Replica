import subprocess

def set_timezone_sydney():
    # Call the 'tzutil' command to set the time zone to 'AUS Eastern Standard Time'
    subprocess.run(['tzutil', '/s', 'AUS Eastern Standard Time'], check=True)
