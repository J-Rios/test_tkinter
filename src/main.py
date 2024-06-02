#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script:
    main.py
Description:
    TKinter Graphical User Interface Application demo test.
Author:
    Jose Miguel Rios Rubio
Date:
    2024-06-02
Version:
    1.0.0
'''

###############################################################################
# Standard Libraries
###############################################################################

# Logging Library
import logging

# System Library
from sys import argv as sys_argv
from sys import exit as sys_exit


###############################################################################
# Local Libraries
###############################################################################

# Graphical USer Interface Library
from gui import GraphicUserInterface


###############################################################################
# Logger Setup
###############################################################################

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


###############################################################################
# Constants & Configurations
###############################################################################

# GUI Window Minimum Width
WINDOW_WIDTH = 800

# GUI Window Minimum Height
WINDOW_HEIGHT = 600

# Software Version
VERSION = "1.0.0"

# Software Version Date
DATE = "2024-06-02"

# Version String
VERSION_STRING = f"v{VERSION} ({DATE})"


###############################################################################
# Left Sidebar Panel Button Functions
###############################################################################

def sidebar_btn_device_info_press():
    '''GUI Left Sidebar Panel "Info" Button Press Handler.'''
    print("Showing Device Info Frame")


def sidebar_btn_flash_fw_press():
    '''GUI Left Sidebar Panel "Flash" Button Press Handler.'''
    print("Showing FW Flash Frame")


def sidebar_btn_debug_press():
    '''GUI Left Sidebar Panel "Debug" Button Press Handler.'''
    print("Showing Debug Frame")


def sidebar_btn_about_press():
    '''GUI Left Sidebar Panel "About" Button Press Handler.'''
    print("Showing About Frame")


###############################################################################
# Main Function
###############################################################################

def main(argc, argv) -> int:
    '''Application Run.'''
    logger.info("Application Start")
    # Show Application Arguments
    logger.info("APP Number of Arguments: %d", argc)
    logger.info("APP Arguments:")
    for arg in argv:
        logger.info("  %s", str(arg))
    logger.info("")
    # Create GUI
    gui = GraphicUserInterface()
    gui.set_theme("Dark", "blue")
    gui.set_footbar_text(VERSION_STRING)
    gui.set_button("Device Info", sidebar_btn_device_info_press)
    gui.set_button("Flash FW", sidebar_btn_flash_fw_press)
    gui.set_button("Debug", sidebar_btn_debug_press)
    gui.set_button("About", sidebar_btn_about_press)
    gui.create_window("pyuJFlasher", WINDOW_WIDTH, WINDOW_HEIGHT)
    gui.create_content()
    gui.loop()
    return 0


###############################################################################
# Runnable Main Script Detection
###############################################################################

if __name__ == "__main__":
    logger.info("Application Launch")
    RETURN_CODE = main(len(sys_argv)-1, sys_argv[1:])
    logger.info("Application Exit (%d)", RETURN_CODE)
    sys_exit(RETURN_CODE)
