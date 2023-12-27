import time
import os
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pavlov import PavlovRCON
from cfg import rcon_ip, serverlocation


class MyHandler(FileSystemEventHandler):
    def __init__(self, rcon_ip, rcon_port, rcon_pass):
        self.rcon_ip = rcon_ip
        self.rcon_port = rcon_port
        self.rcon_pass = rcon_pass

    def on_created(self, event):
        if event.is_directory:
            return
        else:
            file_path = event.src_path
            filename = os.path.basename(file_path)
            filename_without_extension = os.path.splitext(filename)[0]
            print(f'New file created: {file_path}, filename: {filename_without_extension}')
            
            with open(file_path, 'w') as file:
                file.write('0')

            asyncio.run(send_rcon_command(filename_without_extension, self.rcon_ip, self.rcon_port, self.rcon_pass))

async def send_rcon_command(filename, rcon_ip, rcon_port, rcon_pass):
    pavlov = PavlovRCON(rcon_ip, rcon_port, rcon_pass)
    data = await pavlov.send(f"GiveCash {filename}")
    print(data)



# Base path
base_path = f'{serverlocation}/Pavlov/Saved/Config/'

# Construct the specific paths
monitor_path = os.path.join(base_path, 'ModSave/')
path_to_rcon_settings = os.path.join(base_path, 'RconSettings.txt')

# RCON server details

rcon_port = ""
rcon_pass = ""

# Read RconSettings file to get the port and password
with open(path_to_rcon_settings, 'r') as file:
    for line in file:
        if 'Password=' in line:
            rcon_pass = line.strip().split('=')[1]
        elif 'Port=' in line:
            rcon_port = line.strip().split('=')[1]

if __name__ == "__main__":
    event_handler = MyHandler(rcon_ip, rcon_port, rcon_pass)
    observer = Observer()
    observer.schedule(event_handler, monitor_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
