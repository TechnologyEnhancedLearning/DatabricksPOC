import sys
import os
from pathlib import Path

# Path.cwd() gets the folder where the notebook/script is currently executing.
# approach is so we can run in github, dabs, staging, individual workspace
current_dir = Path.cwd()
print(f"Current_dir: {current_dir}")

# Here we go up one level as that is the first shared parent
shared_parent_root = current_dir.parent.resolve()
print(f"shared_parent_root: {shared_parent_root}")


module_folder_path_from_shared_parent = "scratch-module-route"
# Now we go down to the module folder
module_path = (shared_parent_root / module_folder_path_from_shared_parent).resolve()
print(f"module_path: {module_path}")

# We check if it's already there to avoid duplicates if you run the cell twice.
if str(module_path) not in sys.path:
    sys.path.insert(0, str(module_path))

from py_module import *
result3 = py_module_function()
print(result3)