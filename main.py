# -*- coding: utf-8 -*-

import os
os.system("pip install pygame requests pyperclip pythonping")
import sys
import pygame
import json
import requests
import pyperclip as pc
import re
import shlex
import pythonping

pygame.init()

# for compiling the program


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Variable Setup (ONLY FOR FULL CLIENT)
DISPLAYSURF = pygame.display.set_mode((952, 480), pygame.RESIZABLE)
SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAYSURF.get_size()


def load_logo():
    global logo
    global STANDALONE
    try:
        logo = pygame.image.load(resource_path("assets/img/logo.png"))
        pygame.display.set_icon(logo)
        STANDALONE = False
    except:
        try:
            os.remove("SUPERTERMlogo.png")
        except:
            print("Failed to remove SUPERTERMlogo.png")
        try:
            print("Downloading logo...")
            rl = requests.get(
                "https://res.cloudinary.com/onespark/image/upload/v1657217805/SuperTerm/img/logo_hpnmvz.png", allow_redirects=True)
            open('SUPERTERMlogo.png', 'wb').write(rl.content)
            logo = pygame.image.load(resource_path("SUPERTERMlogo.png"))
            pygame.display.set_icon(logo)
            print("logo downloaded successfully")
        except:
            print("Failed to download logo")
        STANDALONE = True


load_logo()
FPS = 60
FramePerSec = pygame.time.Clock()
FONT_SIZE = 14
quality = "low"  # unused for now
Running = True
#global y_offset
#global user_y_offset
#y_offset = 5
#user_y_offset = y_offset
if STANDALONE:
    print("[WARNING] Running in Standalone Mode")
    print("Please run this program from the executable for the best results")


