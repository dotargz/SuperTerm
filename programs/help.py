# ------------------------------------------------------------------------------------
#   Help.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------

def run(system, command_params, command_flags):
    return_text = ""
    list_commands = ", ".join(system.programs)
    list_system_commands = ", ".join(system.system_commands)
    return_text += "Available commands: " + list_commands + "\n"
    return_text += "Available system commands: " + list_system_commands + "\n"
    return return_text

