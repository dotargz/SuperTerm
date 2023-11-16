# -*- coding: utf-8 -*-

try:
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    import sys
    import pygame
    import json
    import platform
    import requests
    import pyperclip as pc
    import re
    import time
    import random
    import shlex
    import pythonping
    import socket as s
    import datetime
    import random
    import importlib
except:
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    os.system("pip install pygame requests pyperclip pythonping")
    exit()
# HAS TO BE DONE FIRST


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
            BIOS.dprint("Failed to remove SUPERTERMlogo.png")
        try:
            BIOS.dprint("Downloading logo...")
            rl = requests.get(
                "https://res.cloudinary.com/onespark/image/upload/v1657217805/SuperTerm/img/logo_hpnmvz.png", allow_redirects=True)
            open('SUPERTERMlogo.png', 'wb').write(rl.content)
            logo = pygame.image.load(resource_path("SUPERTERMlogo.png"))
            pygame.display.set_icon(logo)
            BIOS.dprint("logo downloaded successfully")
        except:
            BIOS.dprint("Failed to download logo")
        STANDALONE = True


load_logo()
FPS = 60
WINDOWS = None
FramePerSec = pygame.time.Clock()
FONT_SIZE = 14
Running = True
if STANDALONE:
    BIOS.dprint("[WARNING] Running in Standalone Mode")
    BIOS.dprint("Please run this program from the executable for the best results")


class OSNotSupported(Exception):
    "Raised when the OS is not supported"
    pass

