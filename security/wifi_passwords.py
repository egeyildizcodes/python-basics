import subprocess

data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode()
profiles = [line.split(":")[1].strip() for line in data.split("\n") if "All User Profile" in line]

for profile in profiles:
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode()
        password = [line.split(":")[1].strip() for line in result.split("\n") if "Key Content" in line]
        print(f"{profile}: {password[0] if password else 'No Password'}")
    except:
        pass
