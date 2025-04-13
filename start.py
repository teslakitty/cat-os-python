import subprocess
import os

# Get the directory where start.py is located (which is the root folder now)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to bios.py in the 'system' folder
bios_path = os.path.join(script_dir, "system", "bios.py")

# Run bios.py using subprocess - TRY USING python3 here!
subprocess.run(["python3", bios_path])