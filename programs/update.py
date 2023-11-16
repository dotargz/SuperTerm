# ------------------------------------------------------------------------------------
#   Update.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------
import requests
import json

def run(system, command_params, command_flags):
    if "--confirm" in command_flags:
        # force update check
        system.alias.set_env("update_warned", "true")
    elif "--unconfirm" in command_flags:
        # reset update check
        system.alias.set_env("update_warned", "false")
    # if it is the first time running the command, warn the user of the network request
    if system.alias.get_env("update_warned", "false").lower() == "false":
        return_text = "Warning: This command will make a request to the main SuperTerm API to check for updates.\n"
        return_text += "This request will include your current version of SuperTerm.\n"
        return_text += "The next time you run this command, this warning will not be displayed and the request will be made.\n"
        system.alias.set_env("update_warned", "true")
    else:
        try:
            if "--test" in command_flags:
                r = requests.get(
                    "https://one.npkn.net/superterm-update/")
            else:
                r = requests.get(
                    "https://one.npkn.net/superterm-update/?client=terminal&version=" + system.VERSION.replace("α", "").replace("β", ""))
            # convert from json to dict
            res = json.loads(r.text)
            return_text = f"Version Status:\n"
            return_text += f"   - Latest Version: {res['update']['latest_version']}\n"
            return_text += f"   - Current Version: {system.VERSION}\n"
            return_text += f"Update Status:\n"

            if res['update']['needs_update'] == "true":
                version_diff = res['update']['version_diff'].split(".")
                if int(version_diff[0]) > 0:
                    return_text += f"   - Major update available: {res['update']['latest_version']}\n"
                elif int(version_diff[1]) > 0:
                    return_text += f"   - Minor update available: {res['update']['latest_version']}\n"
                elif int(version_diff[2]) > 0:
                    return_text += f"   - Patch update available: {res['update']['latest_version']}\n"
                return_text += f"\nDownload the latest version from https://github.com/dotargz/superterm/releases\n"
            elif res['update']['needs_update'] == "unknown":
                return_text += f"- Could not check for specific updates.\n"
            else:
                return_text += f"- No updates available.\n"
        except Exception as e:
            return_text = "Error: Could not check for updates.\n"
            return_text += f"Error Message: {e}\n"
    return return_text