class System(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global STANDALONE
        global WINDOWS
        global bootlist
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        self.NOTBLACK = (12, 12, 12)
        self.WHITE = (255, 255, 255)
        self.stoutsound = pygame.mixer.Sound(
            resource_path("assets/audio/stdout.wav"))
        self.VERSION = "0.5.0β"
        self.NAME = "SuperBIOS βeta"
        self.ticks = 0
        self.FONT_SIZE = 14
        self.y_offset = 5
        self.user_y_offset = self.y_offset
        self.warning = ""
        self.bootlist = ['[  OK  ] Started Show SuperTerm Boot Screen.', '[  OK  ] Started Forward Password R…s to SuperTerm Directory Watch.', '[  OK  ] Reached target Path Units.', '[  OK  ] Reached target Basic System.', '[  OK  ] Found device PLEXTOR_PX-128M3 SYSTEM.', '[  OK  ] Reached target Initrd Root Device.', '[  OK  ] Finished dracut initqueue hook.', '[  OK  ] Reached target Preparation for Remote File Systems.', '[  OK  ] Reached target Remote File Systems.', 'Starting File System Check…089e-4317-9ad5-2678ecf77029...', '[  OK  ] Finished File System Check…7-089e-4317-9ad5-2678ecf77029.', 'Mounting /sysroot...', '[  OK  ] Mounted /sysroot.', '[  OK  ] Reached target Initrd Root File System.', 'Starting Reload Configuration from the Real Root...', '[  OK  ] Finished Reload Configuration from the Real Root.', '[  OK  ] Reached target Initrd File Systems.', '[  OK  ] Reached target Initrd Default Target.', 'Starting Cleaning Up and Shutting Down Daemons...', '[  OK  ] Stopped target Initrd Default Target.', '[  OK  ] Stopped target Basic System.', '[  OK  ] Stopped target Initrd Root Device.', '[  OK  ] Stopped target Initrd /usr File System.', '[  OK  ] Stopped target Path Units.', '[  OK  ] Stopped target Remote File Systems.', '[  OK  ] Stopped target Preparation for Remote File Systems.', '[  OK  ] Stopped target Slice Units.', '[  OK  ] Stopped target Socket Units.', '[  OK  ] Stopped target System Initialization.', '[  OK  ] Stopped target Swaps.', '[  OK  ] Stopped target Timer Units.', '[  OK  ] Stopped dracut initqueue hook.', 'Starting Tell haveged about new root...', 'Starting SuperTerm switch root service...', '[  OK  ] Stopped Apply Kernel Variables.', '[  OK  ] Stopped Load Kernel Modules.', '[  OK  ] Stopped Create Volatile Files and Directories.', '[  OK  ] Stopped target Local File Systems.', '[  OK  ] Stopped Coldplug All udev Devices.', 'Stopping Rule-based Manage…for Device Events and Files...', '[  OK  ] Finished Cleaning Up and Shutting Down Daemons.', '[  OK  ] Stopped Rule-based Manager for Device Events and Files.', '[  OK  ] Closed udev Control Socket.', '[  OK  ] Closed udev Kernel Socket.', '[  OK  ] Stopped dracut pre-udev hook.', '[  OK  ] Stopped dracut cmdline hook.', '[  OK  ] Stopped dracut ask for additional cmdline parameters.', 'Starting Cleanup udev Database...', '[  OK  ] Stopped Create Static Device Nodes in /dev.', '[  OK  ] Stopped Create List of Static Device Nodes.', '[  OK  ] Finished Cleanup udev Database.', '[  OK  ] Finished Tell haveged about new root.', '[  OK  ] Reached target Switch Root.', '[  OK  ] Finished SuperTerm switch root service.', 'Starting Switch Root...', '[  OK  ] Stopped Switch Root.', '[  OK  ] Created slice Virtual Machine and Container Slice.', '[  OK  ] Created slice Slice /system/getty.', '[  OK  ] Created slice Slice /system/modprobe.', '[  OK  ] Created slice Slice /system/systemd-fsck.', '[  OK  ] Created slice User and Session Slice.', '[  OK  ] Set up automount Arbitrary…s File System Automount Point.', '[  OK  ] Stopped target Switch Root.', '[  OK  ] Stopped target Initrd File Systems.', '[  OK  ] Stopped target Initrd Root File System.', '[  OK  ] Reached target Slice Units.', '[  OK  ] Reached target System Time Set.', '[  OK  ] Reached target Local Verity Protected Volumes.', '[  OK  ] Listening on Device-mapper event daemon FIFOs.', '[  OK  ] Listening on LVM2 poll daemon socket.', '[  OK  ] Listening on Process Core Dump Socket.', '[  OK  ] Listening on initctl Compatibility Named Pipe.', '[  OK  ] Listening on udev Control Socket.', '[  OK  ] Listening on udev Kernel Socket.', 'Activating swap /dev/disk/…9816-459c-8d43-6f2656c7fa0a...', 'Mounting Huge Pages File System...', 'Mounting POSIX Message Queue File System...', 'Mounting Kernel Debug File System...', 'Mounting Kernel Trace File System...', 'Starting Load AppArmor profiles...', 'Starting Create List of Static Device Nodes...', 'Starting Monitoring of LVM…meventd or progress polling...', 'Starting Load Kernel Module configfs...', 'Starting Load Kernel Module drm...', 'Starting Load Kernel Module fuse...', '[  OK  ] Stopped Show SuperTerm Boot Screen.', '[  OK  ] Reached target Local Encrypted Volumes.', '[  OK  ] Stopped SuperTerm switch root service.', '[  OK  ] Stopped Journal Service.', '[  OK  ] Listening on Syslog Socket.', '[  OK  ] Stopped Entropy Daemon based on the HAVEGE algorithm.', 'Starting Journal Service...', 'Starting Load Kernel Modules...', 'Starting Remount Root and Kernel File Systems...', 'Starting Coldplug All udev Devices...', '[  OK  ] Activated swap /dev/disk/b…9-9816-459c-8d43-6f2656c7fa0a.', '[  OK  ] Mounted Huge Pages File System.', '[  OK  ] Mounted POSIX Message Queue File System.', '[  OK  ] Mounted Kernel Debug File System.', '[  OK  ] Mounted Kernel Trace File System.', '[  OK  ] Finished Create List of Static Device Nodes.', '[  OK  ] Finished Load Kernel Module configfs.', '[  OK  ] Finished Load Kernel Module drm.', '[  OK  ] Finished Load Kernel Module fuse.', '[  OK  ] Reached target Swaps.', 'Mounting FUSE Control File System...', 'Mounting Kernel Configuration File System...', 'Mounting Temporary Directory /tmp...', '[  OK  ] Mounted FUSE Control File System.', '[  OK  ] Mounted Kernel Configuration File System.', '[  OK  ] Mounted Temporary Directory /tmp.', '[  OK  ] Finished Monitoring of LVM… dmeventd or progress polling.', '[  OK  ] Finished Load Kernel Modules.', 'Starting Apply Kernel Variables for 5.15.8-1-default...', '[  OK  ] Started Journal Service.', '[  OK  ] Finished Remount Root and Kernel File Systems.', 'Starting Flush Journal to Persistent Storage...', 'Starting Load/Save Random Seed...', 'Starting Create Static Device Nodes in /dev...', '[  OK  ] Finished Flush Journal to Persistent Storage.', '[  OK  ] Finished Apply Kernel Variables for 5.15.8-1-default.', 'Starting Apply Kernel Variables...', '[  OK  ] Finished Load AppArmor profiles.', '[  OK  ] Finished Load/Save Random Seed.', '[  OK  ] Finished Create Static Device Nodes in /dev.', '[  OK  ] Reached target Preparation for Local File Systems.',
                         'Starting File System Check…6895-4a09-9aac-4412f3e46349...', 'Starting File System Check…9ec4-460e-ae25-83870db3baad...', 'Starting File System Check…850d-45e0-a3ef-38a5a69268c7...', 'Starting Rule-based Manage…for Device Events and Files...', '[  OK  ] Finished Apply Kernel Variables.', '[  OK  ] Finished Coldplug All udev Devices.', '[  OK  ] Finished File System Check…3-850d-45e0-a3ef-38a5a69268c7.', 'Mounting /home...', '[  OK  ] Mounted /home.', '[  OK  ] Started Rule-based Manager for Device Events and Files.', '[  OK  ] Finished File System Check…4-9ec4-460e-ae25-83870db3baad.', 'Mounting /mnt/PX256...', '[  OK  ] Mounted /mnt/PX256.', '[  OK  ] Finished File System Check…f-6895-4a09-9aac-4412f3e46349.', 'Mounting /mnt/DATA...', '[  OK  ] Mounted /mnt/DATA.', '[  OK  ] Reached target Local File Systems.', 'Starting Restore /run/initramfs on shutdown...', 'Starting Early Kernel Boot Messages...', 'Starting Tell SuperTerm To Write Out Runtime Data...', 'Starting Create Volatile Files and Directories...', '[  OK  ] Finished Restore /run/initramfs on shutdown.', '[  OK  ] Finished Tell SuperTerm To Write Out Runtime Data.', '[  OK  ] Finished Create Volatile Files and Directories.', 'Starting Security Auditing Service...', '[  OK  ] Started Entropy Daemon based on the HAVEGE algorithm.', '[  OK  ] Started Security Auditing Service.', 'Starting Record System Boot/Shutdown in UTMP...', '[  OK  ] Finished Record System Boot/Shutdown in UTMP.', '[  OK  ] Reached target System Initialization.', '[  OK  ] Started Watch /etc/sysconfig/btrfsmaintenance.', '[  OK  ] Started Watch for changes in CA certificates.', '[  OK  ] Started CUPS Scheduler.', '[  OK  ] Started Daily Cleanup of Snapper Snapshots.', '[  OK  ] Started Daily Cleanup of Temporary Directories.', '[  OK  ] Reached target Path Units.', '[  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.', '[  OK  ] Listening on CUPS Scheduler.', '[  OK  ] Listening on D-Bus System Message Bus Socket.', '[  OK  ] Listening on Open-iSCSI iscsid Socket.', '[  OK  ] Listening on Libvirt local socket.', '[  OK  ] Listening on Libvirt admin socket.', '[  OK  ] Listening on Libvirt local read-only socket.', '[  OK  ] Listening on PC/SC Smart Card Daemon Activation Socket.', '[  OK  ] Listening on Virtual machine lock manager socket.', '[  OK  ] Listening on Virtual machine log manager socket.', '[  OK  ] Reached target Socket Units.', '[  OK  ] Reached target Basic System.', 'Starting auditd rules generation...', 'Starting Avahi mDNS/DNS-SD Stack...', '[  OK  ] Started D-Bus System Message Bus.', '[  OK  ] Started irqbalance daemon.', 'Starting Generate issue file for login session...', 'Starting Apply settings from /etc/sysconfig/keyboard...', 'Starting Machine Check Exception Logging Daemon...', 'Starting Name Service Cache Daemon...', 'Starting Authorization Manager...', 'Starting System Logging Service...', 'Starting Self Monitoring a…g Technology (SMART) Daemon...', 'Starting Virtual Machine a…tainer Registration Service...', '[  OK  ] Finished Early Kernel Boot Messages.', '[  OK  ] Started Name Service Cache Daemon.', '[  OK  ] Reached target Host and Network Name Lookups.', '[  OK  ] Reached target User and Group Name Lookups.', 'Starting User Login Management...', '[  OK  ] Started Machine Check Exception Logging Daemon.', 'Starting Save/Restore Sound Card State...', '[  OK  ] Finished Generate issue file for login session.', '[  OK  ] Finished Save/Restore Sound Card State.', 'Starting Load extra kernel modules for sound stuff...', '[  OK  ] Finished Load extra kernel modules for sound stuff.', '[  OK  ] Reached target Sound Card.', '[  OK  ] Finished auditd rules generation.', '[  OK  ] Started System Logging Service.', '[  OK  ] Finished Apply settings from /etc/sysconfig/keyboard.', '[  OK  ] Started Virtual Machine an…ontainer Registration Service.', '[  OK  ] Started User Login Management.', '[  OK  ] Started Avahi mDNS/DNS-SD Stack.', '[  OK  ] Started Authorization Manager.', 'Starting Modem Manager...', 'Starting firewalld - dynamic firewall daemon...', '[  OK  ] Started Modem Manager.', '[  OK  ] Started Self Monitoring an…ing Technology (SMART) Daemon.', '[  OK  ] Started firewalld - dynamic firewall daemon.', '[  OK  ] Reached target Preparation for Network.', 'Starting Network Manager...', '[  OK  ] Started Network Manager.', '[  OK  ] Reached target Network.', '[  OK  ] Reached target Network is Online.', 'Starting NTP client/server...', 'Starting CUPS Scheduler...', 'Starting Login and scanning of iSCSI devices...', 'Starting Samba SMB Daemon...', 'Starting Hostname Service...', '[  OK  ] Finished Login and scanning of iSCSI devices.', '[  OK  ] Reached target Remote File Systems.', 'Starting Virtualization daemon...', 'Starting Permit User Sessions...', '[  OK  ] Started CUPS Scheduler.', '[  OK  ] Finished Permit User Sessions.', 'Starting Hold until boot process finishes up...', '[  OK  ] Started NTP client/server.', '[  OK  ] Reached target System Time Synchronized.', '[  OK  ] Started Backup of RPM database.', '[  OK  ] Started Backup of /etc/sysconfig.', '[  OK  ] Started Balance block groups on a btrfs filesystem.', '[  OK  ] Started Scrub btrfs filesystem, verify block checksums.', '[  OK  ] Started Check if mainboard battery is Ok.', '[  OK  ] Started Discard unused blocks once a week.', '[  OK  ] Started Daily rotation of log files.', '[  OK  ] Started Daily man-db regeneration.', '[  OK  ] Started Timeline of Snapper Snapshots.', '[  OK  ] Started daily update of the root trust anchor for DNSSEC.', '[  OK  ] Reached target Timer Units.', '[  OK  ] Started Command Scheduler.', 'Starting X Display Manager...', '[  OK  ] Started Hostname Service.', '[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.', 'Starting Network Manager Script Dispatcher Service...', '[  OK  ] Started Network Manager Script Dispatcher Service.', 'Starting Locale Service...', '[  OK  ] Started Virtualization daemon.', '[  OK  ] Started Samba SMB Daemon.', '[  OK  ] Started Locale Service.']
        # set the max ticks to the length of the bootlist unless env is set to false
        if self.get_env("boot_anim", "true").lower() == "false":
            self.maxticks = 0
        else:
            self.maxticks = len(self.bootlist)

        if platform.system() != "Windows":
            self.dprint("[WARNING] Running on a non-Windows OS")
            self.dprint("Please run this program from the executable for the best results")
            global WINDOWS
            WINDOWS = False
        else:
            WINDOWS = True
        self.current_display = f"{self.NAME} [Version {self.VERSION}]\n\n"

    def update(self, checkY=True):
        if self.ticks >= self.maxticks/(1+random.random()):
            global INBIOS
            INBIOS = False
            time.sleep(random.random()*0.5)
        else:
            self.ticks += 1
            time.sleep(random.random()/15)
            SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAYSURF.get_size()
            global SYSFONT
            SYSFONT = pygame.font.SysFont("monotype", self.FONT_SIZE)
            global bootlist
            self.current_display += self.bootlist[self.ticks] + "\n"
            if checkY == False:
                self.blit_text(DISPLAYSURF, self.current_display +
                               "\n", (5, self.user_y_offset), SYSFONT, self.WHITE)
            else:
                self.blit_text(DISPLAYSURF, self.current_display +
                               "\n", (5, self.y_offset), SYSFONT, self.WHITE, True)

            pygame.mixer.Sound.play(self.stoutsound)

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

    def set_env(self, key, value, deleteIfNone=False):
        try:
            with open(resource_path("assets/data/environment.json"), "r") as f:
                env = json.load(f)
        except:
            env = {}
        if value == None and deleteIfNone == True:
            try:
                del env[key]
            except KeyError:
                pass
        else:
            env[key] = value
        with open(resource_path("assets/data/environment.json"), "w") as f:
            json.dump(env, f)

    def get_env(self, key, default=None):
        try:
            with open(resource_path("assets/data/environment.json"), "r") as f:
                env = json.load(f)
        except:
            env = {}
        try:
            return env[key]
        except KeyError:
            return default

    def dprint(*arg):
        if BIOS.get_env("debug", "false").lower() == "true":
            print(*arg)


class Terminal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global STANDALONE
        global WINDOWS
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        self.NOTBLACK = (12, 12, 12)
        self.WHITE = (255, 255, 255)
        self.VERSION = "2.0.0β"
        self.NAME = "SuperTerm βeta"
        pygame.display.set_caption(f"{self.NAME} {self.VERSION}")
        self.FONT_SIZE = 14
        self.load_font()
        self.cursor_blinking = False
        self.cursor_blink_time = 0
        self.y_offset = 5
        self.user_y_offset = self.y_offset
        self.history = []
        self.history_count = 0
        self.history_persistent = BIOS.get_env("history_persistent", "false").lower() == "true"
        self.load_history()
        self.current_input = ""
        self.stoutsound = pygame.mixer.Sound(
            resource_path("assets/audio/stdout.wav"))
        self.stinsound = pygame.mixer.Sound(
            resource_path("assets/audio/stdin.wav"))
        self.startupsound = pygame.mixer.Sound(
            resource_path("assets/audio/win11start.wav"))
        self.hasplayedstartup = False
        self.warning = ""
        if WINDOWS == False:
            self.warning += '\n[ WARN ] Non-Windows OS detected.\n[ NON-WINDOWS ] The terminal will not be able to run properly on non-Windows operating systems.'
        if STANDALONE == True:
            self.warning += '\n[ WARN ] Standalone mode enabled.\n[ STANDALONE ] Downloading assets...\n\nWARNING: YOU ARE RUNNING SUPERTERM AS A STANDALONE PYTHON FILE,\nTHE TERMINAL WILL REQUIRE A INTERNET CONNECTION TO WORK AS EXPECTED.\nTO RELOAD THE TERMINAL AND ITS ASSETS, RUN THE COMMAND "RELOAD".'
        self.current_display = f"{self.NAME} [Version {self.VERSION}]\n(c) 2022 OneSpark LLC. All rights reserved.{self.warning}\n\n"
        self.load_programs()
        self.system_commands = {
            "exit": self.exit,
            "clear": self.clear,
            "reload": self.reload,
        }

        #alias for programs so they are somewhat sandboxed (not really)
        class AliasWrapper:
            def __init__(self):
                self.aliaslist = {
                    "get_env": BIOS.get_env,
                    "set_env": BIOS.set_env,
                    "dprint": BIOS.dprint,
                    "resource_path": resource_path,
                    "OSNotSupported": OSNotSupported,
                }
            def __getattr__(self, name):
                if name in self.aliaslist:
                    return self.aliaslist[name]
                else:
                    return NameError(f"name '{name}' is not defined")
        self.alias = AliasWrapper()

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
                BIOS.dprint("Failed to remove FiraCode-Regular.ttf")
            try:
                BIOS.dprint("Downloading FiraCode-Regular.ttf...")
                rf = requests.get(
                    "https://res.cloudinary.com/onespark/raw/upload/v1657217832/SuperTerm/fonts/FiraCode-Regular_flmsme.ttf", allow_redirects=True)
                try:
                    open('FiraCode-Regular.ttf', 'wb').write(rf.content)
                    BIOS.dprint("FiraCode-Regular.ttf downloaded successfully")
                except:
                    BIOS.dprint(
                        "Failed to write FiraCode-Regular.ttf (probably because of a permissions error)")
                try:
                    FONT = pygame.font.Font(resource_path(
                        "FiraCode-Regular.ttf"), self.FONT_SIZE)
                except:
                    BIOS.dprint("Failed to load FiraCode-Regular.ttf")
            except:
                FONT = pygame.font.SysFont("monotype", self.FONT_SIZE)
                BIOS.dprint("Failed to download FiraCode-Regular.ttf ")
            STANDALONE = True

    def load_history(self):
        # Loads all saved history
        if not self.history_persistent:
            return
        persistent_history = resource_path("assets\\data\\history.json")

        # create the file if it doesn't exist
        if not os.path.exists(persistent_history):
            with open(persistent_history, 'w') as f:
                json.dump([], f)

        with open(persistent_history, 'r') as f:
            self.history = json.load(f)

    def save_history(self):
        # Saves any new history
        if not self.history_persistent:
            return
        persistent_history = resource_path("assets/data/history.json")
        with open(persistent_history, 'w') as f:
            try:
                json.dump(self.history, f)
            except:
                BIOS.dprint("Error: Writing to terminal history failed.")

    def update(self, checkY=False):
        if self.hasplayedstartup == False:
            pygame.mixer.Sound.play(self.startupsound)
            self.hasplayedstartup = True
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
            BIOS.dprint("Full command: " + str(tokenized))
            BIOS.dprint("CURRENT COMMAND: " + str(cmd))
            BIOS.dprint("Commnd length: " + str(len(tokenized)))
            # format the commands in various ways
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
            BIOS.dprint("Command: " + command)
            BIOS.dprint("Full Command: " + full_command)
            BIOS.dprint("Params: " + str(command_params))
            BIOS.dprint("Flags: " + str(command_flags))
            # check if the command is valid
            if command in self.programs:
                # run the command
                return_text = self.run_program(command, command_params, command_flags) + "\n"
            elif command in self.system_commands:
                # run the command
                return_text = self.system_commands[command]() if not None else "" + "\n"
                sandbox = True
            else:
                return_text = f"Error: Command '{command}' not found.\n"
            if sandbox == False:
                if command != "clear":
                    if len(tokenized) == 1:
                        self.current_display += f'~$ {full_command}\n' + \
                            return_text
                        self.history.append(full_command)
                        self.history_count = 0
                        pygame.mixer.Sound.play(TERMINAL.stoutsound)
                    else:
                        if notFirst == False:
                            self.current_display += f'~$ {full_command}\n' + \
                                return_text
                            BIOS.dprint("Adding to history: " + full_command)
                            self.history.append(full_command)
                            self.history_count = 0
                            notFirst = True
                            pygame.mixer.Sound.play(TERMINAL.stoutsound)
                        else:
                            self.current_display += return_text

        if sandbox == True:
            return return_text
        self.save_history() # Runs after any commands are ran

    def load_programs(self):
        # import all py scripts in the /programs folder and add them to the list of valid programs
        self.programs = []
        for file in os.listdir(resource_path("programs")):
            if file.endswith(".py"):
                self.programs.append(file.replace(".py", ""))
                BIOS.dprint("Loaded program: " + file.replace(".py", ""))

    def run_program(self, program, params, flags):
        # run a program from the /programs folder
        try:
            program_module = importlib.import_module(
                "programs." + program)
            return_text = program_module.run(self, params, flags)
            return return_text
        except ModuleNotFoundError:
            return_text = f"Error: Program '{program}' not found.\n"
            return return_text
        except OSNotSupported:
            return_text = f"Error: Program '{program}' not supported on this OS.\n"
            return_text += f"Error: {e}\n"
            return return_text

    def get_program_metadata(self, program):
        # get the metadata for a program
        try:
            program_module = importlib.import_module(
                "programs." + program)
            try:
                tmp = program_module.metadata
                return tmp
            except AttributeError:
                return None
        except ModuleNotFoundError:
            return None


    def clear(self):
        self.current_display = ""
        self.blit_text(DISPLAYSURF, self.current_display,
                       (5, 5), FONT, TERMINAL.WHITE)
        self.y_offset = 5
        self.user_y_offset = 5

    def exit(self):
        global Running
        print('[ INFO ] Exiting...')
        Running = False
        self.save_history() # Since otherwise it wouldn't be auto-saved
        pygame.quit()
        sys.exit()
        exit()

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

        BIOS.dprint("justcommand: " + str(justcommand))

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

        BIOS.dprint("justflag: " + str(justflag))

        # Shlex processing to make life easier
        output = []
        for i in range(len(split_commands)):
            output.append(shlex.split(split_commands[i]))

        BIOS.dprint("output: " + str(output))

        # Parameters processing
        output2 = []
        for command in range(len(output)):
            tmp = [[]]
            for token_index in range(len(output[command])):
                if token_index != 0 and not output[command][token_index].startswith("-"):
                    tmp[0].append(output[command][token_index])
            output2.append(tmp)

        BIOS.dprint("Just params: " + str(output2))

        # Add the command names and flags back
        for rcmd in range(len(justcommand)):
            output2[rcmd].insert(0, justcommand[rcmd])
            output2[rcmd].append(justflag[rcmd])

        return output2

    def reload(self):
        self.__init__()
        BIOS.dprint("Reloaded.")
        self.hasReloaded = True
        return None

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


BIOS = System()
INBIOS = True
TERMINAL = Terminal()
while Running:
    # Event handling
    for event in pygame.event.get():
        if INBIOS == False:
            if event.type == pygame.KEYUP:
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
                    pygame.mixer.Sound.play(TERMINAL.stinsound)
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
                            pygame.mixer.Sound.play(TERMINAL.stinsound)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    TERMINAL.current_input += pc.paste()
                if event.button == 4:
                    TERMINAL.user_y_offset = min(
                        TERMINAL.user_y_offset + 56, 5)
                if event.button == 5:
                    TERMINAL.user_y_offset -= 56
                TERMINAL.update()
            elif event.type == pygame.VIDEORESIZE:
                DISPLAYSURF = pygame.display.set_mode(
                    event.size, pygame.RESIZABLE)
                TERMINAL.y_offset = 5
                TERMINAL.update(True)
        if event.type == pygame.QUIT:
            Running = False
            sys.exit()

    DISPLAYSURF.fill(TERMINAL.NOTBLACK)

    INBOOTSCREEN = False
    if INBIOS == False:
        TERMINAL.update()
    else:
        if INBOOTSCREEN == True:
            BOOTSCREEN.update()
        else:
            BIOS.update()

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
