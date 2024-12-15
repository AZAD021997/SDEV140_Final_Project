# File:Communication_App.py
# DATE: 2024-12-08
# AUTHOR:Azad Baidha Tchagnaou
# DESCRIPTION: """This program will allows us to translate from one language to another."""

import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class CommunicationApp:
    def __init__(self, root):
        self.root = root
        
        self.root.title("Communication-Multi-Language Translator App")

        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Create an instance of Translator
        self.translator = Translator()
        
        # Header
        self.header_frame = tk.Frame(self.root)
        
        self.header_frame.pack(fill="x")
        self.header_label = tk.Label(self.header_frame, text="Communication-Multi-Language Translator App", font=("Arial",16, "bold"))
        self.header_label.pack()
        
        #Language Selection
        self.language_frame = tk.Frame(self.root)
        self.language_frame.pack(fill="x")
        self.primary_language_label = tk.Label(self.language_frame, text="Primary Language:", font=("Arial", 12))

        self.primary_language_label.pack(side="left")
        self.primary_language_var = tk.StringVar()
        self.primary_language_menu = ttk.Combobox(self.language_frame, textvariable=self.primary_language_var)
        self.primary_language_menu['values'] = list(LANGUAGES.values())
        self.primary_language_menu.pack(side="left")
        self.target_language_label = tk.Label(self.language_frame, text="Target Language:", font=("Arial", 12, ))
        self.target_language_label.pack(side="left")
        self.target_language_var = tk.StringVar()
        self.target_language_menu = ttk.Combobox(self.language_frame, textvariable=self.target_language_var)
        self.target_language_menu['values'] = list(LANGUAGES.values())
        self.target_language_menu.pack(side="left")

        # Translation Input
        self.translation_input_frame = tk.Frame(self.root)

        self.translation_input_frame.pack(fill="x")

        self.translation_input_label = tk.Label(self.translation_input_frame, text="Enter text to translate:", font=("Arial", 12))

        self.translation_input_label.pack(side="left")

        self.translation_input_entry = tk.Text(self.translation_input_frame, height=10, width=50, font=("Arial", 12, ))

        self.translation_input_entry.pack(side="left")
        

        # Translation Button
    
        self.translation_button_frame = tk.Frame(self.root)

        self.translation_button_frame.pack(fill="x")
        self.translation_button = tk.Button(self.translation_button_frame, text="Translate", command=self.translate_text, font=("Arial", 12, "bold"))
    
        self.translation_button.pack(side="left")

        # Translation Output

        self.translation_output_frame = tk.Frame(self.root)

        self.translation_output_frame.pack(fill="x")

        self.translation_output_label = tk.Label(self.translation_output_frame, text="Translated text:", font=("Arial", 12))

        self.translation_output_label.pack(side="left")

        self.translation_output_text = tk.Text(self.translation_output_frame, height=10, width=50, font=("Arial", 12,))
                                       
        self.translation_output_text.pack(side="left")
        
        # Translation Button
        self.translation_button_frame = tk.Frame(self.root)
        self.translation_button_frame.pack(fill="x")
        self.translation_button = tk.Button(self.translation_button_frame, text="Translate", command=self.translate_text, font=("Arial", 12, "bold"))
        self.translation_button.pack(side= "left")
    def translate_text(self):
            translator = Translator()
            primary_language = self.primary_language_var.get()
            target_language = self.target_language_var.get()
            text_to_translate = self.translation_input_entry.get("1.0", "end-1c")
            translation = translator.translate(text_to_translate, src=primary_language, dest=target_language)
            self.translation_output_text.delete("1.0", "end")
            self.translation_output_text.insert("1.0", translation.text)

if __name__ == "__main__":
        root = tk.Tk()
        app = CommunicationApp(root)
        root.mainloop()

        