# ------------------------------------------------------------------------------------
#   NSlookup.py for SuperTerm
#   Author: dotargz
#   Date: 2023-11-14
# ------------------------------------------------------------------------------------
import socket as s

metadata = {
    "name": "nslookup",
    "description": "Lookup the IP address of a hostname.",
    "version": "1.0.0",
    "author": "dotargz",
    "dependencies": ["socket"],
    "superterm_version": ">=1.0.0",
    "usage": "nslookup <hostname>"
}

def pad(tmp):
    max_length = 15
    tmp += " " * (max_length - len(tmp))
    return tmp

def run(system, command_params, command_flags):
    try:
        host = command_params[0]
        ipv4 = s.gethostbyname(host)
        ipv6_data = s.getaddrinfo(host, "7") # echo port
        result = ""
        result += pad('Server:') + f"{ipv4}\n"
        result += pad('Address:') + f"{ipv4}#7\n"
        result += f"\n"
        result += f"Non-authoritative answer:\n"
        result += pad('Name:') + f"{host.lower()}\n"
        result += pad('Address:') + f"{ipv4}\n"
        result += pad('Name:') + f"{host.lower()}\n"
        result += pad('Address:') + f"{str(ipv6_data[0][4][0])}\n"
        return result
    except IndexError:
        return "Error: No url specified\n"
    except s.gaierror:
        return f"Error: Could not find hostname '{command_params[0]}'.\n"
