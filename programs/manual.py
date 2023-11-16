# ------------------------------------------------------------------------------------
#   manual.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   Lists the manual for a given program using the program's metadata fields.
# ------------------------------------------------------------------------------------

metadata = {
    "name": "manual",
    "description": "Lists the manual for a given program",
    "version": "1.0.0",
    "author": "dotargz",
    "dependencies": [],
    "superterm_version": ">=1.1.0",
    "usage": "manual <program> [--verbose]",
    "flags": {
        "--verbose": "Display verbose manual with increased indentation",
    },
    "arguments": {
        "<program>": "Name of the program to get the manual for",
    },
    "examples": [
        {
            "description": "Display manual for 'example_program'",
            "command": "manual example_program",
        },
        {
            "description": "Display verbose manual with increased indentation",
            "command": "manual example_program --verbose",
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


def toTitleCase(string):
    def tTC(string):
        if len(string) == 0:
            return ""
        if len(string) == 1:
            return string.upper()
        if string == "superterm":
            return "SuperTerm"
        tmp = string[0].upper() + string[1:].lower()
        return tmp
    # take a sentence and title case each word
    tmp = string.split("_")
    tmp = [tTC(word) for word in tmp]
    return " ".join(tmp)

def run(system, command_params, command_flags):
    indent = 0
    def format_metadata(metadata, indent):
        output = ""
        if "--verbose" in command_flags:
            for key, value in metadata.items():
                if isinstance(value, dict):
                    output += f"{toTitleCase(key)}:\n{format_metadata(value, indent + 1)}"
                elif isinstance(value, list):
                    output += f"{toTitleCase(key)}:\n"
                    for item in value:
                        if isinstance(item, dict):
                            output += format_metadata(item, indent + 1) + "\n"
                        elif isinstance(item, list):
                            output += f"{'  ' * (indent+1)}- {item}\n"
                        elif isinstance(item, str):
                            output += f"{'  ' * (indent+1)}- {item}\n"
                else:
                    output += f"{'  ' * indent}{toTitleCase(key)}: {value if value is not None else 'None'}\n"
        else:
            if "name" in metadata and "description" in metadata:
                output += f"{toTitleCase(metadata['name'])}: {metadata['description']}\n"
            if "usage" in metadata:
                output += f"Usage: {metadata['usage']}\n"
        return output

    if len(command_params) == 0:
        return "Error: No program specified\n"
    program = command_params[0]

    if program not in system.programs:
        return f"Error: Program '{program}' not found\n"

    program_metadata = system.get_program_metadata(program)

    if program_metadata is None:
        return f"'{program}' does not have any metadata associated with it.\n"

    return_text = format_metadata(program_metadata, 0)

    # if the program in question has metadata values that are not in this program's metadata, then it is likely that the program is setting its own metadata, and a warning should be displayed
    if len(set(program_metadata.keys()) - set(metadata.keys())) > 0:
        return_text += f"\nWarning: The program '{program}' is setting non-standard metadata values.\nWarning: This program may not be compatible with this version of SuperTerm.\n"

    return return_text

