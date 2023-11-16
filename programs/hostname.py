# ------------------------------------------------------------------------------------
#   Hostname.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------
import socket as s

def run(system, command_params, command_flags):
    return_text = ""
    try:
        return_text += s.gethostname() + "\n"
    except PermissionError:
        return_text += "Error: ICMP Permission denied.\n"
    except RuntimeError:
        return_text += f"Error: Could not find hostname '{command_params[0]}'.\n"
    return return_text
