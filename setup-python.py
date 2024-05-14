import os
import subprocess
import sys
import venv

def create_virtual_environment(env_name):
    """
    Create a virtual environment with the specified name in the current directory.
    """
    venv_path = os.path.join(os.getcwd(), env_name)
    
    # Create the virtual environment
    print(f"Creating virtual environment at {venv_path}...")
    venv.create(venv_path, with_pip=True)
    print("Virtual environment created successfully.")
    
    return venv_path

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

def generate_shell_script(env_path, requirements_file="requirements.txt"):
    """
    Generate a shell script to activate the virtual environment and install packages.
    """
    script_content = f"""
#!/bin/bash
source {env_path}/bin/activate
pip install -r {requirements_file}
"""
    script_path = "activate_and_install.sh"
    with open(script_path, 'w') as script_file:
        script_file.write(script_content)
    
    # Make the script executable
    os.chmod(script_path, 0o775)
    
    print(f"Generated shell script {script_path}.")
    return script_path

if __name__ == "__main__":
    env_name = "myenv"  # Change this to your virtual environment's name

    # Step 1: Create the virtual environment
    venv_path = create_virtual_environment(env_name)
    
    # Step 2: Add the virtual environment to .gitignore
    add_to_gitignore(env_name)
    
    # Step 3: Generate the shell script
    script_path = generate_shell_script(venv_path)
    
    # Step 4: Run the shell script
    print(f"Running shell script {script_path}...")
    subprocess.run(['bash', script_path], check=True)
    print("Virtual environment activated and packages installed.")