class Terminal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        self.NOTBLACK = (12, 12, 12)
        self.WHITE = (255, 255, 255)
        self.VERSION = "0.4.2α"
        self.NAME = "SuperTerm αlpha"
        pygame.display.set_caption(f"{self.NAME} {self.VERSION}")
        self.FONT_SIZE = 14
        self.load_font()
        self.cursor_blinking = False
        self.cursor_blink_time = 0
        self.y_offset = 5
        self.user_y_offset = self.y_offset
        self.history = []
        self.history_count = 0
        self.current_input = ""
        if STANDALONE == True:
            warning = '\n[ WARN ] Standalone mode enabled.\n[ STANDALONE ] Downloading assets...\n\nWARNING: YOU ARE RUNNING SUPERTERM AS A STANDALONE PYTHON FILE,\nTHE TERMINAL WILL REQUIRE A INTERNET CONNECTION TO WORK AS EXPECTED.\nTO RELOAD THE TERMINAL AND ITS ASSETS, RUN THE COMMAND "RELOAD".'
        else:
            warning = ''
        self.current_display = f"{self.NAME} [Version {self.VERSION}]\n(c) 2022 OneSpark LLC. All rights reserved.{warning}\n\n"

    def load_font(self, isReloading=False):
        global FONT
        global STANDALONE
        try:
            FONT = pygame.font.Font(resource_path(
                'assets/fonts/FiraCode-Regular.ttf'), self.FONT_SIZE)
            STANDALONE = False
        except:
            try:
                if isReloading == False:
                    os.remove("FiraCode-Regular.ttf")
            except:
                print("Failed to remove FiraCode-Regular.ttf")
            try:
                print("Downloading FiraCode-Regular.ttf...")
                rf = requests.get(
                    "https://res.cloudinary.com/onespark/raw/upload/v1657217832/SuperTerm/fonts/FiraCode-Regular_flmsme.ttf", allow_redirects=True)
                try:
                    open('FiraCode-Regular.ttf', 'wb').write(rf.content)
                    print("FiraCode-Regular.ttf downloaded successfully")
                except:
                    print(
                        "Failed to write FiraCode-Regular.ttf (probably because of a permissions error)")
                try:
                    FONT = pygame.font.Font(resource_path(
                        "FiraCode-Regular.ttf"), self.FONT_SIZE)
                except:
                    print("Failed to load FiraCode-Regular.ttf")
            except:
                FONT = pygame.font.SysFont("monotype", self.FONT_SIZE)
                print("Failed to download FiraCode-Regular.ttf ")
            STANDALONE = True

    def update(self, checkY=False):
        SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAYSURF.get_size()
        if self.cursor_blinking == True:
            cursor_char = ""
        elif self.cursor_blinking == False:
            cursor_char = "_"
        if checkY == False:
            global FONT
            self.blit_text(DISPLAYSURF, self.current_display +
                           f'~$ {self.current_input}' + cursor_char + "\n", (5, self.user_y_offset), FONT, TERMINAL.WHITE)
        else:
            self.blit_text(DISPLAYSURF, self.current_display +
                           f'~$ {self.current_input}' + cursor_char + "\n", (5, self.y_offset), FONT, TERMINAL.WHITE, True)

    def down_history(self):
        TERMINAL.history_count += 1
        if TERMINAL.history_count >= 1:
            TERMINAL.history_count = 0
        if TERMINAL.history_count == 0:
            TERMINAL.current_input = ""
        else:
            if TERMINAL.history_count < 0:
                try:
                    TERMINAL.current_input = TERMINAL.history[TERMINAL.history_count]
                except IndexError:
                    TERMINAL.history_count = 0
                    TERMINAL.current_input = ""
            else:
                pass

    def up_history(self):
        TERMINAL.history_count -= 1
        if TERMINAL.history_count == 0:
            TERMINAL.current_input = ""
        else:
            try:
                if TERMINAL.history_count < 0 - len(TERMINAL.history):
                    TERMINAL.history_count = 0 - len(TERMINAL.history)
                TERMINAL.current_input = TERMINAL.history[TERMINAL.history_count]
            except IndexError:
                TERMINAL.history_count = 0
                TERMINAL.current_input = ""

    def capitalize(self, string):
        mapping = [('1', '!'), ('2', '@'), ('3', '#'), ('4', '$'), ('5', '%'), ('6', '^'), ('7', '&'), ('8', '*'), ('9', '('), ('0', ')'),
                   ('-', '_'), ('=', '+'), ('[', '{'), (']', '}'), ('\\', '|'), (';', ':'), ('\'', '"'), (',', '<'), ('.', '>'), ('/', '?')]
        for k, v in mapping:
            string = string.replace(k, v)
        return string

    def run_command(self, command, sandbox=False, notFirst=False):
        # strip the command of backslashes
        #command = re.sub(r'\\$|\\', '', command)
        try:
            tokenized = self.advanced_tokenize(command)
        except ValueError:
            self.current_display += f'~$ {command}\n' + \
                "Error: Invalid syntax.\n"
            self.history.append(command)
            self.history_count = 0
            return
        # reject empty commands
        if tokenized == [['', [], []]]:
            return
        for cmd in tokenized:
            print("Full command: " + str(tokenized))
            print("CURRENT COMMAND: " + str(cmd))
            print("Commnd length: " + str(len(tokenized)))
            # list of valid commands
            vaild_commands = ["echo", "clear", "exit",
                              "help", "run", "version", "debug", "license", "reload", "tkz", "ping", "update", "st", "kill"]
            command_alias = ["cls"]
            # format the commands in various ways
            list_commands = ", ".join(vaild_commands)
            return_text = ""
            full_command = command
            tkcommand = cmd[0]
            normal_command = tkcommand
            command = tkcommand.lower()
            command_params = cmd[1]
            command_flags = cmd[2]
            # cleanze the parameters
            while "" in command_params:
                command_params.remove("")
            # print for debugging
            print("Command: " + command)
            print("Full Command: " + full_command)
            print("Params: " + str(command_params))
            print("Flags: " + str(command_flags))
            # check if the command is valid
            if command in vaild_commands or command in command_alias:
                if command == "clear" or command == "cls":
                    self.clear()
                elif command == "echo":
                    return_text = " ".join(command_params) + "\n"
                elif command == "exit":
                    global Running
                    print('[ INFO ] Exiting...')
                    Running = False
                    pygame.quit()
                    sys.exit()
                    exit()
                elif command == "help":
                    return_text = f"Commands: {list_commands}\n"
                elif command == "run":
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
                elif command == "version":
                    return_text = f"{TERMINAL.NAME} v{TERMINAL.VERSION}\n"
                elif command == "license":
                    return_text = f"Copyright 2022 OneSpark LLC.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
                elif command == "debug":
                    debug_string = {"History": str(
                        self.history), "History count": str(self.history_count)}
                    print(debug_string)
                    return_text = f"{debug_string}\n"
                elif command == "reload":
                    self.reload()
                    sandbox = True
                elif command == "tkz":
                    return_text = f"{str(self.advanced_tokenize(full_command))}\n"
                elif command == "ping":
                    try:
                        ping_list = pythonping.ping(
                            command_params[0], verbose=True, size=2)
                        for response in ping_list:
                            return_text += f"{response}\n"
                    except PermissionError:
                        return_text += "Error: ICMP Permission denied.\n"
                    except RuntimeError:
                        return_text += f"Error: Could not find hostname '{command_params[0]}'.\n"
                elif command == "update":
                    r = requests.get("https://server.hyprlink.xyz/updatecheck?client=terminal&version=" + TERMINAL.VERSION.replace("α", ""))
                    #convert from json to dict
                    res = json.loads(r.text)
                    try:
                        return_text = f"Version Status:\n"
                        #return_text += f"Server Status: {res['server']['status']}\n"
                        return_text += f"- Latest Version: {res['update']['latest_version']}α\n"
                        return_text += f"- Current Version: {TERMINAL.VERSION}\n"
                        return_text += f"Update Status:\n"
                        if res['update']['needs_update'] == "true":
                            if res['update']['version_diff'].split(".")[0] != "0":
                                return_text += f"- Major update available: {res['update']['latest_version']}α\n"
                            elif res['update']['version_diff'].split(".")[1] != "0":
                                return_text += f"- Minor update available: {res['update']['latest_version']}α\n"
                            elif res['update']['version_diff'].split(".")[2] != "0":
                                return_text += f"- Patch update available: {res['update']['latest_version']}α\n"
                            return_text += f"Download the latest version from https://github.com/dotargz/superterm/releases\n"
                        else:
                            return_text += f"- No updates available.\n"
                    except Exception as e:
                        return_text = "Error: Could not check for updates.\n"
                elif command == "st":
                    os.system(f"start {os.path.basename(__file__)}")
                    if "-s" not in command_flags:
                        return_text = f"Running SuperTerm...\n"
                    else:
                        return_text = ""
                else:
                    return_text = "Error: Command handler not found.\n"
            else:
                return_text = f"Error: Command '{normal_command}' not found.\n"
            if sandbox == False:
                if command != "clear" and command != "cls":
                    if len(tokenized) == 1:
                        self.current_display += f'~$ {full_command}\n' + \
                            return_text
                        self.history.append(full_command)
                        self.history_count = 0
                    else:
                        if notFirst == False:
                            self.current_display += f'~$ {full_command}\n' + \
                                return_text
                            print("Adding to history: " + full_command)
                            self.history.append(full_command)
                            self.history_count = 0
                            notFirst = True
                        else:
                            self.current_display += return_text
        if sandbox == True:
            return return_text

    def clear(self):
        self.current_display = ""
        self.blit_text(DISPLAYSURF, self.current_display,
                       (5, 5), FONT, TERMINAL.WHITE)
        self.y_offset = 5
        self.user_y_offset = 5

    def tokenize(self, command):
        tokens = command.split(" ")
        return tokens

    def advanced_tokenize(self, command):
        # Basic processing
        command = command.strip()
        split_commands = re.split(' && ', command)

        # Command action handling
        global justcommand
        justcommand = []
        for cmd in range(len(split_commands)):
            tokens = split_commands[cmd].split(" ")
            justcommand.append(tokens[0])

        # Flag handling
        global justflag
        justflag = []
        for cmd in range(len(split_commands)):
            flagtmp = []
            tokens = split_commands[cmd].split(" ")
            for token in range(len(tokens)):
                if tokens[token].startswith("-") == True:
                    flagtmp.append(tokens[token])
            justflag.append(flagtmp)

        # Shlex processing to make life easier
        output = []
        for i in range(len(split_commands)):
            output.append(shlex.split(split_commands[i]))

        # Parameters processing
        output2 = []
        global tmp
        for command in range(len(output)):
            tmp = [[]]
            for token in range(len(output[command])):
                if output[command].index(str(output[command][token])) != 0:
                    if output[command][token].startswith("-") == False:
                        tmp[0].append(output[command][token])
            output2.append(tmp)

        #print("Just params: " + str(output2))

        # Add the command names and flags back
        for rcmd in range(len(justcommand)):
            output2[rcmd].insert(0, justcommand[rcmd])
            output2[rcmd].append(justflag[rcmd])

        return output2

    def reload(self):
        self.__init__()
        print("Reloaded.")
        self.hasReloaded = True

    def blit_text(self, surface, text, pos, font, color=pygame.Color(0, 0, 0), checkY=False):
        # 2D array where each row is a list of words.
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                if checkY:
                    if y + word_height >= max_height:
                        x = pos[0]
                        self.y_offset -= word_height
                        y -= word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.


