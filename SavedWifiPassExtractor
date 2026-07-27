import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = data.decode('utf-8').split('\n')
wifi_names = []
for profile in data:


    if "All User Profile" in profile:
        profile = profile.split(":")

        profile = profile[1]
        profile = profile[1:-1]

        wifi_names.append(profile)
print("{:<20}|  {:}\n".format('Wifi Names', 'Password'))
for name in wifi_names:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', name, 'key=clear'])
    data = data.decode('utf-8').split('\n')
    passwords = []
    for passw in data:
        if "Key Content" in passw:
            password = passw.split(":")

            password = password[1]
            password = password[1:-1]

            passwords.append(password)

    try:
        # return Wifi name & Password
        print("{:<20}|  {:}".format(name,passwords[0]))
    except IndexError:
        print("{:<20}|  {:}".format(name, ""))
