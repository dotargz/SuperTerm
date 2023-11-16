# ------------------------------------------------------------------------------------
#   Date.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------
import datetime

def run(system, command_params, command_flags):
    return_text = ""
    try:
        now = datetime.datetime.now()
        current_date = now.strftime("%a %m/%d/%y")
        return_text += f"The current date is: {current_date}\n"
    except PermissionError:
        return_text += "Error: ICMP Permission denied.\n"
    return return_text
