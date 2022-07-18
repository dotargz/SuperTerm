# SuperTerm
A simple, but feature-packed FUI (Fantasy User Interface) terminal built with only Python for maximum performance issues 

# How-to
To use SuperTerm, input commands into the main interface. You can view a list of available commands with the "help" command.

# Building & Compiling from source
To compile SuperTerm, do the following:
- Clone this repo using ``git clone https://github.com/dotargz/superterm.git``
- Create a VENV named ``super_env`` using ``python -m venv super_env``
- Activate the VENV using the script found in ``super_env/Scripts`` (bat or sh depending on OS)
- Install PyInstaller using ``pip install pyinstaller``
- Run ``pyinstaller main.spec``. 
- The executible *should* be in ``dist/``

## Disclaimers
- When running the program in any form (including the compiled version), pip is ran to insure every library is installed.
- When running the program by itself (the python file), [Cloudinary](https://cloudinary.com) is used to fetch needed assets and a warning is displayed to the user.

