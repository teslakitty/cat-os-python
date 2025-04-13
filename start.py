# cat-os runner
# This script is used to run the cat-os program
import subprocess
import os

# Get the directory where start.py is located (which is the root folder now)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to bios.py in the 'system' folder
bios_path = os.path.join(script_dir, "system", "bios.py")

# Run bios.py using subprocess
subprocess.run(["python", bios_path])