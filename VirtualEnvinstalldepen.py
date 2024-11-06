import os
import subprocess
import sys

# Define the virtual environment directory and requirements file
venv_dir = 'rajveer'
requirements_file = 'requirement.txt'


# Function to create a virtual environment
def create_venv():
    print(f"Creating virtual environment in {venv_dir}...")
    subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])


# Function to install dependencies from requirements.txt
def install_dependencies():
    print("Installing dependencies...")
    pip_executable = os.path.join(venv_dir, 'bin', 'pip')  # For Linux/Mac
    if os.name == 'nt':  # Windows
        pip_executable = os.path.join(venv_dir, 'Scripts', 'pip.exe')

    subprocess.check_call([pip_executable, 'install', '-r', requirements_file])


def main():
    # Create the virtual environment
    create_venv()

    # Install dependencies
    install_dependencies()

    print("Setup complete!")


if __name__ == '__main__':
    main()
