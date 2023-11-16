# ------------------------------------------------------------------------------------
#   Ping.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------
import pythonping

def run(system, command_params, command_flags):
    return_text = ""
    try:
        ping_list = pythonping.ping(
            command_params[0], verbose=True, size=2)
        for response in ping_list:
            return_text += f"{response}\n"
    except PermissionError:
        return_text += "Error: ICMP Permission denied.\n"
    except RuntimeError:
        return_text += f"Error: Could not find hostname '{command_params[0]}'.\n"
    except IndexError:
        return_text += "Error: No hostname specified.\n"
    return return_text
