####################################
# ~~~ Created by: Mahdi Zafari ~~~ #
####################################

import subprocess
import re

def get_wifi_profiles():
    profiles_output = subprocess.check_output('netsh wlan show profiles', shell=True).decode('utf-8')
    profiles = re.findall(r'All User Profile\s*:\s*(.*)', profiles_output)
    return profiles

def get_wifi_password(profile):
    try:
        profile_info_output = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True).decode('utf-8')
        password = re.findall(r'Key Content\s*:\s*(.*)', profile_info_output)
        return password[0] if password else None
    except subprocess.CalledProcessError:
        return None

def main():
    profiles = get_wifi_profiles()
    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    print("Wi-Fi Networks:")
    print("----------------------------------------------------")
    print("| {:<30} | {:<20} |".format("Network Name", "Password"))
    print("----------------------------------------------------")
    for profile in profiles:
        password = get_wifi_password(profile)
        print("| {:<30} | {:<20} |".format(profile.strip(), password.strip() if password else "No password found"))
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()