TERMINAL = Terminal()
while Running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.key == pygame.K_RETURN:
                TERMINAL.run_command(TERMINAL.current_input)
                TERMINAL.current_input = ""
                TERMINAL.update(True)
                TERMINAL.user_y_offset = TERMINAL.y_offset
            elif event.key == pygame.K_BACKSPACE:
                try:
                    TERMINAL.current_input = TERMINAL.current_input[:-1]
                except:
                    TERMINAL.current_input = ""
            elif event.key == pygame.K_SPACE:
                TERMINAL.current_input = TERMINAL.current_input + " "
            elif event.key == pygame.K_ESCAPE:
                TERMINAL.current_input = ""
            elif event.key == pygame.K_TAB or event.key == pygame.K_CAPSLOCK or event.key == pygame.K_NUMLOCK or event.key == pygame.K_SCROLLOCK or event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT or event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL or event.key == pygame.K_RALT or event.key == pygame.K_LALT or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_HOME or event.key == pygame.K_END or event.key == pygame.K_PAGEUP or event.key == pygame.K_PAGEDOWN or event.key == pygame.K_F1 or event.key == pygame.K_F2 or event.key == pygame.K_F3 or event.key == pygame.K_F4 or event.key == pygame.K_F5 or event.key == pygame.K_F6 or event.key == pygame.K_F7 or event.key == pygame.K_F8 or event.key == pygame.K_F9 or event.key == pygame.K_F10 or event.key == pygame.K_F11 or event.key == pygame.K_F12 or event.key == pygame.K_INSERT or event.key == pygame.K_PRINTSCREEN:
                pass
            elif event.key == pygame.K_UP:
                TERMINAL.up_history()
            elif event.key == pygame.K_DOWN:
                TERMINAL.down_history()
            else:
                if event.key == pygame.K_LSHIFT:
                    pass
                elif event.key == pygame.K_RSHIFT:
                    pass
                else:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        TERMINAL.current_input = TERMINAL.current_input + \
                            TERMINAL.capitalize(
                                pygame.key.name(event.key).upper())
                    else:
                        TERMINAL.current_input = TERMINAL.current_input + \
                            pygame.key.name(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                TERMINAL.current_input += pc.paste()
            if event.button == 4:
                TERMINAL.user_y_offset = min(TERMINAL.user_y_offset + 56, 5)
            if event.button == 5:
                TERMINAL.user_y_offset -= 56
            TERMINAL.update()
        elif event.type == pygame.VIDEORESIZE:
            DISPLAYSURF = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            TERMINAL.y_offset = 5
            TERMINAL.update(True)
        if event.type == pygame.QUIT:
            Running = False
            sys.exit()

    DISPLAYSURF.fill(TERMINAL.NOTBLACK)

    TERMINAL.update()

    SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAYSURF.get_size()

    pygame.display.update()
    if TERMINAL.cursor_blinking == True and TERMINAL.cursor_blink_time > 30:
        TERMINAL.cursor_blinking = False
        TERMINAL.cursor_blink_time = 0
    elif TERMINAL.cursor_blinking == False and TERMINAL.cursor_blink_time > 30:
        TERMINAL.cursor_blinking = True
        TERMINAL.cursor_blink_time = 0
    else:
        TERMINAL.cursor_blink_time += 1
    FramePerSec.tick(FPS)
