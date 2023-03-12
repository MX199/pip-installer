import sys
import os
import pkg_resources
packages = ["tqdm","requests"]
for package in packages:
    if pkg_resources.get_distribution(package):
        print(f"{package} already installed.")
        continue # added this line
    result = os.system(f"{sys.executable} -m pip install --ignore-installed {package} -q")
    if result != 0:
        print(f"Failed to install {package}.")
        break
    try:
        __import__(package)
        print(f"{package} OK")
    except Exception as e:
        print(f"Failed to import {package}: {e}")
        break
import sys
import time
import tqdm
import pkgutil
import subprocess
import importlib
import requests
import logging
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
for char in word:
    print(char, end="")
    sys.stdout.flush()
    time.sleep(0.001)
print()


modules = ["pkgutil", "subprocess", "tqdm","requests","logging"]
for module in modules:
    try:
        globals()[module] = __import__(module)
    except ImportError:
        print(f"Please install {module} module first.")
        exit()





































# Define a list of packages to test
packages = ["numpy", "pandas"]
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
def check_internet_connection():
    try:
        response = requests.get("https://www.google.com")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

if check_internet_connection():
    # Run pip commands
    pass
else:
    # Handle connection error
    logging.error("No internet connection. Please check your connection and try again.")
def get_latest_version(package):
    url = f"https://pypi.org/pypi/{package}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["info"]["version"]
    else:
        logging.warning(f"Failed to retrieve latest version for package {package}.")
        return None
# Define a function to ask for user confirmation
def confirm(message):
    answer = input(message + " (y/n): ")
    return answer.lower() == "y"
# Define a function to uninstall a package using pip
def uninstall(package):
    if not check_internet_connection():
        logging.error("No internet connection. Please check your connection and try again.")
        return False
    try:
        result = subprocess.run(["pip", "uninstall", "-y", package], capture_output=True)
        if result.returncode == 0:
            tqdm.tqdm.write(f"Package {package} uninstalled successfully. \U0001F389")
            return True
        else:
            # Check if the package is already uninstalled by looking for the message "WARNING: Skipping" in the output
            output = result.stdout.decode("utf-8")
            if f"WARNING: Skipping {package}" in output:
                tqdm.tqdm.write(f"Package {package} was already uninstalled. \U0001F44D")
                return True
            else:
                logging.warning(f"Failed to uninstall package {package}. Please check your internet connection and permissions.")
                return False
    except Exception as e:
        logging.error(f"An error occurred while trying to uninstall package {package}: {e}")
        return False
def check_and_install(package):
    loader = pkgutil.find_loader(package)
    if loader is None:
        # Get latest version
        version = get_latest_version(package)
        if version is not None:
            if not check_internet_connection():
                logging.error("No internet connection. Please check your connection and try again.")
                return False
            logging.info(f"Package {package} is not installed. Trying to install version {version} using pip.")
            try:
                result = subprocess.run(["pip", "install", f"{package}=={version}"], capture_output=True)
                if result.returncode == 0:
                    tqdm.tqdm.write(f"Package {package} version {version} installed successfully. \U0001F389")
                    return True
                else:
                    logging.warning(f"Failed to install package {package}. Please check your internet connection and permissions.")
                    return False
            except Exception as e:
                logging.error(f"An error occurred while trying to install package {package}: {e}")
                return False
    else:
        # Check if installed version is up-to-date
        installed_package = importlib.import_module(package)
        installed_version = installed_package.__version__

        # Get latest version
        latest_version = get_latest_version(package)

        if latest_version is not None and installed_version != latest_version:
            if not check_internet_connection():
                logging.error("No internet connection. Please check your connection and try again.")
                return False
            logging.info(f"Package {package} is not up-to-date. Trying to update to version {latest_version} using pip.")
            try:
                result = subprocess.run(["pip", "install", "--upgrade", f"{package}=={latest_version}"],capture_output=True)
                if result.returncode == 0:
                    tqdm.tqdm.write(f"Package {package} updated to version {latest_version} successfully. \U0001F389")
                    return True
                else:
                    logging.warning(f"Failed to update package {package}. Please check your internet connection and permissions.")
                    return False
            except Exception as e:
                logging.error(f"An error occurred while trying to update package {package}: {e}")
                return False
        else:
            tqdm.tqdm.write(f"Package {package} is already up-to-date with version {installed_version}. \U0001F44D")
            return True
def choose_action():
    choice = input("To install press 1, to uninstall press 2: ")
    if choice == "1":
        return "install"
    elif choice == "2":
        return "uninstall"
    else:
        logging.warning("Invalid input. Please try again.")
        return choose_action()

# Ask for user confirmation before running the code

if confirm("Are you sure you want to run the code?"):
    # Ask for user choice of action
    action = choose_action()

    # Perform the action according to the user choice
    if action == "install":

        # Check and install each package in the list
        results = [check_and_install(package) for package in tqdm.tqdm(packages)]
        if not all(results):
            logging.warning("Some packages failed to install. Please try again.")
            exit()
        else:
            logging.info("All packages installed successfully.")

            # Test the packages' functions by importing them and printing their versions and attributes
            logging.info("Testing the packages' functions:")

            # Loop through each package in the list
        for package in packages:
            # Import the package using importlib and get its name and version attributes
            mod = importlib.import_module(package)
            name = getattr(mod, "__name__", None)
            version = getattr(mod, "__version__", None)

            # Print the name and version of the package
            logging.info(f"{name} version: {version}")

            # Ask for user confirmation before undoing the installation
        if confirm("Do you want to undo the installation?"):
            results = [uninstall(package) for package in tqdm.tqdm(packages)]
            if not all(results):
                logging.warning("Some packages failed to uninstall. Please try again.")
                exit()
            else:
                logging.info("All packages uninstalled successfully.")
    elif action == "uninstall":

        # Uninstall each package in the list without checking if they are installed or not (assuming they are)
        results = [uninstall(package) for package in tqdm.tqdm(packages)]
        if not all(results):
            logging.warning("Some packages failed to uninstall. Please try again.")
            exit()
        else:
            logging.info("All packages uninstalled successfully.")
else:
    print("Code execution aborted.")
