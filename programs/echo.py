# ------------------------------------------------------------------------------------
#   Echo.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------

def run(system, command_params, command_flags):
    return_text = ""
    for param in command_params:
        return_text += param + " "
    return return_text + "\n"
