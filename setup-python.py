# Activate virtual environment

import subprocess
import sys
import venv
import os

def install_requirements():
    try:
        # Running pip install command for the requirements.txt file
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("All packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")

def create_virtual_environment(env_name):
    """
    Create a virtual environment with the specified name in the current directory.
    """
    venv_path = os.path.join(os.getcwd(), env_name)
    
    # Create the virtual environment
    print(f"Creating virtual environment at {venv_path}...")
    venv.create(venv_path, with_pip=True)
    print("Virtual environment created successfully.")
    
    # Path to the pip executable inside the virtual environment
    if os.name == 'nt':
        pip_executable = os.path.join(venv_path, 'Scripts', 'pip.exe')
    else:
        pip_executable = os.path.join(venv_path, 'bin', 'pip')

    return pip_executable

def install_requirements(pip_executable):
    try:
        # Running pip install command for the requirements.txt file
        print(f"Installing packages using {pip_executable}...")
        subprocess.check_call([pip_executable, 'install', '-r', 'requirements.txt'])
        print("All packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")

def add_to_gitignore(venv_name):
    gitignore_path = ".gitignore"
    new_entry = f"{venv_name}/\n"
    
    # Check if .gitignore file exists, create it if not
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w') as f:
            f.write(new_entry)
        print(f"Created .gitignore and added {venv_name}/ to it.")
    else:
        # Read the existing .gitignore file
        with open(gitignore_path, 'r') as f:
            lines = f.readlines()
        
        # Add the new entry if it's not already present
        if new_entry not in lines:
            with open(gitignore_path, 'a') as f:
                f.write(new_entry)
            print(f"Added {venv_name}/ to .gitignore.")
        else:
            print(f"{venv_name}/ is already in .gitignore.")

if __name__ == "__main__":
    env_name = "myenv"  # Change the environment name if needed
    pip_executable = create_virtual_environment(env_name)
    install_requirements(pip_executable)
    add_to_gitignore(env_name)
