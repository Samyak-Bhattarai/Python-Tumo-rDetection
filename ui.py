import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from test import test_model

# Creating the main window
root = tk.Tk()
root.title("Drag and Drop Image")
root.geometry("680x680")

image_name = ""  
global predict
def on_drop(event=None):
    global image_named
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")]
    )
    if file_path:
        image_name = file_path.split("/")[-1]
        predict = test_model(image_name)
        img = Image.open(file_path)
        img.thumbnail((400, 400))  
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        image_name_label.config(text=f"Image Name: {image_name}")
        check_value(predict)

def check_value(predict):
    if predict == 0:
        value_label.config(text="No tumor", font=("Helvetica", 40))
    else:
        value_label.config(text="Tumor Found", font=("Helvetica", 40))

def on_click():
    on_drop()

def on_check():
    check_value(predict)


image_label = tk.Label(root)
image_label.pack(pady=20)

drop_button = tk.Button(root, text="Drop Image Here", command=on_drop)
drop_button.pack(pady=20)


click_button = tk.Button(root, text="Click to Add Image", command=on_click)
click_button.pack(pady=20)

check_button = tk.Button(root, text="Check Value", command=on_check)
check_button.pack(pady=20)

value_label = tk.Label(root, text="")
value_label.pack(pady=20)


image_name_label = tk.Label(root, text="")
image_name_label.pack(pady=20)


root.mainloop()
