if command == "run" and WINDOWS == True:
    if "".join(command_params).replace(" ", "") == "":
        return_text = "Error: No file specified.\n"
    else:
        cmdToRun = "start " + " ".join(command_params)
        cmd = " ".join(command_params)
        print("Running: " + cmd)
        os.system(cmdToRun)
        if "-s" not in command_flags:
            return_text = f"Running {cmd}...\n"
        else:
            return_text = ""
elif command == "tkz":
    return_text = f"{str(self.advanced_tokenize(full_command))}\n"
