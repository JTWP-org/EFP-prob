u need to set 2 variables in the py 
```
# Base path
base_path = '/home/steam/pavlovserver/Pavlov/Saved/Config/'
rcon_ip = "127.0.0.1"  # Set server IP for RCON
```
<p>the rest it will find on its own 
running the script 
assuming u have a python env setup u just install and run with </p>
```python3 efp-prob.py```


<h2>install</h2>

```
pip install async-pavlov

pip install watchdog
```

```
python3 efp-prob.py
```

In the Main Block
what its doing ?

    Initialization of MyHandler:
        An instance of the MyHandler class is created with RCON details (rcon_ip, rcon_port, rcon_pass). These details are read from the RconSettings.txt file before entering the main block.

    Setting Up the Observer:
        The Observer from the watchdog library is initialized.
        The MyHandler instance is registered with the observer to handle events in the specified directory (monitor_path).

    Starting the Observer:
        The observer starts monitoring the directory. It runs continuously in a loop (while True loop), checking for file system events.

    Handling a KeyboardInterrupt:
        The script includes exception handling for a KeyboardInterrupt (usually triggered by pressing Ctrl+C). If such an interruption occurs, the observer stops.

Overall Script Flow

    Before the Main Block: The script reads the RCON configuration from the RconSettings.txt file. This is crucial as it sets up the necessary credentials for sending RCON commands later in the script.

    During File Creation (MyHandler's on_created Method):
        When a new file is detected in the monitored directory, the on_created method of the MyHandler instance is triggered.
        This method processes the new file (clears it and writes '0') and then uses asyncio.run to execute the send_rcon_command asynchronous function with the filename (minus the .txt extension).

    Async RCON Command (send_rcon_command Function):
        The send_rcon_command function, defined outside the main block, is an asynchronous function responsible for sending the RCON command using the PavlovRCON class.

Your script is set up so that the continuous monitoring and handling of new files are all controlled within the main block, following the best practices for Python script organization. This structure ensures that your monitoring and event handling only occur when the script is run directly, not when (or if) it's imported as a module in another Python script.
