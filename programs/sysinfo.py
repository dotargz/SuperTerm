# ------------------------------------------------------------------------------------
#   Sysinfo.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   List system information like license, version, as well as a list of
#   hardware on the system.
# ------------------------------------------------------------------------------------
import platform
import psutil

metadata = {
    "name": "sysinfo",
    "description": "Lists system information",
    "version": "1.0.0",
    "author": "dotargz",
    "dependencies": ['os'],
    "superterm_version": ">=2.0.0",
    "usage": "sysinfo <license|version|hardware>",
}

def run(system, command_params, command_flags):
    if len(command_params) == 0:
        return "Usage: " + metadata["usage"] + "\n"
    if command_params[0] == "license":
        return f"Copyright 2022 OneSpark LLC.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR A NY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
    if command_params[0] == "version":
        return f"{system.NAME} v{system.VERSION}\n"
    if command_params[0] == "hardware":
        return_text = ""
        return_text += f"System: {platform.system()}\n"
        return_text += f"Node: {platform.node()}\n"
        return_text += f"Release: {platform.release()}\n"
        return_text += f"Version: {platform.version()}\n"
        return_text += f"Machine: {platform.machine()}\n"
        return_text += f"Processor: {platform.processor()}\n"
        return_text += f"CPU Cores: {psutil.cpu_count()}\n"
        return_text += f"CPU Usage: {psutil.cpu_percent()}%\n"
        return_text += f"Memory Usage: {psutil.virtual_memory().percent}%\n"
        return_text += f"Swap Usage: {psutil.swap_memory().percent}%\n"
        return_text += f"Disk Usage: {psutil.disk_usage('/').percent}%\n"
        return return_text
    else:
        return "Error: Invalid parameter(s).\n"
