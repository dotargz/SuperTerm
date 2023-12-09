import random
def run(system, command_params, command_flags):
    return_text = ""
    # Needs this to take input for some reason
    for param in command_params:
        return_text += param
    # 
    if random.randint(1, 2) == 1:
        arg = "is true"
    else:
        arg = "is false"
    return (f"{return_text} {arg}")