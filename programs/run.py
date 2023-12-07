# ------------------------------------------------------------------------------------
#   run.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------
import os

def run(system, command_params, command_flags):
    if system.alias.WINDOWS:
        if "".join(command_params).replace(" ", "") == "":
            return "Error: No file specified.\n"
        else:
            cmdToRun = "start " + " ".join(command_params)
            cmd = " ".join(command_params)
            print("Running: " + cmd)
            os.system(cmdToRun)
            if "-s" not in command_flags:
                return f"Running {cmd}...\n"
            else:
                return ""
    else:
        try:
            if "".join(command_params).replace(" ", "") == "":
                return "Error: No file specified.\n"
            else:
                cmdToRun = "xdg-open " + " ".join(command_params)
                cmd = " ".join(command_params)
                print("Running: " + cmd)
                os.system(cmdToRun)
                if "-s" not in command_flags:
                    return f"Running {cmd}...\n"
                else:
                    return ""
        except:
            return "Error: Could not open file.\n"

