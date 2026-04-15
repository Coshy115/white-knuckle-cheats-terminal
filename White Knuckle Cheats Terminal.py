### White Knuckle Cheats Terminal
# Python 3.14
import sys
import os
import time
import pydirectinput
import win32gui
import win32con
from colorama import Fore

cheats = False
status = ""

def clear_screen():
    os.system('cls')

def main_menu():
    if cheats == False:
        status = Fore.RED + "Disabled" + Fore.WHITE
        print("  White Knuckle Cheats Terminal")
        print("---------------------------------")
        print(f"1) Toggle Cheats [{status}] | 0) Exit")
        print("\n")
    else:
        status = Fore.GREEN + "Enabled" + Fore.WHITE
        print("  White Knuckle Cheats Terminal")
        print("---------------------------------")
        print(f"1) Toggle Cheats [{status}] | 2) Teleport Menu | 3) Items Menu | 4) Godify | 5) Denizens Menu | 0) Exit")
        print("\n")

def teleport_menu():
    clear_screen()
    print("  Teleport Menu  ")
    print("-----------------")
    print("1) Silos Beginning   | 2) Silos Saferoom    | 3) Interlude Lockdown")
    print("4) Interlude Ascent  | 5) Habitation Shaft  | 6) Delta Labs")
    print("7) Habitation Ending | 8) Back")
    print("\n")
    choice = int(input(": "))
    options = {1 : "m1_intro_01", 2 : "m1_silos_safearea_01", 3 : "campaign_interlude_silo_to_pipeworks_01", 
               4 : "campaign_interlude_pipeworks_to_habitation_01", 5 : "m3_habitation_shaft_intro", 6 : "m3_habitation_lab_lobby", 
               7 : "m3_habitation_lab_ending"}
    if choice != 8:
        while not choice in options and choice != 8:
           print("Choice not in list, please pick a number above.")
           choice = int(input(": "))
           if choice == 8:
               return "Back"
        return "teleportplayertolevel " + options[choice]
    else:
        return "Back"

def items_menu():
    clear_screen()
    print("  Items Menu  ")
    print("--------------")
    print("1) Hammer           | 2) Flashlight       | 3) Flare Gun")
    print("4) Flare            | 5) Floppy Disk T1   | 6) Floppy Disk T2")
    print("7) Floppy Disk T3   | 8) Brick            | 9) Piton")
    print("10) Auto Piton      | 11) Rebar           | 12) Rope Rebar")
    print("13) Explosive Rebar | 14) Blink Eye       | 15) Beans")
    print("16) Food Bar        | 17) Milk            | 18) Pills")
    print("19) Injector        | 20) Periphery Beans | 21) Timepiece")
    print("22) Translocator    | 23) Spear           | 24) Remote")
    print("25) Glove           | 26) Back")
    print("\n")
    choice = int(input(": "))
    options = {1 : "item_hammer", 2 : "item_flashlight", 3 : "item_flaregun", 
               4 : "item_flaregun_ammo", 5 : "item_floppy_t1", 6 : "item_floppy_t2", 
               7 : "item_floppy_t3", 8 : "item_rubble", 9 : "item_piton", 10 : "item_autopiton",
               11 : "item_rebar", 12 : "item_rebarrope", 13 : "item_rebar_explosive",
               14 : "item_blinkeye", 15 : "item_beans", 16 : "item_food_bar",
               17 : "item_milk", 18 : "item_pillbottle", 19 : "item_injector",
               20 : "item_beans_periphery", 21 : "item_artifact_timepiece", 22 : "item_artifact_translocator",
               23 : "item_artifact_rebar_return", 24 : "item_artifact_remote", 25 : "item_artifact_evaglove"}
    if choice != 26:
        while not choice in options and choice != 26:
           print("Choice not in list, please pick a number above.")
           choice = int(input(": "))
           if choice == 26:
               return "Back"
        return "spawnentity " + options[choice]
    else:
        return "Back"

def denizens_menu():
    clear_screen()
    print("  Denizens Menu  ")
    print("-----------------")
    print("1) Disable Mass     | 2) Ignored By Denizens | 3) Roach")
    print("4) Gold Roach       | 5) Platinum Roach      | 6) Ruby Roach")
    print("7) Lemon Roach      | 8) Breeder             | 9) Grub")
    print("10) Barnacle        | 11) Bloodbug           | 12) Hopper")
    print("13) Drone           | 14) Buddy              | 15) Sturge")
    print("16) Gasbag          | 17) Turret             | 18) Bloodbug Worker")
    print("19) Back")
    print("\n")
    choice = int(input(": "))
    options = {1 : "deathgoo-height NaN", 2 : "notarget", 3 : "denizen_roach", 
               4 : "denizen_roach_gold", 5 : "denizen_roach_platinum", 6 : "denizen_roach_flying_ruby", 
               7 : "denizen_roach_lemon", 8 : "denizen_breeder", 9 : "denizen_sluggrub", 10 : "denizen_barnacle_small",
               11 : "denizen_bloodbug", 12 : "denizen_hopper", 13 : "denizen_drone",
               14 : "denizen_drone_buddy", 15 : "denizen_sturge", 16 : "denizen_gasbag",
               17 : "denizen_turret_basic", 18 : "denizen_bloodbug_worker"}
    if choice == 1:
        return options[1]
    elif choice == 2:
        return options[2]
    elif choice != 19:
        while not choice in options and choice != 19:
           print("Choice not in list, please pick a number above.")
           choice = int(input(": "))
           if choice == 19:
               return "Back"
        return "spawnentity " + options[choice]
    else:
        return "Back"

def focus():
    def focus_window(title_substring):
        def enum_handler(hwnd, ctx):
            title = win32gui.GetWindowText(hwnd)
            if title == title_substring:
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)

        win32gui.EnumWindows(enum_handler, None)
    focus_window("White Knuckle")

def type_uppercase(x):
    pydirectinput.keyDown('shift')
    pydirectinput.press(x)
    pydirectinput.keyUp('shift')

def terminal(decision):
    focus()
    time.sleep(0.1)
    type_uppercase('`')
    time.sleep(0.1)
    pydirectinput.PAUSE = 0.01
    for i in decision:
        if i == "_":
            type_uppercase('-')
        elif i == "N":
            type_uppercase('n')
        else:
            pydirectinput.typewrite(i, interval=0)
    time.sleep(0.1)
    pydirectinput.press("enter")
    time.sleep(0.1)
    type_uppercase('`')

while True:
    clear_screen()
    main_menu()
    choice = int(input(": "))

    if choice == 1:
        terminal("cheats")
        if cheats == False:
            cheats = True
        else:
            cheats = False
    elif choice == 2:
        tp_choice = teleport_menu()
        if tp_choice == "Back":
            clear_screen()
            main_menu()
        else:
            terminal(tp_choice)
    elif choice == 3:
        item_choice = items_menu()
        if item_choice == "Back":
            clear_screen()
            main_menu()
        else:
            terminal(item_choice)
    elif choice == 4:
        terminal("godmode")
        terminal("fullbright")
        terminal("infinitestamina")
    elif choice == 5:
        denizen_choice = denizens_menu()
        if denizen_choice == "Back":
            clear_screen()
            main_menu()
        else:
            terminal(denizen_choice)
    elif choice == 0:
        sys.exit()