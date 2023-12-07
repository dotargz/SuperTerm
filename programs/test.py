# ------------------------------------------------------------------------------------
#   Test.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
#
#   WARNING: Legacy SuperTerm code, uses the return_text paradigm
#   When creating new programs, you may simply return a string and it will be printed
# ------------------------------------------------------------------------------------

# this is the metadata for the program that is used by the manual program, it has no effect on the program itself
metadata = {
    "name": "test",
    "description": "Boilerplate program.",
    "version": "1.0.0",
    "author": "dotargz",
    "dependencies": [],
    "superterm_version": ">=2.0.0",
    "usage": "test",
    "flags": {
        "--flag": "Flag description",
    },
    "arguments": {
        "arg1": "Argument description",
    },
    "examples": [
        {
            "description": "Test example",
            "command": "test",
        },
        {
            "description": "Test example with flag",
            "command": "test --flag",
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

def run(system, command_params, command_flags):
    return_text = "Boilerplate program."
    return return_text
