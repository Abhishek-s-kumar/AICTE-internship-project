import cv2
import os
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog

def generate_lookup_tables():
    encrypt_table = {chr(i): i for i in range(256)}
    decrypt_table = {i: chr(i) for i in range(256)}
    return encrypt_table, decrypt_table

def encrypt_image(img, message):
    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3

def decrypt_message(img):
    n, m, z = 0, 0, 0
    decrypted_message = ""
    for _ in range(len(msg)):
        decrypted_message += chr(img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % 3
    return decrypted_message

def open_image():
    file_path = tk.filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    img = cv2.imread(file_path)
    if img is None:
        tk.messagebox.showerror("Error", "Failed to load the image.")
    return img

def encrypt_and_save():
    global img, msg, encrypt_password_entry
    img = open_image()
    if img is not None:
        msg = msg_entry.get()
        encrypt_image(img, msg)
        cv2.imwrite("encryptedImage.jpg", img)
        tk.messagebox.showinfo("Success", "Image encrypted and saved as encryptedImage.jpg.")
    msg_entry.delete(0, tk.END)  # Clear the message entry

def decrypt_and_display():
    global img, msg, encrypt_password_entry
    decrypt_password = decrypt_password_entry.get()
    if decrypt_password == encrypt_password_entry.get():
        decrypted_msg = decrypt_message(img)
        tk.messagebox.showinfo("Decryption Result", f"Decrypted message: {decrypted_msg}")
    else:
        tk.messagebox.showerror("Error", "Incorrect password.")

# Main GUI window
root = tk.Tk()
root.title("Image Encryption/Decryption")

# Text Entry Boxes
msg_label = tk.Label(root, text="Enter Secret Message:")
msg_label.pack()
msg_entry = tk.Entry(root)
msg_entry.pack(pady=5)

encrypt_password_label = tk.Label(root, text="Enter Encryption Passcode:")
encrypt_password_label.pack()
encrypt_password_entry = tk.Entry(root, show="*")
encrypt_password_entry.pack(pady=5)

decrypt_password_label = tk.Label(root, text="Enter Decryption Passcode:")
decrypt_password_label.pack()
decrypt_password_entry = tk.Entry(root, show="*")
decrypt_password_entry.pack(pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_and_save)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_and_display)
decrypt_button.pack(pady=10)

# Run the GUI
root.mainloop()
