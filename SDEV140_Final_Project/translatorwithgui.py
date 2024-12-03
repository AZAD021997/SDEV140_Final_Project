# FILE:translatorwithgui.py
# DATE:2024-12-02
# AUTHOR:Azad Baidha Tchagnaou
# DESCRIPTION: """This program will translate from one language to another. SDEV 140's final project."

from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

root=Tk()
root.title("Communication Multi Languages Translator")
root.geometry("1100x500")
root.resizable(False,False)