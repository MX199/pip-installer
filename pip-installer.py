import sys
import os
packages = ["pkgutil", "subprocess", "tqdm"]
for package in packages:
    result = os.system(f"{sys.executable} -m pip install --force-reinstall {package}")
    code = result >> 8
    msg = f"Package {package} installed successfully." if code == 0 else f"Failed to install package {package}."
    print(msg)
    try:
        exec(f"import {package}")
        print(f"Package {package} is working.")
    except Exception as e:
        print(f"Package {package} is not working: {e}")
        exit()
word =("""\

████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░████░░░░▄▀░░░░█░░░░░░▄▀░░░░░░█
███░░▄▀░░███░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░██████████████░░▄▀░░███████░░▄▀░░█████
███░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░██████░░▄▀░░███████░░▄▀░░█████
███░░▄▀░░███░░▄▀░░██░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀░░███████░░▄▀░░█████
███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░██████░░▄▀░░███████░░▄▀░░█████
███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░██████████████░░▄▀░░███████░░▄▀░░█████
█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░████░░░░▄▀░░░░█████░░▄▀░░█████
█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀░░█████░░▄▀░░█████
█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░█████░░░░░░█████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████


                    """)
import time
for char in word:
    print(char, end="")
    sys.stdout.flush()
    time.sleep(0.001)
print()


modules = ["pkgutil", "subprocess", "tqdm"]
for module in modules:
    try:
        globals()[module] = __import__(module)
    except ImportError:
        print(f"Please install {module} module first.")
        exit()



import pkgutil
import subprocess
import tqdm
# edit packages here 
packages = ["numpy", "pandas", "matplotlib"]

def check_and_install(package):
    loader = pkgutil.find_loader(package)

    if loader is None:
        print(f"Package {package} is not installed. Trying to install it using pip.")
        try:
            result = subprocess.run(["pip", "install", package], capture_output=True)

            if result.returncode == 0:
                tqdm.tqdm.write(f"Package {package} installed successfully. \U0001F389")
                return True 
            else:
                print(f"Failed to install package {package}. Please check your internet connection and permissions.")
                return False 
        except Exception as e:
            print(f"An error occurred while trying to install package {package}: {e}")
            return False 
    else:
        tqdm.tqdm.write(f"Package {package} is already installed. \U0001F44D")
        return True 
results = [check_and_install(package) for package in tqdm.tqdm(packages)]
if not all(results):
    print("Some packages failed to install. Please try again.")
    exit()
else:
    print("All packages installed successfully.")
