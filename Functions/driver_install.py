import psutil
import subprocess

# define dictionary of VID/DID values and their corresponding driver filenames
driver_dict = {
    "10EC&DEV_8168": "Realtek_LAN_Driver.exe",
    "8086&DEV_1E22": "Intel_USB3_Driver.exe",
    # add more VID/DID keys and filenames as needed
}

def get_device_info():
    """Returns a list of tuples containing device info: (device name, vendor ID, device ID)"""
    device_list = []
    for dev in psutil.disk_partitions(all=True):
        try:
            partitions = psutil._psplatform.win32._get_drive_partitions()
            for part in partitions:
                if part.drive == dev.device:
                    phy_disk = part.physicaldrive
                    device_name = phy_disk.caption.rstrip("\")
                    vendor_id, device_id = phy_disk.deviceid.split("&")
                    device_list.append((device_name, vendor_id, device_id))
        except Exception:
            continue
    return device_list

def install_driver(driver_filename):
    """Runs an executable install file specified by 'driver_filename' with silent option."""
    subprocess.run([driver_filename, "/quiet", "/norestart"], shell=True)

# main code
device_list = get_device_info()

for device in device_list:
    vendor_id, device_id = device[1], device[2]
    vid_did = f"{vendor_id}&DEV_{device_id}"
    if vid_did in driver_dict:
        driver_filename = driver_dict[vid_did]
        try:
            install_driver(driver_filename)
            print(f"Installed driver successfully for {device[0]}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing driver for {device[0]}: {e}")
    else:
        print(f"No driver found for {device[0]}")
