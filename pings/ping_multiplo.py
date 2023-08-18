import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(f'verificando o ip: {ip}')
        print('-' * 60)
        os.system(f'ping -n 2 {ip}')
        print('-' * 60)
        time.sleep(3)
