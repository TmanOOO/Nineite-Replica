import subprocess


def uninstall_program(program_name):
    identifying_number = subprocess.check_output(f"wmic product where name='{program_name}' get IdentifyingNumber").strip().decode('utf-8').split("\n")[1]
    uninstall_command = f'start /wait msiexec /x "{{{identifying_number}}}" /qn'
    subprocess.call(uninstall_command, shell=True)

# List of program names to uninstall
# add in the ProgamA and so on
programs_to_remove = ["ProgramA", "ProgramB", "ProgramC"]

# Loop through each program and call the uninstall_program function with its name
for program_name in programs_to_remove:
    uninstall_program(program_name)