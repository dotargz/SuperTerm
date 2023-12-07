# ------------------------------------------------------------------------------------
#   STenv.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------
import json

metadata = {
    "name": "stenv",
    "description": "Set, get, and delete environment variables.",
    "version": "1.0.0",
    "author": "dotargz",
    "dependencies": ['json'],
    "superterm_version": ">=2.0.0",
    "usage": "stenv <set|get|del|list> [key] [value]",
    "flags": {
        "--all": "Delete all environment variables when using 'del'",
    },
    "arguments": {
        "set": "Set an environment variable",
        "get": "Get an environment variable",
        "del": "Delete an environment variable",
        "list": "List all environment variables",
        "listcache": "List the cached environment variables for debugging",
    },
    "examples": [
        {
            "description": "Set environment variable 'test' to 'value'",
            "command": "stenv set test value",
        },
        {
            "description": "Get environment variable 'test'",
            "command": "stenv get test",
        },
    ],
    "license": "MIT",
    "repository": "https://github.com/dotargz/SuperTerm/",
    "Issues": "https://github.com/dotargz/SuperTerm/issues",
    "maintainers": [
        {
            "name": "dotargz",
            "email": "me@blueskye.dev",
        },
    ],
}

# This program is used to set, get, and delete environment variables.
def run(system, command_params, command_flags):
    return_text = ""
    if len(command_params) == 0:
        return_text = "Error: No parameter specified.\n"
    else:
        if command_params[0] == "set":
            if len(command_params) == 3:
                system.alias.set_env(command_params[1], command_params[2])
                return_text = f"Set environment variable '{command_params[1]}' to '{command_params[2]}'\n"
            else:
                return_text = "Error: Invalid syntax.\n"
        elif command_params[0] == "get":
            if len(command_params) == 2:
                env = system.alias.get_env(command_params[1])
                if env == None:
                    return_text = f"Error: Environment variable '{command_params[1]}' not found.\n"
                else:
                    return_text = f"Environment variable '{command_params[1]}' is set to '{env}'\n"
            else:
                return_text = "Error: Invalid syntax.\n"
        elif command_params[0] == "del":
            if len(command_params) == 2:
                env = system.alias.get_env(command_params[1])
                if env == None:
                    return_text = f"Error: Environment variable '{command_params[1]}' not found.\n"
                else:
                    system.alias.set_env(command_params[1], None, True)
                    return_text = f"Environment variable '{command_params[1]}' deleted.\n"
            elif len(command_flags) == 1:
                if command_flags[0] == "--all":
                    with open(system.alias.resource_path("assets/data/environment.json"), "w") as f:
                        json.dump({}, f)
                    return_text = "All environment variables deleted.\n"
            else:
                return_text = "Error: Invalid syntax.\n"
        elif command_params[0] == "list":
            try:
                with open(system.alias.resource_path("assets/data/environment.json"), "r") as f:
                    env = json.load(f)
                    for key in env:
                        return_text += f"{key}: {env[key]}\n"
            except Exception as e:
                return_text = "Error: Could not load environment variables.\n"
                return_text += f"Error Message: {e}\n"
        elif command_params[0] == "listcache":
            try:
                env = system.alias.env_cache
                for key in env:
                    return_text += f"{key}: {env[key]}\n"
            except Exception as e:
                return_text = "Error: Could not load environment variables.\n"
                return_text += f"Error Message: {e}\n"
        else:
            return_text = "Error: Invalid parameter.\n"
    return return_text
