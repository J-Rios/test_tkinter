# -*- coding: utf-8 -*-

'''
Script:
    gui.py
Description:
    TKinter Graphical User Interface implementation.
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

from os import path as os_path


###############################################################################
# TKinter Libraries
###############################################################################

from customtkinter import CTk as tk_window
from customtkinter import CTkFrame as tk_frame
from customtkinter import CTkCanvas as tk_canvas
from customtkinter import CTkButton as tk_button
from customtkinter import CTkLabel as tk_label
from customtkinter import CTkFont as tk_font
from customtkinter import set_appearance_mode as tk_set_appearance_mode
from customtkinter import set_default_color_theme as tk_set_default_color_theme

from tkinter import PhotoImage as tk_image
from tkinter import NW


###############################################################################
# Constants & Configurations
###############################################################################

# Actual constants.py full path directory name
SCRIPT_PATH = os_path.dirname(os_path.realpath(__file__))
RESOURCES_PATH = f"{SCRIPT_PATH}/../res"

# Used Colors
COLORS = \
{
    "window_bg": "#28292A",  # Low Dark Grey
    "up_headbar_bg": "#28292A",  # Low Dark Grey
    "up_headbar_header_fg": "#FFFFFF",  # White
    "left_sidebar_bg": "#2B2B2B",  # High Dark Grey
    "left_sidebar_btn_bg": "#252526",  # Medium Dark Grey
    "left_sidebar_btn_fg": "#C7C7C7",  # White-Grey
    "left_sidebar_btn_mouse_hover_bg": "#353737",  # Light Grey
    "left_sidebar_btn_mouse_hover_fg": "#C7C7C7",  # White-Grey
    "left_sidebar_btn_selected_bg": "#04395E",  # Dark Blue
    "left_sidebar_btn_selected_mouse_hover_bg": "#06558C",  # Light Blue
    "footbar_bg": "#1D6AB8",  # Blue
    # Orange CE9178
}


###############################################################################
# Auxiliary Classes
###############################################################################

class Button():
    '''Button UI element class.'''
    def __init__(self):
        self.uid = "0"
        self.label = "None"
        self.callback = None


###############################################################################
# GUI Class
###############################################################################

class GraphicUserInterface():
    '''
    Graphical User Interface Class that defines all the visual elements
    of an Application.
    '''

    def __init__(self):
        '''GraphicUserInterface Constructor.'''
        self.gui_objects = []
        self.window = None
        self.window_width = 0
        self.window_height = 0
        self.left_sidebar = None
        self.up_headbar = None
        self.btn_id = 0
        self.cb_buttons = {}
        self.footbar_text = ""

    def set_footbar_text(self, text):
        self.footbar_text = text

    def set_button(self, label, callback):
        '''Set a button on the left sidebar menu.'''
        btn = Button()
        btn.label = label
        btn.callback = callback
        btn.uid = self.btn_id
        self.btn_id = self.btn_id + 1
        self.cb_buttons[btn.uid] = btn

    def set_theme(self, appearance, color):
        '''
        Setup GUI Theme and colors.
            - appearance: "System" (standard), "Dark", "Light"
            - color: "blue" (standard), "green", "dark-blue", etc
        '''
        tk_set_appearance_mode(appearance)
        tk_set_default_color_theme(color)

    def create_window(self, title, width=None, height=None):
        '''Setup and create the TKinter Window.'''
        self.window = tk_window()
        self.window.title(title)
        self.window_width = self.window.winfo_screenwidth()
        self.window_height = self.window.winfo_screenheight()
        self.window_min_width = self.window_width
        self.window_min_height = self.window_height
        if width is not None:
            self.window_min_width = width
        if height is not None:
            self.window_min_height = height
        self.window.minsize(width=self.window_min_width,
                            height=self.window_min_height)
        size_str = "{}x{}".format(
            self.window_min_width, self.window_min_height)
        self.window.geometry(size_str)
        self.create_grid_layout()

    def create_grid_layout(self):
        self.window.grid_rowconfigure(0, weight=1)

    def create_content(self):
        self.create_left_sidebar()
        self.create_content_frame()
        self.create_footbar()

    def create_left_sidebar(self):
        # Frame Creation
        self.left_sidebar = tk_frame(
            self.window,
            bg_color=COLORS["left_sidebar_bg"],
            height=self.window_height,
            width=int(self.window_min_height / 3),
            corner_radius=0
        )
        self.left_sidebar.grid(
            row=0, column=0, padx=(5, 5), pady=(0, 0), sticky="ns")
        # Sidebar Logo
        #self.image = tk_image(file=f"{RESOURCES_PATH}/sidebar_logo.png")
        #self.left_sidebar_img = tk_canvas(
        #    self.left_sidebar,
        #    bg = COLORS["left_sidebar_bg"],
        #    width = self.image.width(),
        #    height = self.image.height(),
        #    highlightthickness = 0
        #)
        #self.left_sidebar_img.grid(row=0, column=0, padx=20, pady=(75, 70))
        #self.left_sidebar_img.create_image(0, 0, image=self.image, anchor=NW)
        # Sidebar Title
        self.sidebar_title = tk_label(
            self.left_sidebar, text="Menu",
            font=tk_font(size=20, weight="bold")
        )
        self.sidebar_title.grid(row=1, column=0, padx=20, pady=(10, 30))
        # Sidebar Buttons
        row = 2
        self.left_sidebar_buttons = {}
        for i in range(len(self.cb_buttons)):
            btn = self.cb_buttons[i]
            self.left_sidebar_buttons[btn.uid] = tk_button(self.left_sidebar,
                text = btn.label,
                command = lambda \
                    btn_uid=btn.uid: self.sidebar_btn_press(btn_uid)
            )
            self.left_sidebar_buttons[btn.uid].grid(row=row, padx=20, pady=10)
            row = row + 1

    def sidebar_btn_press(self, button_id):
        if button_id in self.cb_buttons:
            btn = self.cb_buttons[button_id]
            print("Button \"{}\" pressed".format(btn.label))
            self.header_label.configure(text=btn.label)
            btn.callback()

    def create_content_frame(self):
        # Content Frame
        self.content = tk_frame(self.window,
            height=self.window_height, width=self.window_width)
        self.content.grid(row=0, column=1, padx=(25, 30), pady=(30, 30),
                          sticky="nsew")
        self.window.grid_columnconfigure(1, weight=3)
        # Content Title Label
        self.header_label = tk_label(self.content,
            text=self.cb_buttons[0].label,
            font=tk_font(size=20, weight="bold")
        )
        self.header_label.grid(row=0, column=0)
        self.header_label.pack(anchor="center", pady=20)

    def create_footbar(self):
        # Content Frame
        self.footer = tk_frame(self.window,
            bg_color=COLORS["footbar_bg"], fg_color=COLORS["footbar_bg"])
        self.footer.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.footer.grid_columnconfigure(0, weight=1)
        # Footer Version Label
        self.footer_label = tk_label(self.footer,
            text=self.footbar_text,
            font=tk_font(size=10, weight="bold"),
            bg_color=COLORS["footbar_bg"],
        )
        self.footer_label.grid(sticky="e", padx=(0, 15))

    def loop(self):
        self.window.mainloop()

    def update(self):
        self.window.update()

    def close(self):
        self.window.destroy()
