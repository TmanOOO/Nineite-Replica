import winreg

def enable_rdp():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
          r'System\CurrentControlSet\Control\Terminal Server', 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'fDenyTSConnections', 0, winreg.REG_DWORD, 0)
        key.Close()
        print("RDP enabled successfully.")
    except Exception as e:
        print("Error enabling RDP:", e)
