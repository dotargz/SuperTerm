# ------------------------------------------------------------------------------------
#   Time.py for SuperTerm
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
        current_time = now.strftime("%H:%M:%S") # uses a combination of real time and random for the nanoseconds
        formated_time = current_time + '.' + str(random.randrange(0,59)) # real nanoseconds would likely be offset anyways
        return_text += f"The current time is: {formated_time}\n"
    except PermissionError:
        return_text += "Error: ICMP Permission denied.\n"
    return return_text
