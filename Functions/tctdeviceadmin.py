import subprocess

def add_admin_user_silent(username, password):
    # run net user command as Administrator to create new user with administrative privileges
    try:
        subprocess.run(["net", "user", username, password, "/add", "/comment:'Created by installer'", "/expires:never", "/passwordchg:no", "/fullname:'New User'", f"/homedir:C:\Users\{username}", "/usercomment:''", "/scriptpath:''", f"/profilepath:C:\Users\{username}\AppData\Roaming'", f"/basepath:C:\Users\{username}\Documents", "/logonpasswordchg:no", "/times:all", "/countrycode:0", "/workstations:''", "/office:''", "/pubkeyoption:0", "/randompwd:No",'/silent'], check=True, shell=True)
        # adds the created user to local administrators group
        subprocess.run(["net", "localgroup", "Administrators", username, "/add",'/silent'], check=True, shell=True)
        print(f"User {username} created successfully with administrative privileges!")
    except subprocess.CalledProcessError as e:
        print(f"Error while creating user: {e}")
